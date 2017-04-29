import tsptest

def alpha(distances, names, drunk_factor):
    names.append(names[0])
    return names

tsptest.test(alpha)
