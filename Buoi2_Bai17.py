n, m = 0, 100
while True:
    try:
        n = int(input("Nhập số: "))
    except ValueError:
        print("Vui lòng nhập số nguyên!")
        continue  # quay lại vòng lặp nhập lại

    if n < 0 or n == m:
        break

print("n =", n)