from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
    # starting room
    # while visited rooms is less than room graph
    while len(visited) != len(room_graph):
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
            for moves in find_new_path:
                for direction, value in visited[player.current_room.id].items():
                    if moves == value:
                        # hold old room
                        old_room = player.current_room.id
                        # update last move
                        last_move = (direction, old_room)
                        # move player
                        player.travel(direction)
                        # add to traversal path
                        traversal_path.append(direction)


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
            visited[current_room] = {}
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
            visited[current_room][opp_directions[last_move[0]]
                                  ] = last_move[1]
            for direction, value in visited[current_room].items():
                if value == '?':
                    random_path.append(direction)
        if len(random_path) != 0:
            random_direction = random.choice(random_path)
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
    que = []
    que.append([player.current_room.id])
    # create an empty set to track visited verticies
    tracker = set()
    # while the queue is not empty:
    while len(que) != 0:
        # get current vertex path
        current_path = que[0]
        current_vertex = current_path[-1]
        que.pop(0)
        # check if current vertex has not been visited
        if current_vertex not in tracker:
            # mark the current vertex as visited
            tracker.add(current_vertex)
            # Check if the current vertex is destination and return
            for value in visited[current_vertex].values():
                que.append(current_path + [value])
                if value == '?':
                    return current_path[1:]
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
