def score(item):
    return ord(item) - ord("a") + 1 if item.islower() else ord(item) - ord("A") + 27

with open("input_03.txt", "r") as f:
    file_data = f.read().splitlines()
    
    score_1 = score_2 = 0

    for item in file_data:
        middle = len(item) // 2
        rucksack_1, rucksack_2 = item[:middle], item[middle:]
        (duplicate_item, ) = set(rucksack_1).intersection(rucksack_2)
        score_1 += score(duplicate_item)

    for item in range(0, len(file_data), 3):
        threepack = file_data[item:item + 3]
        (badge, ) = set(threepack[0]).intersection(threepack[1]).intersection(threepack[2])
        score_2 += score(badge)
 
print(score_1)
print(score_2)