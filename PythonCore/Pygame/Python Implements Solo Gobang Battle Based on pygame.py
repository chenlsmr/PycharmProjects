# 1、引入pygame 和 pygame.locals
import pygame
from pygame.locals import *
import time
import sys

initChessList = []
initRole = 1  # 代表白子下 2：代表当前是黑子下
resultFlag = 0
userFlag = True

class StornPoint():
    def __init__(self, x, y, value=0):
        '''
        :param x: 代表x轴坐标
        :param y: 代表y轴坐标
        :param value: 当前坐标点的棋子：0:没有棋子 1:白子 2:黑子
        '''
        self.x = x
        self.y = y
        self.value = value
        pass


def initChessSquare(x, y):
    '''
    初始化棋盘的坐标
    :param x:
    :param y:
    :return:
    '''
    # 使用二维列表保存了棋盘是的坐标系，和每个落子点的数值
    for i in range(15):  # 每一行的交叉点坐标
        rowList = []
        for j in range(15):  # 每一列的交叉点坐标
            pointX = x + j * 40
            pointY = y + i * 40
            # value  = 0
            sp = StornPoint(pointX, pointY, 0)
            rowList.append(sp)
            pass
        initChessList.append(rowList)
    pass


# 处理事件
def eventHandler():
    global userFlag
    '''
    监听各种事件
    :return:
    '''
    for event in pygame.event.get():

        global initRole
        # 监听点积退出按钮事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pass
        # 监听鼠标点积事件
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  #
            print((x, y))
            i = j = 0
            for temp in initChessList:
                for point in temp:
                    if x >= point.x - 15 and x <= point.x + 15 \
                            and y >= point.y - 15 and y <= point.y + 15:
                        # 当前区域没有棋子，并且是白子下
                        if point.value == 0 and initRole == 1 and userFlag:
                            point.value = 1
                            judgeResult(i, j, 1)
                            initRole = 2  # 切换棋子颜色
                            pass
                        elif point.value == 0 and initRole == 2 and userFlag:
                            point.value = 2
                            judgeResult(i, j, 2)
                            initRole = 1  # 切换棋子颜色
                            pass
                        break
                        pass
                    j += 1
                    pass
                i += 1
                j = 0
            pass
        pass

    pass


# 判断输赢函数
def judgeResult(i, j, value):
    global resultFlag

    flag = False  # 用于判断是否已经判决出输赢
    for x in range(j - 4, j + 5):  # 水平方向有没有出现5连
        if x >= 0 and x + 4 < 15:
            if initChessList[i][x].value == value and \
                    initChessList[i][x + 1].value == value and \
                    initChessList[i][x + 2].value == value and \
                    initChessList[i][x + 3].value == value and \
                    initChessList[i][x + 4].value == value:
                flag = True
                break
                pass
    for x in range(i - 4, i + 5):  # 垂直方向有没有出现5连
        if x >= 0 and x + 4 < 15:
            if initChessList[x][j].value == value and \
                    initChessList[x + 1][j].value == value and \
                    initChessList[x + 2][j].value == value and \
                    initChessList[x + 3][j].value == value and \
                    initChessList[x + 4][j].value == value:
                flag = True
                break
                pass

    # 判断东北方向的对角线是否出现了5连
    for x, y in zip(range(j + 4, j - 5, -1), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y + 4 >= 0 and y < 15:
            if initChessList[y][x].value == value and \
                    initChessList[y - 1][x + 1].value == value and \
                    initChessList[y - 2][x + 2].value == value and \
                    initChessList[y - 3][x + 3].value == value and \
                    initChessList[y - 4][x + 4].value == value:
                flag = True
                break
                pass
            pass
        pass

    # 判断西北方向的对角是否出现了五连
    for x, y in zip(range(j - 4, j + 5), range(i - 4, i + 5)):
        if x >= 0 and x + 4 < 15 and y >= 0 and y + 4 < 15:
            if initChessList[y][x].value == value and \
                    initChessList[y + 1][x + 1].value == value and \
                    initChessList[y + 2][x + 2].value == value and \
                    initChessList[y + 3][x + 3].value == value and \
                    initChessList[y + 4][x + 4].value == value:
                flag = True
                break
                pass
            pass
        pass

    if flag:
        resultFlag = value
        pass
    pass


# 加载素材
def main():
    global resultFlag, initChessList
    initChessSquare(27, 27)  # 初始化棋牌
    pygame.init()  # 初始化游戏环境
    # 创建游戏窗口
    screen = pygame.display.set_mode((620, 620), 0, 0)  # 第一个参数是元组：窗口的长和宽
    # 添加游戏标题
    pygame.display.set_caption("五子棋小游戏")
    # 图片的加载
    background = pygame.image.load('images/bg.png')
    blackStorn = pygame.image.load('images/storn_black.png')
    whiteStorn = pygame.image.load('images/storn_white.png')
    winStornW = pygame.image.load('images/white.png')
    winStornB = pygame.image.load('images/black.png')
    rect = blackStorn.get_rect()

    while True:
        screen.blit(background, (0, 0))
        # 更新棋盘棋子
        for temp in initChessList:
            for point in temp:
                if point.value == 1:
                    screen.blit(whiteStorn, (point.x - 18, point.y - 18))
                    pass
                elif point.value == 2:
                    screen.blit(blackStorn, (point.x - 18, point.y - 18))
                    pass
                pass
            pass
        # 如果已经判决出输赢
        if resultFlag > 0:
            initChessList = []  # 清空棋盘
            initChessSquare(27, 27)  # 重新初始化棋盘
            if resultFlag == 1:
                screen.blit(winStornW, (50, 100))
            else:
                screen.blit(winStornB, (50, 100))
            pass
        pygame.display.update()

        if resultFlag > 0:
            time.sleep(3)
            resultFlag = 0
            pass
        eventHandler()
        pass

    pass


if __name__ == "__main__":
    main()
    pass
