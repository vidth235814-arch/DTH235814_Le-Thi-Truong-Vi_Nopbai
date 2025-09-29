def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s

def run_case(case_number):
    global val
    val = 5
    print(f"\\n=== Trường hợp {case_number} ===")
    if case_number == 1:
        print(sum1(5))
        print(sum2())
        print(sum3())
    elif case_number == 2:
        print(sum1(5))
        print(sum3())
        print(sum2())
    elif case_number == 3:
        print(sum2())
        print(sum1(5))
        print(sum3())
    else:
        print("Không có case này.")

if __name__ == "__main__":
    run_case(1)
    run_case(2)
    run_case(3)

    print(""" """)