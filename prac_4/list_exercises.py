numbers = []
for number in range(5):
    num = int(input("Number {}: ".format(number + 1)))
    numbers.append(num)

print("The First number is {} :".format(numbers[0]))
print("The Last number is {} :".format(numbers[-1]))
print("The smallest number is {} :".format(min(numbers)))
print("The largest number is {} :".format(max(numbers)))
print("The average of the numbers is {} :".format(sum(numbers)/len(numbers)))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input("Enter username :").lower()
if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")
