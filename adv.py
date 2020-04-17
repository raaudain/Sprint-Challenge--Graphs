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
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


player = Player(world.starting_room)



def dft(starting_room):

    stack = Stack()
    stack.push([starting_room])
    
    rooms = []
    
    for i in world.rooms:
        rooms.append(i)
    
    
    
    # print(rooms)
    path = []
    visited = set()
    
    
        #moves = stack.pop()
        #person = moves[-1]
    
        # if person not in visited:
        #     visited.add(person)
    while stack.size() > 0:
        test = stack.pop()
        vertex = test[-1]
        
    
            
        # if vertex not in visited:
        #     visited.add(vertex)
            
    
        for move in player.current_room.get_exits():
            
            if move not in visited:
                
                player.travel(move)
                print(move)
            else:
                #path = path+
            # player.travel(move)
            #print(player.current_room.get_exits()[vertex])
                print("hey", move)
                temp_path = path.copy()
                temp_path.append(move)
                stack.push(move)
                #visited.append(player.current_room.id)
                
                # temp_path = move.copy()
                # temp_path.append(move)
                # print("temp", temp_path)
                # stack.push(temp_path)
                # path.append(temp_path)
            
            # print(path)
        #path = temp_path
            
    # print("path", path[1:])
    # print(visited)
    # print("stack", stack)
        
    return path[1:]

#def bft(starting_room):
    
    # queue = Queue()
    # queue.enqueue([starting_room])
    
    # path = []
    # visited = set()
    
    # while queue.size() > 0:
    #     moves = queue.dequeue()
    #     person = moves[-1]
    
    #     # if person not in visited:
    #     #     visited.add(person)
            
    #     for move in player.current_room.get_exits():
    #         temp_path = moves.copy()
    #         temp_path.append(move)
            
    #         queue.enqueue(temp_path)
    #         path.append(move)
            
    #         print(path)
                
    # return path

# Fill this out with directions to walk
#traversal_path = ['n', 'n']
traversal_path = dft(player.current_room.id)

# print("1", player.current_room.id)
# print("2", player.current_room.get_exits())
#print(player.travel(direction))


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
