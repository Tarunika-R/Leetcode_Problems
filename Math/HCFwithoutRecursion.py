def HCF(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("HCF of", a, "and", b, "is:", HCF(a, b))