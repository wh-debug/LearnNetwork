magicans = ['alice', 'david', 'carolina']
for magican in magicans:
    print(magican.title())

print('\n')
for magican in magicans:
    print(magican.upper())

print('\n')
for magican in magicans:
    print(f"{magican.title()}, that was a great trick!")

# 创建数字列表
numbers = list(range(1, 6))
print(numbers)

squares = [value ** 3 for value in range(1, 11)]
print(squares)

# 可以被3整除的倍数
tempnumber = list(range(3, 30, 3))
print(tempnumber)

# 使用切片 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:8])