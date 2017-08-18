a = input("give a number: ")
a_int = int(a)
b, c = 1, 0
while b <= a_int:
    c = c + b
    b = b + 1
print(a, b, c)
print("Result: ", c / (b - 1))
