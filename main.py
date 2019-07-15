import pygame
import sys
import re
import numpy as np

import Game
import Board
import Block

#使ったブロックのリスト
greenUsedBlocks = []
yellowUsedBlocks = []

# TODO: Playerクラスのプロパティから引っ張ってくる
#パスリスト
turnPassedList = [False, False] # GREEN, YELLOWの順番

# TODO: Gameクラスのプロパティから引っ張ってくる
TILE_NUMBER = 8

#スコア表
scoreTable = {'a':1, 'b':2, 'c':3, 'd':3, 'e':4, 'f':4, 'g':4, 'h':4, 'i':4, 'j':5, 'k':5, 'l':5, 'm':5, 'n':5, 'o':5, 'p':5, 'q':5, 'r':5, 's':5, 't':5, 'u':5}

# TODO: Gameクラスのプロパティから引っ張ってくる
GREEN  = 'green'
YELLOW = 'yellow'
RED    = 'red' # 将来的に実装
BLUE   = 'blue' # 将来的に実装

# TODO: Gameクラスのプロパティから引っ張ってくる
TILE_NUMBER = 8

def skipTurn(board, whoTurn):
    if whoTurn == GREEN:
        nextPlayer = YELLOW
    elif whoTurn == YELLOW:
        nextPlayer = GREEN

    block, whoTurn = selectBlock(board, nextPlayer)
    blockUsableCheck(board, block, whoTurn)

    eval(whoTurn + 'UsedBlocks').pop()

    return block, whoTurn

def scoreCheck():
    if all(turnPassedList):
        #スコアチェック
        greenRemainingBlock = list(set(blockSpells) - set(greenUsedBlocks))
        yellowRemainingBlock = list(set(blockSpells) - set(yellowUsedBlocks))
        greenScore = sum(list(map(lambda alphabet: scoreTable[alphabet], greenRemainingBlock)))
        yellowScore = sum(list(map(lambda alphabet: scoreTable[alphabet], yellowRemainingBlock)))
        #結果発表
        print('ゲームは終了です')
        print('緑色の点数は' + str(greenScore) + '点です')
        print('黄色の点数は' + str(yellowScore) + '点です')

        if greenScore < yellowScore:
            print('勝者は「緑色」です')
        elif greenScore > yellowScore:
            print('勝者は「黄色」です')
        else:
            if len(greenRemainingBlock) < len(yellowRemainingBlock):
                print('勝者は「緑色」です')
            elif len(greenRemainingBlock) > len(yellowRemainingBlock):
                print('勝者は「黄色」です')
            else:
                print('引き分けです')

        turnPassedList[0] = False
        return True
    else:
        return False

blockSpells  = [chr(ord('a') + i) for i in range(21)] # aからuの配列
blockNumbers = [str(n) for n in range(8)] # 0から7の配列

def selectBlock(board, whoTurn):
    print('既に使っているブロック')
    print(sorted(eval(whoTurn + 'UsedBlocks')))
    print('')

    selected_block = input('ブロックを選択してください：')

    while selected_block in eval(whoTurn + 'UsedBlocks') or not selected_block in blockSpells:
        if selected_block in eval(whoTurn + 'UsedBlocks'):
            print('そのブロックは既に使っています\n')
            selected_block = input('ブロックを選択してください：')
        else:
            # Xキーが入力されたらターンスキップ
            if selected_block == 'x':
                if whoTurn == GREEN:
                    turnPassedList[0] = True
                elif whoTurn == YELLOW:
                    turnPassedList[1] = True

                if scoreCheck():
                    sys.exit()
                else:
                    block, whoTurn = skipTurn(board, whoTurn)
                    return block, whoTurn
            else:
                print('入力が間違っています\n')
                selected_block = input('ブロックを選択してください：')

    selectedDirection = input('向きを選択してください：')
    while not selectedDirection in blockNumbers:
        print('入力が間違っています')
        selectedDirection = input('向きを選択してください：')
    selectedDirection = int(selectedDirection)

    block = Block.Block(selected_block, selectedDirection)
    eval(whoTurn + 'UsedBlocks').append(selected_block)

    return block, whoTurn

def blockUsableCheck(board, block, whoTurn):
    while not board.settable_area_exist_check(TILE_NUMBER, block.selected['shape'], eval('board.' + whoTurn + '_board')):
        print('そのブロックを置く場所がありません')
        eval(whoTurn + 'UsedBlocks').pop()
        block, whoTurn = selectBlock(board, whoTurn)

def start(game, board):
    # ゲームスタート処理
    board.check_status(game, GREEN)
    block, whoTurn = selectBlock(board, GREEN)
    blockUsableCheck(board, block, whoTurn)

    while True:
        for event in pygame.event.get():
            # ESCAPEキーが押されたらゲーム終了
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Zキーが押されたらブロック選択キャンセル
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                print('\n選択がキャンセルされました\n')
                eval(whoTurn + 'UsedBlocks').pop()
                block, whoTurn = selectBlock(board, whoTurn)
                blockUsableCheck(board, block, whoTurn)
            # クリックしたらブロックを配置
            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos = int(pygame.mouse.get_pos()[0]/game.TILE_LENGTH) # 右方向に正
                ypos = int(pygame.mouse.get_pos()[1]/game.TILE_LENGTH) # 下方向に正
                if whoTurn == GREEN:
                    if board.settable_check(block.selected['shape'], board.green_board, xpos, ypos):
                        board.change_status(block.selected['shape'], block.selected['influence'], board.green_board, board.yellow_board, xpos, ypos)
                        board.change_image(block.selected['shape'], game.GREEN_IMAGE, game.GREEN_RECT, xpos, ypos, game.surface, game.TILE_LENGTH)
                        board.check_status(game, YELLOW)
                        block, whoTurn = selectBlock(board, YELLOW)
                        blockUsableCheck(board, block, whoTurn)
                    else: print('ここには置けません')

                elif whoTurn == YELLOW:
                    if board.settable_check(block.selected['shape'], board.yellow_board, xpos, ypos):
                        board.change_status(block.selected['shape'], block.selected['influence'], board.yellow_board, board.green_board, xpos, ypos)
                        board.change_image(block.selected['shape'], game.YELLOW_IMAGE, game.YELLOW_RECT, xpos, ypos, game.surface, game.TILE_LENGTH)
                        board.check_status(game,GREEN)
                        block, whoTurn = selectBlock(board, GREEN)
                        blockUsableCheck(board, block, whoTurn)
                    else: print('ここには置けません')

def main():
    game  = Game.Game()
    board = Board.Board(game.TILE_NUMBER)
    start(game, board)

if __name__ == '__main__':
    main()
