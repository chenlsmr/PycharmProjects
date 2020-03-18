__Author__ = "Chen Lei"

import random

# 导入random模块

checkcode = ''
# 定义一个空字符串，赋给checkcode

for i in range(6):
    # 这里一个for循环，是让i在range（6）中循环，每次循环取出
    # 来的值，赋给i；这里range(6)=(0,1,2,3,4,5)

    current = random.randrange(0, 6)
    # randrange是random中的一个方法，随机从range（0,6）中取一个数出来，赋值给current

    if current < 2:
        # 这里用了一个if语句，如果current小于2，做什么事

        checkcode += chr(random.randint(65, 90))
        # 如果current等于i，randint也是random中的一个方法，chr是python中的内置函数
        # 意思是把数字转换成ascll码表对应的字符，65到90正好对应ascll码中的大写A到大写Z
        # 这句函数意思是chr取出一个字母加上checkcode，重新赋值给checkcode

    elif current >= 2 and current < 4:
        # elif，如果current大于等于2，且小于4做什么。

        checkcode += chr(random.randint(97, 122))
        # 其他类似于上一条，其中97到122正好对应ascll码中的小写a到小写z

    else:
        # if的用法，如果current不符合上面条件，做什么事

        checkcode += str(random.randint(0, 9))
        # str也是python的内置函数，就是把什么转换为字符串，这里是把0到9的任意一个整数
        # 取出来，加上checkcode，重新赋值给checkcode

print(checkcode)
# 最后打印一下checkcode