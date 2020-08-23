def map_ancestors(ancestors):
    d = {}
    for i in ancestors:
        if i[1] in d:
            d[i[1]].add(i[0])
        else:
            d[i[1]] = set()
            d[i[1]].add(i[0])
    return d


def earliest_ancestor(ancestors, starting_node):
    # graph the ancestors
    a_map = map_ancestors(ancestors)
    print(a_map)
    # create stack
    stack = []
    # create visited set
    visited = set()
    # insert starting person list into stack
    stack.insert(0, [starting_node])
    # longest_path
    longest_path = []
    # while stack > 0:
    while len(stack) > 0:
        # get current path
        current_path = stack[0]
    # get current person
        current_person = current_path[-1]
        stack.pop(0)
    # if current person not in a_map and longest path arr length = 0
        if current_person not in a_map and len(longest_path) == 0:
            # return -1
            return -1
        else:
            # if person has not been visited
            if current_person not in visited:
                # add current person to visited
                visited.add(current_person)
                # if they are parent, continue
                if current_person not in a_map:
                    continue
                else:
                    for value in a_map[current_person]:
                        # add parents to longest path and stack
                        stack.insert(0, current_path + [value])
                        longest_path.append(current_path + [value])

    return longest_path[-1][-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 3))  # 10
# print(earliest_ancestor(test_ancestors, 2))  # -1
