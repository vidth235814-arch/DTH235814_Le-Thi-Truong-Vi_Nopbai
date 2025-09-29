thang = int(input("Nhập số tháng (1-12): "))

if 1 <= thang <= 3:
    print(f"Tháng {thang} thuộc Quý 1")
elif 4 <= thang <= 6:
    print(f"Tháng {thang} thuộc Quý 2")
elif 7 <= thang <= 9:
    print(f"Tháng {thang} thuộc Quý 3")
elif 10 <= thang <= 12:
    print(f"Tháng {thang} thuộc Quý 4")
else:
    print("Tháng không hợp lệ. Vui lòng nhập số từ 1 đến 12.")
