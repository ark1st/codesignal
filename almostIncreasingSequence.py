def almostIncreasingSequence(sequence):
    count = 0

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            count += 1
            if i >= 1 and sequence[i + 1] <= sequence[i - 1]:
                if len(sequence) - 2 > i and sequence[i + 2] <= sequence[i]:
                    count += 1

    return count <= 1


