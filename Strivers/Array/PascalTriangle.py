# # Finding the value for the given row and column in Pascal's Triangle
# def nCr(n, r):
#     res = 1

#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)
#     return res

# def pascalTriangle(r, c):
#     element = nCr(r - 1, c - 1)
#     return element

# if __name__ == "__main__":
#     r = 5   
#     c = 3
#     element = pascalTriangle(r, c)
#     print(f"The value at row {r} and column {c} in Pascal's Triangle is: {element}")


# Printing the n-th row of the Pascal's triangle
def PasclTriangle(n):
    ans = 1
    print(ans, end=' ')
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i 
        print(ans, end=' ')
    return ans

if __name__ == "__main__":
    n = 5  # Row number
    print(f"The {n}-th row of Pascal's Triangle is: ", end='')
    PasclTriangle(n)
    print()  # For a new line after printing the row


