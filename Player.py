import Block
import random

class Player():
    block_shape_index_list     = [chr(ord('a') + i) for i in range(21)] # aからuの配列
    block_direction_index_list = [str(n) for n in range(8)] # 0から7の配列

    def __init__(self, enum, boolean):
        self.color = enum
        self.computer = boolean
        self.passed = False
        self.used_blocks = []
        self.usable_blocks = []
        self.use_block = []
        self.selected_shape_index = ''
        self.selected_direction_index = ''
        self.score = 0

    def pass_my_turn(self, game):
        print('\n＝＝＝＝＝＝＝＝＝＝' + game.current_player.color.name + '\'s Turn＝＝＝＝＝＝＝＝＝＝')
        print('置けるブロックが存在しないためパスとなります')
        game.change_turn()

    def start_my_turn(self, game, board):
        board.check_status(game)
        self.select_block(board)
        block = Block.Block(self.selected_shape_index, self.selected_direction_index, True)

        if not self.computer:
            while not any((block[0] == self.selected_shape_index and block[1] == self.selected_direction_index)
                          for block in self.usable_blocks):
                print('そのブロックを置く場所がありません\n')
                self.select_block(board)
                block = Block.Block(self.selected_shape_index, self.selected_direction_index, True)

        return block

    def select_block(self, board):
        if self.computer:
            self.use_block = random.choice(self.usable_blocks)
            self.selected_shape_index     = self.use_block[0]
            self.selected_direction_index = self.use_block[1]
        else:
            print('手持ちのブロックリスト')
            print([i for i in self.block_shape_index_list if i not in self.used_blocks])
            self.selected_shape_index = input('\nブロックを選択してください：')
            while True:
                if self.check_input(board):
                    break

            self.selected_direction_index = input('向きを選択してください：')
            while not self.selected_direction_index in self.block_direction_index_list:
                print('入力が間違っています')
                self.selected_direction_index = input('向きを選択してください：')
            self.selected_direction_index = int(self.selected_direction_index)

    def check_input(self, board):
        if self.selected_shape_index in self.used_blocks:
            print('そのブロックは既に使っています\n')
            self.selected_shape_index = input('ブロックを選択してください：')
            return False
        elif not self.selected_shape_index in self.block_shape_index_list:
            print('入力が間違っています\n')
            self.selected_shape_index = input('ブロックを選択してください：')
            return False
        else:
            return True

    def cancel_selected(self, game, board):
        print('\n選択がキャンセルされました\n')
        block = self.start_my_turn(game, board)
        return block
