with open("input_10.txt") as file:
    registry_value = 1
    cycle_count = 1
    all_signals = []

    for line in file:
        # Part 1
        if line.strip() == 'noop':
            all_signals.append(registry_value)
            cycle_count += 1
        else:
            all_signals.append(registry_value)
            all_signals.append(registry_value)
            cycle_count += 2
            registry_value += int(line.strip().split()[1])
        
    # Part 2
    for i in range(6):
        for j in range(40):
            cycle = i * 40 + j
            if all_signals[cycle] in range(j - 1, j + 2):
                print('#', end='')
            else:
                print('.', end='')
        print('')

print(all_signals[20]*20 + all_signals[60]*60 + all_signals[100]*100 + all_signals[140]*140 + all_signals[180]*180 + all_signals[220]*220)