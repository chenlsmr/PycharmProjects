line = int(input('输入数字'))
row = line
l = 1
while l < line  :
        i = l
        while i - 1 > 0:
            print(' ', end = '')
            i -= 1
        r = row
        while r > 0:
            print('*', end = '')
            r -= 1
        print('')
        l += 1
