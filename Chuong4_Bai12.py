def oscillate():
    res = []
    # -3,3, -2,2, -1,1
    for i in range(3, 0, -1):
        res.append(-i)
        res.append(i)
    # 0,0
    res.append(0)
    res.append(0)
    # 1,-1,2,-2,3,-3
    for i in range(1, 4):
        res.append(i)
        res.append(-i)
    # finally 4,-4
    res.append(4)
    res.append(-4)
    return res

if __name__ == "__main__":
    arr = oscillate()
    print('\t'.join(str(x) for x in arr))