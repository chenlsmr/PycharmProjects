# == , != , <= , >= , < , >  逻辑运算符
print(1 == 1)  # 真
print(1 == 2)  # 假
print(1 != 2)  # 真
print(1 != 1)  # 假
print(1 <= 2)  # 真
print(1 >= 2)  # 假
print(1 < 2)  # 真
print(1 > 2)  # 假

# 思考题
print(1 == "1")  # 真 还是  假

#  与或非
print(1 == 1 and 2 == 2)  # 真 and  真  =  真
print(1 == 1 and 1 == 2)  # 真 and 假 = 假
print(2 == 1 and 1 == 2)  # 假 and 假 = 假


print(1 == 1 or 2 == 2)  # 真 or  真 = 真
print(1 == 1 or 1 == 2)  # 真 or  假 = 真
print(2 == 1 or 1 == 2)  # 假 or  假 = 假

print(not 1 == 1)  # not 真 = 假
print(not 1 == 2)  # not 假 = 真