def range_fully_contains(a1, b1, a2, b2):
    return int(a2) >= int(a1) and int(b2) <= int(b1)

def range_overlaps(a1, b1, a2, b2):
    return max(int(a1),int(a2)) <= min(int(b1),int(b2))

with open("input_04.txt", "r") as f:
    file_data = f.read().splitlines()

    score_1 = score_2 = 0

    for pair in file_data:
        elf_1, elf_2 = pair.split(',')

        elf_1_min, elf_1_max = elf_1.split('-')
        elf_2_min, elf_2_max = elf_2.split('-')

        if range_fully_contains(elf_1_min, elf_1_max, elf_2_min, elf_2_max) or range_fully_contains(elf_2_min, elf_2_max, elf_1_min, elf_1_max):
            score_1 += 1

        if range_overlaps(elf_1_min, elf_1_max, elf_2_min, elf_2_max) or range_overlaps(elf_2_min, elf_2_max, elf_1_min, elf_1_max):
            score_2 += 1

print(score_1)
print(score_2)