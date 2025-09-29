# Nhập hai số a và b
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Nhập phép toán
phep_toan = input("Nhập phép toán (+, -, *, /): ")

# Xử lý và xuất kết quả
if phep_toan == '+':
    print("Kết quả:", a + b)
elif phep_toan == '-':
    print("Kết quả:", a - b)
elif phep_toan == '*':
    print("Kết quả:", a * b)
elif phep_toan == '/':
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Lỗi: không thể chia cho 0!")
else:
    print("Phép toán không hợp lệ!")
