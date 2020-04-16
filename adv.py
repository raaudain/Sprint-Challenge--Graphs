from room import Room
from player import Player
from world import World

import sys
sys.path.append("../Graphs/projects/graph")
from util import Queue, Stack
import random
from ast import literal_eval

# Load world
world = World()
#room = Room()

# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


player = Player(world.starting_room)

def dft(starting_room):
    #room = Room()
    
    stack = Stack()
    stack.push([starting_room.id])
    
    
    
    visited = set()
    
    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        print(vertex)
        
        # if vertex not in visited:
        #     print(vertex, player)
        #     visited.add(vertex)
            
        for step in world.rooms:
            if step not in visited:
                print(vertex, player)
                visited.add(step)
            
            print(step, player)
            temp_path = path.copy()
            temp_path.append(step)
            stack.push(temp_path)
    return

# def bft(starting_room):
#     visited = set()
#     queue = Queue()
#     queue.enqueue([starting_room.id])
    
#     while queue.size() > 0:
#         path = queue.dequeue()
#         vertex = path[-1]
#         # test = room.id
        
#         if vertex not in visited:
#             print(vertex)
#             visited.add(vertex)
            
#             for step in world.rooms:
#                 print(step, world.rooms[vertex])
#                 temp_path = path.copy()
#                 temp_path.append(step)
#                 queue.enqueue(temp_path)

# Fill this out with directions to walk
#traversal_path = ['n', 'n']
traversal_path = dft(player.current_room)

#print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
