n = int(input("Nhập chiều cao n: "))
m = int(input("Nhập chiều rộng m: "))

for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()