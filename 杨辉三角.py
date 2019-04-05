def triangles(n):
    l = [1]
    # 记录第几行，同时知道有多少个元素
    num = 1
    while num <= n:
        # 使用切片是避免两个变量指向同一个列表，从而影响了下面操作
        L = l[:]
        yield L
        num += 1
        if len(l) > 1:
            for d in range(1, num-1):
                l[d] = L[d] + L[d-1]
        l[0] = 1
        l.append(1)


t = triangles(10)
for x in t:
    print(x)