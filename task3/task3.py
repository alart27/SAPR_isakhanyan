import csv
import math


def task(data: str):
    inp = csv.reader(data.splitlines(), delimiter=',')
    rows = list(inp)
    n = len(rows)
    graph_entropy = 0
    for row in rows:
        for l in row:
            lval = l
            if lval != '0':
                fraction = float(lval) / (n - 1)
                graph_entropy += -fraction * math.log2(fraction)
    return round(graph_entropy, 1)


if __name__ == '__main__':
    input_data = '2,0,2,0,0\n0,1,0,0,1\n2,1,0,0,1\n0,1,0,1,1\n0,1,0,1,1\n'
    result = task(input_data)
    print(result)