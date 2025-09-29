thang = int(input("Nhập vào một tháng (1-12): "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", thang, "có 31 ngày.")
elif thang in [4, 6, 9, 11]:
    print("Tháng", thang, "có 30 ngày.")
elif thang == 2:
    nam = int(input("Nhập năm: "))
    # Kiểm tra năm nhuận
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng 2 năm", nam, "có 29 ngày.")
    else:
        print("Tháng 2 năm", nam, "có 28 ngày.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập từ 1 đến 12.")