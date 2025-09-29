import math

def log_a_x(a, x):
    # log_a(x) = ln(x) / ln(a)
    return math.log(x) / math.log(a)

def main():
    try:
        a = float(input("Nhập cơ số a (a>0 và a!=1): "))
        x = float(input("Nhập x (x>0): "))
    except Exception as e:
        print("Lỗi nhập liệu:", e)
        return

    if a <= 0 or a == 1 or x <= 0:
        print("Điều kiện không hợp lệ: cần a>0, a!=1, x>0.")
        return

    val = log_a_x(a, x)
    print(f"log_{a}({x}) = {val:.6f}")

if __name__ == "__main__":
    main()