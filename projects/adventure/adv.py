from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def traverse_world():
    # visited dictionary
    visited = {}
    # create stack for dft
    stack = []
    # insert current room id in stack
    stack.insert(0, player.current_room.id)
    # hold opposite move and last room
    last_room = (None, None)
    while len(stack) > 0:
        # get current room
        current_room = stack[-1]
        # get all directions you can move
        room_exits = player.current_room.get_exits()
        # remove room from stack
        stack.pop(0)
        # add empty dictionary in visited dictionary
        visited[current_room] = {}
        # for all the exits in room, add ? value in keys dictionary (in visited)
        for ex in room_exits:
            # check move from last room and change the opposite direction value
            if last_room[0] is not None and last_room[0] == ex:
                visited[current_room][ex] = last_room[1]
            else:
                # add exits to visited dictionary with ? holder
                visited[current_room][ex] = '?'
        # if player can move north
        if 'n' in visited[current_room]:
            # hold the OPPOSITE move and old room
            last_room = ('s', current_room)
            # travel north
            player.travel('n')
            # add to traversal path
            traversal_path.append('n')
            # update the old rooms n value
            visited[last_room[1]]['n'] = player.current_room.id
            # add current room to stack
            stack.insert(0, player.current_room.id)
    print(visited)


traverse_world()
print(traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
