a = int(input("请输入菱形每条边星星的个数："))
b = a
c = a
for i in range(1, a + 1):   # 先打印正三角，由空格和*根据规律组成
    print(" " * (b - 1), "*" * (2 * i - 1))
    b -= 1
    if i == a:  # 临界点，当打印到此，开始打印倒三角
        for y in range(1, a):
            print(" " * y, "*" * (2*c-3))
            c -= 1
