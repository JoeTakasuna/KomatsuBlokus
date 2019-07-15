import numpy as np

class Block():
    def __init__(self):
        self.call_block('j')
        self.rotate_block(2)
        print(self.selected['shape'])

    def call_block(self, selected_shape_index):
        # selected_shapeに従ってDBから持ってくる
        self.selected = block_table['j']

    def rotate_block(self, selected_direction_index):
        if selected_direction_index == 0: # 初期向き
            self.selected['shape']     = self.selected['shape']
            self.selected['influence'] = self.selected['influence']
        elif selected_direction_index == 1: # 裏向き
            self.selected['shape']     = np.rot90(self.selected['shape'].T, -1)
            self.selected['influence'] = np.rot90(self.selected['influence'].T, -1)
        elif selected_direction_index == 2: # 初期向きから90°時計回りに
            self.selected['shape']     = np.rot90(self.selected['shape'], -1)
            self.selected['influence'] = np.rot90(self.selected['influence'], -1)
        elif selected_direction_index == 3: # 裏向きから90°反時計回りに
            self.selected['shape']     = self.selected['shape'].T
            self.selected['influence'] = self.selected['influence'].T
        elif selected_direction_index == 4: # 初期向きから180°時計回りに
            self.selected['shape']     = np.rot90(self.selected['shape'], -2)
            self.selected['influence'] = np.rot90(self.selected['influence'], -2)
        elif selected_direction_index == 5: # 裏向きから180°反時計回りに
            self.selected['shape']     = np.rot90(self.selected['shape'].T, -3)
            self.selected['influence'] = np.rot90(self.selected['influence'].T, -3)
        elif selected_direction_index == 6: # 初期向きから270°時計回りに
            self.selected['shape']     = np.rot90(self.selected['shape'], -3)
            self.selected['influence'] = np.rot90(self.selected['influence'], -3)
        elif selected_direction_index == 7: # 裏向きから270°反時計回りに
            self.selected['shape']     = np.rot90(self.selected['shape'].T, -2)
            self.selected['influence'] = np.rot90(self.selected['influence'].T, -2)

block_table = {
    'a':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,0,2,1,2,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 1
    },
    'b':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,2,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 2
    },
    'c':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,2,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 3
    },
    'd':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,2,0],
        [0,0,1,1,1,1,0],
        [0,0,2,1,1,2,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 3
    },
    'e':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,2,1,2,0,0]
        ]),
        'score': 4
    },
    'f':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,2,1,1,1,0,0],
        [0,1,1,1,1,0,0],
        [0,2,1,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 4
    },
    'g':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,2,0],
        [0,0,1,1,1,1,0],
        [0,0,1,1,1,2,0],
        [0,0,2,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 4
    },
    'h':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,1,0],
        [0,0,1,1,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,2,1,1,2,0],
        [0,0,1,1,1,1,0],
        [0,0,1,1,1,1,0],
        [0,0,2,1,1,2,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 4
    },
    'i':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,2,1,1,2,0,0],
        [0,1,1,1,1,2,0],
        [0,2,1,1,1,1,0],
        [0,0,2,1,1,2,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 4
    },
    'j':{
        'shape': np.asarray([
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
        ]),
        'influence': np.asarray([
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,2,1,2,0,0]
        ]),
        'score': 5
    },
    'k':{
        'shape': np.asarray([
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,2,1,1,1,0,0],
        [0,1,1,1,1,0,0],
        [0,2,1,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    'l':{
        'shape': np.asarray([
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,2,1,1,1,0,0],
        [0,1,1,1,1,0,0],
        [0,1,1,1,2,0,0],
        [0,2,1,2,0,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    'm':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,2,1,1,1,0,0],
        [0,1,1,1,1,0,0],
        [0,1,1,1,1,0,0],
        [0,2,1,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    'n':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,1,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,2,1,1,2,0,0],
        [0,1,1,1,1,0,0],
        [0,2,1,1,1,0,0],
        [0,1,1,1,1,0,0],
        [0,2,1,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    'o':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,2,0],
        [0,0,1,1,1,1,0],
        [0,0,1,1,1,2,0],
        [0,0,1,1,1,0,0],
        [0,0,2,1,2,0,0]
        ]),
        'score': 5
    },
    'p':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,2,1,1,1,2,0],
        [0,1,1,1,1,1,0],
        [0,2,1,1,1,2,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    'q':{
        'shape': np.asarray([
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,2,1,2,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,1,2],
        [0,0,1,1,1,1,1],
        [0,0,2,1,1,1,2],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    'r':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,1,1,0,0],
        [0,0,1,1,0],
        [0,0,0,1,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,2,1,1,2,0,0],
        [0,1,1,1,1,2,0],
        [0,2,1,1,1,1,0],
        [0,0,2,1,1,1,0],
        [0,0,0,2,1,2,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    's':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,2,1,2,0,0,0],
        [0,1,1,1,1,2,0],
        [0,1,1,1,1,1,0],
        [0,2,1,1,1,1,0],
        [0,0,0,2,1,2,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    't':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,2,1,2,0,0,0],
        [0,1,1,1,1,2,0],
        [0,1,1,1,1,1,0],
        [0,2,1,1,1,2,0],
        [0,0,2,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    },
    'u':{
        'shape': np.asarray([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
        ]),
        'influence': np.asarray([
        [0,0,0,0,0,0,0],
        [0,0,2,1,2,0,0],
        [0,2,1,1,1,2,0],
        [0,1,1,1,1,1,0],
        [0,2,1,1,1,2,0],
        [0,0,2,1,2,0,0],
        [0,0,0,0,0,0,0]
        ]),
        'score': 5
    }
}
