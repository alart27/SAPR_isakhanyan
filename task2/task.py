from collections import defaultdict
import csv


def task(data: str):
    parents = defaultdict(list)
    children = defaultdict(list)

    inp = csv.reader(data.splitlines(), delimiter=',')

    for line in inp:
        
        if not line:
            continue

        par, chi = line
        parents[chi].append(par)
        children[par].append(chi)
        if par not in parents:
            parents[par] = []
        if chi not in children:
            children[chi] = []

    root = next(key for key in parents if not parents[key])
    leaves = [key for key in children if not children[key]]
    result_dict = {key: {'r1': set(children[key]), 'r2': set(parents[key]), 'r3': set(), 'r4': set(), 'r5': set()}
                    for key in parents}

    stack = [root]
    while stack:
        cur_node = stack.pop()
        for child in children[cur_node]:
            result_dict[child]['r4'] |= result_dict[cur_node]['r2'] | result_dict[cur_node]['r4']
            result_dict[child]['r5'] |= result_dict[cur_node]['r1'] - {child}
            stack.append(child)

    stack = list(leaves)
    while stack:
        cur_node = stack.pop()
        for parent in parents[cur_node]:
            result_dict[parent]['r3'] |= result_dict[cur_node]['r1'] | result_dict[cur_node]['r3']
            if parent not in stack:
                stack.append(parent)

    rs = ('r1', 'r2', 'r3', 'r4', 'r5')
    csv_output = '\n'.join([','.join([str(len(result_dict[node][r])) for r in rs]) for node in sorted(result_dict)]) + '\n'

    return csv_output

if __name__ == '__main__':
    input_data = "1,2\n1,3\n3,4\n3,5\n"
    print(task(input_data))
