import math

def distance(ax, ay, bx, by):
    return math.sqrt((bx - ax)**2 + (by - ay)**2)

def main():
    print("Nhập tọa độ A (xA yA) và B (xB yB), cách nhau bởi dấu cách.")
    try:
        ax, ay = map(float, input("A(xA yA): ").split())
        bx, by = map(float, input("B(xB yB): ").split())
    except Exception as e:
        print("Lỗi nhập liệu:", e)
        return
    d = distance(ax, ay, bx, by)
    print(f"Độ dài đoạn AB = {d:.6f}")

if __name__ == "__main__":
    main()

