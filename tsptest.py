import json, sys

with open("distances.json", "r") as f:
    distances = json.load(f)


def test(func):
    drunk_factor = 1.05 # gets 5% slower at each pub
    names = sorted(distances.keys())
    route = func(distances, names, drunk_factor)

    if len(route) == 0:
        print("ERR: Needs to be contain at least one pub")

    # Test if same start and end
    if route[0] != route[-1]:
        print("ERR: Need to start and end at the same place")
        return

    # Test if it visits all the pubs
    visited = set(route)
    for pub in names:
        if pub not in visited:
            print("ERR: Did not visit {}".format(pub))
            return

    # Check time
    t = 0
    speed = 1.38889 #ms 5 kmph, average walking pace
    last = route[0]
    for pub in route[1:]:
        d = distances[last][pub]
        t += d / speed
        speed / 1.05 # gets 5% slower at each pub
        last = pub
    print(t)

def read_from_stdin(distances, names, drunk_factor):
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    return lines

if __name__ == "__main__":
    test(read_from_stdin)
