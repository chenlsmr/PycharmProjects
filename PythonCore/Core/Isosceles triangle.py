line = int(input('请输入边长'))
row = 1
while row <= line:
        left = line - row +1
        while left >0:
            print(' ',end ='')
            left -= 1
        star = 2*row - 1
        star = row
        while star > 0:
            print('*',end ='')
            print(' ',end ='')
            star -= 1
        right = line - row +1
        while right >0:
            print(' ',end ='')
            right -= 1
        print('')
        row += 1
