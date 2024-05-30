first = int(input('Введите первое число:')) # 123, 42
second = int(input('Введите второе число:')) # 456, 69
third = int(input('Введите третье число:')) # 789, 42

if first == second == third:
    print(3)

elif first == second or first == third or second == third:
    print(2)

else:
    print(0)