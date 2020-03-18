n = int(input("输入要打印的菱形的每个边的元素个数："))
list_a = [i for i in range(n)]  # 生成前n行的行数列表，例如[0,1,2,3,4]
list_b = list_a[0:len(list_a) - 1:]  # 生成剩余行数列表并反转，例如[0,1,2,3]
list_c = list_b[::-1]    # 对剩余行数列表并反转便于打印操作
list_d = list_a + list_c  # 将两个列表合并
print(list_d)

b = [' ' * (n - i) + '*' * (2 * i + 1) for i in list_d] # 根据规律，打印空格" "和"*"

for line in b:
    print(line)
