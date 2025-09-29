def doc_so_hai_chu_so(n):
    
    if not (0 <= n <= 99):
        return "Số không hợp lệ. Vui lòng nhập số từ 0 đến 99."
    
    
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
   
    if n < 10:
        return chu_so[n]
    
    hang_chuc = n // 10
    hang_don_vi = n % 10
    
    ket_qua = ""


    if hang_chuc == 1:
        ket_qua += "mười"
    elif hang_chuc > 1:
        ket_qua += chu_so[hang_chuc] + " mươi"

    
    if hang_don_vi == 0:
        
        if hang_chuc != 0: 
            pass
    elif hang_don_vi == 1:
        
        if hang_chuc == 1:
            ket_qua += " một"
        elif hang_chuc > 1:
            ket_qua += " mốt"
        else: 
            ket_qua += " " + chu_so[hang_don_vi] 
    elif hang_don_vi == 5:
        
        if hang_chuc == 0: 
            ket_qua += chu_so[hang_don_vi]
        elif hang_chuc == 1: 
            ket_qua += " lăm"
        else:
            ket_qua += " lăm"
    elif hang_don_vi > 0:
             ket_qua += chu_so[hang_don_vi] 
    else:
            ket_qua += " " + chu_so[hang_don_vi]
            
    return ket_qua.strip().capitalize()


so_test = [5, 10, 15, 21, 35, 89, 90, 99, 0]
for so in so_test:
    print(f"n={so} => {doc_so_hai_chu_so(so)}")
    
