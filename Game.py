import pygame
import sys
import re
import numpy as np

import Player

# TODO: Playerクラスのプロパティから引っ張ってくる
turn_passed_list = [False, False] # GREEN, YELLOWの順番

class Game():
    TILE_NUMBER = 8
    TILE_LENGTH = 50

    GREEN  = 'green'
    YELLOW = 'yellow'
    RED    = 'red' # 将来的に実装
    BLUE   = 'blue' # 将来的に実装

    # タイルの設置はボード外エラー回避の為2マス広く
    SCREEN_WIDTH  = TILE_LENGTH * (TILE_NUMBER + 2)
    SCREEN_HEIGHT = TILE_LENGTH * (TILE_NUMBER + 2)
    TILE_LIMIT    = TILE_LENGTH * TILE_NUMBER

    # ビューの設定
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface.fill((0,0,0)) # 黒で塗りつぶし

    TILE_IMAGE   = pygame.image.load('image/tile.bmp').convert()
    GREEN_IMAGE  = pygame.image.load('image/green.bmp').convert()
    YELLOW_IMAGE = pygame.image.load('image/yellow.bmp').convert()

    TILE_RECT   = TILE_IMAGE.get_rect() # 画像と同じサイズの長方形座標を取得
    GREEN_RECT  = GREEN_IMAGE.get_rect()
    YELLOW_RECT = YELLOW_IMAGE.get_rect()

    # タイルで画面を埋める
    for i in range(0, TILE_LIMIT, TILE_LENGTH):
        for j in range(0, TILE_LIMIT, TILE_LENGTH):
            # 枠の分はスキップ
            surface.blit(TILE_IMAGE, TILE_RECT.move((i + TILE_LENGTH), (j + TILE_LENGTH)))

    # pygameの初期設定
    pygame.init()
    pygame.display.set_caption('Komatsu Blokus')
    pygame.mouse.set_visible(True) #マウスポインターの表示をオン

    def __init__(self, color):
        self.who_turn = color

    def start(self, game, board):
        player1 = Player.Player(self.GREEN)
        player2 = Player.Player(self.YELLOW)
        # ゲームスタート処理
        board.check_status(game, turn_passed_list)
        block = player1.select_block(board)
        block = player1.block_usable_check(board, block)

        while True:
            for event in pygame.event.get():
                # ESCAPEキーが押されたらゲーム終了
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # Zキーが押されたらブロック選択キャンセル
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    if game.who_turn == self.GREEN:
                        block = player1.cancel_selected(board, block)
                    elif game.who_turn == self.YELLOW:
                        block = player2.cancel_selected(board, block)
                # クリックしたらブロックを配置
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    xpos = int(pygame.mouse.get_pos()[0]/game.TILE_LENGTH) # 右方向に正
                    ypos = int(pygame.mouse.get_pos()[1]/game.TILE_LENGTH) # 下方向に正
                    if game.who_turn == self.GREEN:
                        if board.settable_check(block.selected['shape'], board.green_board, xpos, ypos):
                            board.change_status(block.selected['shape'], block.selected['influence'], board.green_board, board.yellow_board, xpos, ypos)
                            board.change_image(block.selected['shape'], game.GREEN_IMAGE, game.GREEN_RECT, xpos, ypos, game.surface, game.TILE_LENGTH)
                            game.who_turn = self.YELLOW
                            board.check_status(game, turn_passed_list)
                            block = player2.select_block(board)
                            block = player2.block_usable_check(board, block)
                        else: print('ここには置けません')

                    elif game.who_turn == self.YELLOW:
                        if board.settable_check(block.selected['shape'], board.yellow_board, xpos, ypos):
                            board.change_status(block.selected['shape'], block.selected['influence'], board.yellow_board, board.green_board, xpos, ypos)
                            board.change_image(block.selected['shape'], game.YELLOW_IMAGE, game.YELLOW_RECT, xpos, ypos, game.surface, game.TILE_LENGTH)
                            game.who_turn = self.GREEN
                            board.check_status(game, turn_passed_list)
                            block = player1.select_block(board)
                            block = player1.block_usable_check(board, block)
                        else: print('ここには置けません')
