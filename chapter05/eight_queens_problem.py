# coding=utf-8
"""
@desc:
国际象棋中的皇后比中国象棋里的大车还厉害，皇后能横向，纵向和斜向移动，在这三条线上的其他棋子都可以被吃掉。
所谓八皇后问题就是：将八位皇后放在一张8x8的棋盘上，使得每位皇后都无法吃掉别的皇后，（即任意两个皇后都不在同一条横线，
竖线和斜线上），问一共有多少种摆法。此问题是在1848年由棋手马克思·贝瑟尔提出的，后面陆续有包括高斯等大数学家们给出
自己的思考和解法，所以此问题不只是有年头了，简直比82年的拉菲还有年头，我们今天不妨尝尝这老酒。
@author: huijz
@version 0.1
@date 2020-08-31
@email huijz8117@gmail.com
"""
BOARD_SIZE = 8  # 棋盘大小 8*8=64


def under_attack(col, queens):
    left = right = col
    for i, c in reversed(queens):
        # 左右有冲突的位置的列号
        left, right = left - 1, right + 1
        if c in (left, col, right):
            return True
        return False


def solve(n):
    if n == 0:
        return [[]]
    smaller_solutions = solve(n - 1)
    return [solution + [(n, i + 1)]
            for i in xrange(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(i + 1, solution)]


for answer in solve(BOARD_SIZE):
    print answer
