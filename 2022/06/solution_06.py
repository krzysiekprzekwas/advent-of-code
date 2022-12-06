def get_marker(message, marker_length):
    for i in range(marker_length, len(message)):
        if len(set(message[i-marker_length:i])) == marker_length:
           return i

with open("input_06.txt", encoding="utf-8") as f:
    file_data = f.read()

print(get_marker(file_data, 4))
print(get_marker(file_data, 14))