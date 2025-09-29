import math

def nested_sqrt(a, n):
    """Tính sqrt(a + sqrt(a + ... (n lần sqrt)))"""
    if n <= 0:
        return 0.0
    res = math.sqrt(a)  # n==1
    for _ in range(2, n+1):
        res = math.sqrt(a + res)
    return res

def main():
    try:
        a = float(input("Nhập a (thực): "))
        n = int(input("Nhập số lần lồng n (nguyên dương): "))
    except Exception as e:
        print("Lỗi nhập liệu:", e)
        return
    if n <= 0:
        print("n phải là số nguyên dương.")
        return
    result = nested_sqrt(a, n)
    print(f"Kết quả căn lồng a={a}, n={n}: {result:.6f}")

if __name__ == "__main__":
    main()
