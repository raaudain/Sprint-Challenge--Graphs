from room import Room
from player import Player
from world import World

import sys
sys.path.append("../Graphs/projects/graph")
from util import Queue, Stack
from graph import Graph
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


# Used to move back when you hit a deadend
move_back = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}

def traversal(room, visited_room = set(), path = []):

    for move in player.current_room.get_exits():
        
        # Move player if next_room is not None
        # See player.py
        player.travel(move)
        
        # If player hasn't been in current room add to visited set
        if player.current_room.id not in visited_room:
            visited_room.add(player.current_room.id)
            
            path.append(move)
            
            # Run function again
            traversal(room)
        
        # If player has been in current room,
        # turn back 
        else:
            path.append(move)
            player.travel(move_back[move])
    print(path)
    return path

# Fill this out with directions to walk
#traversal_path = ['n', 'n']
traversal_path = traversal(player.current_room.id)
#traversal_path = []


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
