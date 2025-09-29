print("Chương trình tính tổng S = 1 + 2 + ... + n")
n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S += i
print("Giá trị S =", S)
