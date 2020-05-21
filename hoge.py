
filename = "./ciger_list.txt"

with open(filename) as f:
    lines = f.read().splitlines()
    print(lines)
