from datetime import datetime, timedelta

# Nhập ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    # Tạo đối tượng ngày từ dữ liệu nhập
    ngay_hien_tai = datetime(nam, thang, ngay)

    # Cộng thêm 1 ngày
    ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)

    # In ra kết quả theo định dạng dd/mm/yyyy
    print("Ngày kế tiếp là: {}/{}/{}".format(
        ngay_ke_tiep.day,
        ngay_ke_tiep.month,
        ngay_ke_tiep.year
    ))

except ValueError:
    print("Ngày không hợp lệ! Vui lòng nhập lại.")
