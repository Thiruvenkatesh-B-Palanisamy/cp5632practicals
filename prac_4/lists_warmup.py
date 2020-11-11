numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = "ten"
print(numbers)
numbers[-1] = 0
print(numbers)
num_slice = numbers[2:]
print(num_slice)
for number in numbers:
    if number == 9:
        print("yes")
        break

