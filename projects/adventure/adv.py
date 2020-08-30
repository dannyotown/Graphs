from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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
opp_directions = {'s': 'n', 'n': 's', 'w': 'e', 'e': 'w'}


def traverse_world():
    # create visited dictionary
    visited = dict()
    # last move
    last_move = (None, None)
    # while visited rooms is less than room graph
    count = 0
    while count < 25:
        # search as deep as possible (DFS)
        world_dft(visited, last_move)
        # find room with undiscovered path
        find_new_path = world_bfs(visited)
        # if no path, all rooms have been visited
        if len(find_new_path) == 0:
            # return traversal list
            return traversal_path
        else:
            # otherwise move player to room with undiscovered path
            for move in find_new_path:
                # hold old room
                old_room = player.current_room.id
                # update last move
                last_move = (move, old_room)
                # move player
                player.travel(move)
                # add to traversal path
                traversal_path.append(move)
        count += 1
    print(visited, 'vis')


def world_dft(visited, last_move):
    # create stack
    stack = []
    # stack visit
    stack_visit = set()
    # insert current room into stack
    stack.insert(0, player.current_room.id)
    # while len of stack is not 0
    while len(stack) != 0:
        # get current room
        current_room = stack[0]
        # pop off stack
        stack.pop(0)
        # direction list
        random_path = []
        # check to see if in visited overall
        if current_room not in visited:
            # get rooms exits
            current_room_exits = player.current_room.get_exits()
          # otherwise create room in visited with exit ?s
            visited[player.current_room.id] = {}
           # for exit rooms in visited
            if last_move[0] is not None:
                visited[current_room][opp_directions[last_move[0]]
                                      ] = last_move[1]
            for direction in current_room_exits:
                # mark directions with ?
                if direction not in visited[current_room]:
                    visited[current_room][direction] = '?'
                    random_path.append(direction)
        else:
            # for directions in room visited
            for direction, value in visited[player.current_room.id].items():
                if value == '?':
                    random_path.append(direction)
        if len(random_path) != 0:
            random_direction = random.choice(random_path)
            print(random_direction)
            # check to make sure we haven't visited the room yet
            if current_room not in stack_visit:
                # add to visit list
                stack_visit.add(player.current_room.id)
                # hold old room
                old_room = player.current_room.id
                # move player
                player.travel(random_direction)
                # add vlaue to traversal path
                traversal_path.append(random_direction)
                # update old_room's direction with new room
                visited[old_room][random_direction] = player.current_room.id
                # update last move
                last_move = (random_direction, old_room)
                # insert new value into stack
                stack.insert(0, player.current_room.id)

        # otherwise you are at exit
        else:
            return player.current_room.id


def world_bfs(visited):
    # create que
    que = []
    # moves
    moves = []
    # create visited
    que_visited = set()
    # insert current room into que
    que.append([player.current_room.id])
    # while que has room
    while len(que) != 0:
        # get current que path
        current_que_path = que[0]
        # get current que room
        current_que_room = current_que_path[-1]
        # pop off que
        que.pop(0)
        # if it hasn't been visited
        if current_que_room not in que_visited:
            # if its keys have question marks
            for direction, value in visited[current_que_room].items():
                if value == '?' and value not in que_visited:
                    print(visited)
                    print(player.current_room.id)
                    print(moves)
                    return moves
                else:
                    if value not in que_visited:
                        moves.append(direction)
                        que.append(current_que_path+[value])
                        que_visited.add(current_que_room)
    return []


traverse_world()
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
