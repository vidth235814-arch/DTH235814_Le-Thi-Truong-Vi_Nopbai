import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def square(n=6):
    for i in range(n):
        print('* ' * n)

def right_triangle(n=6):
    for i in range(1, n+1):
        print('* ' * i)

def isosceles_triangle(n=6):
    for i in range(1, n+1):
        print(' '*(n-i) + '* ' * i)

def diamond(n=5):  # n is half height
    for i in range(n):
        print(' '*(n-i-1) + '* '*(i+1))
    for i in range(n-1):
        print(' '*(i+1) + '* '*(n-i-1))

def main():
    shapes = [
        ("Hình vuông", square),
        ("Tam giác vuông (bên trái)", right_triangle),
        ("Tam giác cân", isosceles_triangle),
        ("Hình thoi", diamond)
    ]
    for title, func in shapes:
        clear()
        print(title + "\n")
        func()
        print("\n(Chuyển sang hình tiếp theo sau 5 giây...)")
        time.sleep(5)
    print("Đã hiển thị xong 4 hình.")

if __name__ == "__main__":
    main()