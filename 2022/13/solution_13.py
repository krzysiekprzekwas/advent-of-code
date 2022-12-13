from functools import cmp_to_key


def compare(left_item, right_item):
    # For ints lower integer should come first
    if type(left_item) == type(right_item) == int:
        return left_item - right_item
    # For lists compare element wise
    elif type(left_item) == type(right_item) == list:
        for i, j in zip(left_item, right_item):
            # Compare elements
            if compare(i, j) == 0:
                continue
            else:
                return compare(i, j)

        # When elements are the same compare list lengths
        return len(left_item) - len(right_item)
    # When type is mismatched, cast as array
    elif type(left_item) == int and type(right_item) != int:
         return compare([left_item], right_item)
    elif type(left_item) != int and type(right_item) == int:
        return compare(left_item, [right_item])
    else:
        print(f"Unexpected comparision between {left_item} and {right_item}")

answer_1 = []
packets = []

with open("input_13.txt") as file:
    chunks = file.read().split('\n\n')

    for idx, chunk in enumerate(chunks):
        line_1, line_2 = chunk.splitlines()
        packets.extend([eval(line_1), eval(line_2)])
        order = compare(eval(line_1), eval(line_2))
        if order < 0:
            answer_1.append(idx+1)

packets.extend([[[2]], [[6]]])

sorted_packets = sorted(packets, key=cmp_to_key(compare))

index_1 = sorted_packets.index([[2]]) + 1
index_2 = sorted_packets.index([[6]]) + 1

print(sum(answer_1))
print(index_1 * index_2)