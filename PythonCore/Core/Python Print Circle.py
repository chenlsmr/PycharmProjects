import math
def num2(args):
    pass
def quan():
    num = int(input('请输入一个整数'))
    if num >26:
        print('无效数字')
        return
    for i in range(num2-1):
        for j in range(num2-1):
         index = max(abs(num-1-i),abs(num-1-j))
        print(chr(97+index),end='')
    print()
