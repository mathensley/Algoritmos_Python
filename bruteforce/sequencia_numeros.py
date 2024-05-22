def sub_num(numbers):
    n = len(numbers)
    max_seq = 0
    for i in range(n):
        atual = numbers[i]
        count = 1
        for j in range(i+1, n):
            if (numbers[i] < numbers[j] 
                and atual < numbers[j]):
                    atual = numbers[j]
                    count += 1
        if max_seq < count:
            max_seq = count
    return max_seq

numbers = [7, 6, 10, 3, 5, 4, 8, 9, 1]
print(sub_num(numbers))