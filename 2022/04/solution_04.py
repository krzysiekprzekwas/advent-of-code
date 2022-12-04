def range_fully_contains(a1, b1, a2, b2):
    return a2 >= a1 and b2 <= b1

def range_overlaps(a1, b1, a2, b2):
    return max(a1,a2) <= min(b1,b2)

with open("input_04.txt", "r") as f:
    file_data = f.read().splitlines()

    score_1 = score_2 = 0

    for pair in file_data:
        elf_1, elf_2 = pair.split(',')

        elf_1_min, elf_1_max = map(int, elf_1.split('-'))
        elf_2_min, elf_2_max = map(int, elf_2.split('-'))

        if range_overlaps(elf_2_min, elf_2_max, elf_1_min, elf_1_max):
            score_2 += 1
            
            if range_fully_contains(elf_1_min, elf_1_max, elf_2_min, elf_2_max) or range_fully_contains(elf_2_min, elf_2_max, elf_1_min, elf_1_max):
                score_1 += 1


print(score_1)
print(score_2)