# 流程控制 之 if else 判断
if 1 == 1:  # 如果 if 跟随的条件 为 真 那么执行属于 if 中的语句
    print("真的")

if 1 == 2:  # 如果 if 跟随的条件为 假 那么不执行属于if 的语句,然后寻找 else
    print("假的")
else:  # 寻找到 else 之后 执行属于else中的语句
    print("1==2 假的")

# 高端判断 之 否则如果:
if 1 == 2:
    print("1==2")

elif 1 == 1:  # 如果 if 条件不成立,会进行第二次判断 elif ,如果elif条件成立,则执行属于elif中的语句,如不成立则else
    print("1==1")

else:
    print("全是骗人的")