n = int(input("Nhập chiều cao n: "))

# Tam giác đỉnh quay xuống (lật ngược)
for i in range(n, 0, -1):
  
    # in dấu * cho phần tam giác bên phải
    print("* " * i)

# Tam giác đỉnh quay xuống thứ hai (nối tiếp dưới)
for i in range(n, 0, -1):
    print("* " * i)

    n = int(input("Nhập chiều cao n: "))

