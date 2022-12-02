with open("input_01.txt", "r") as f:
	# Get the lines, split by elf
    file_data = f.read().split("\n\n")
 
	# Map from strings to ints
    data = [[int(calories) for calories in elf.splitlines()] for elf in file_data]
 
	# Sum calories per elf
    elf_sums = [sum(calories) for calories in data]
 
	# Sort elfs by summed calories
    sorted_elf_sums = sorted(elf_sums)
 
print(sorted_elf_sums[-1])
print(sum(sorted_elf_sums[-3:]))