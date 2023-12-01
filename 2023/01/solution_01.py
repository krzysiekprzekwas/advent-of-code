with open("input_01.txt", "r") as f:
    data = f.read().splitlines()

    # 1

    sum_1 = 0
    for line in data:
        digits = list(filter(str.isdigit, line))
        sum_1 += int(digits[0] + digits[-1])


    # 2

    letters_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    sum_2 = 0
    for line in data:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)

            for letters, number in letters_map.items():
                if line[i:].startswith(letters):
                    digits.append(number)

        sum_2 += int(digits[0] + digits[-1])

print(sum_1)
print(sum_2)
