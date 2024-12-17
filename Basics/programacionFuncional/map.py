numbers = [1, 2, 3, 4, 5]
result1 = list(map(lambda x: x + x, numbers))
result2 = list(map(lambda x: x * 3, numbers))
result3 = list(map(lambda x: x / 0.5, numbers))

print(result1)
print(result2)
print(result3)

def suma(num1, num2):
    return num1 + num2

print(suma(4, 6))
