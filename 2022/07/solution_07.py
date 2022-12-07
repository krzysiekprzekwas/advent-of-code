with open("input_07.txt") as file:
    lines = file.read().splitlines()

dirs = {'/':0}
files = {}
current_path = ''

for line in lines:
    cmd_parts = line.split()
    if cmd_parts[0] == '$':
        if cmd_parts[1] == 'cd':
            if cmd_parts[2] == '..':
                current_path= '/'.join(current_path.split('/')[:-1])
            else:
                current_path = current_path + '/' + cmd_parts[2]
    else:
        if cmd_parts[0]=="dir":
            dirs[str(current_path + '/' + cmd_parts[1])] = 0
        else:
            files[str(current_path + '/' + cmd_parts[1])] = int(cmd_parts[0])

for d in dirs:
    for f in files:
        if f.startswith(d):
            dirs[d] += files[f]

print(sum(s for s in dirs.values() if s <= 100_000))
print(min(s for s in dirs.values() if 70_000_000 - dirs['/'] + s >= 30_000_000))