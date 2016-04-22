#Formula is AX^2+BX+C
A = int(input("What is the value of A: "))
B = int(input("What is the value of B: "))
C = int(input("What is the value of C: "))
X = int(input("What is the value of X: "))

print("The following quadratic was entered:", A, end="")
print("X",end="")
print("^2","+", B,end="")
print("X","+",C)
equation = A*(X**2)+B*X+C
print("The value of the quadratic is:", equation)
