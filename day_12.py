from collections import defaultdict

test_input = """\
start-qs
qs-jz
start-lm
qb-QV
QV-dr
QV-end
ni-qb
VH-jz
qs-lm
qb-end
dr-fu
jz-lm
start-VH
QV-jz
VH-qs
lm-dr
dr-ni
ni-jz
lm-QV
jz-dr
ni-end
VH-dr
VH-ni
qb-HE
"""


def calculate_paths(input):
    paths = defaultdict(set)

    for path in input.splitlines():
        source, destination = path.split('-')

        # graph is bidrectional so a-b means path from a to b and b to a
        paths[source].add(destination)
        paths[destination].add(source)

    all_paths = set()
    nodes_to_process = [('start',)]
    while nodes_to_process:
        path = nodes_to_process.pop()

        if path[-1] == 'end':
            print(f'\tadding {path} to all_paths because it ends with `end`')
            all_paths.add(path)
            continue

        for cand in paths[path[-1]]:  # get all of the nodes that the last node in the current path has a connection to
            if not cand.islower() or cand not in path:
                nodes_to_process.append((*path, cand))

    return len(all_paths)


print(calculate_paths(test_input))
