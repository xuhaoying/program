# tk2048.py

# _map_data 绑定一个 4 x 4 列表,此列表为2048游戏地图，初始值如下:
# _map_data = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

_map_data = [
    [0, 0, 2, 2],
    [4, 0, 4, 2],
    [0, 8, 8, 0],
    [2, 0, 0, 0]
]

def transpose(lst):
    '''矩阵转置'''
    data = []
    for r in range(4):
        row = []
        for c in range(4):
            row.append(lst[c][r])
        data.append(row)
    return data

def get_space_count():
    '''此方法返回地图中0的个数'''
    count = 0
    for line in _map_data:
        count += line.count(0)  # line.count(0) 返回0的个数
    return count

def fill2():
    '''此函数将向_map_data中添加2或者4到空位置'''
    blank_count = get_space_count() # 得到地图上的空白位置
    if blank_count == 0:
        print("地图已满，不添加")
        return
    L = [2, 2, 2, 2, 2, 4]
    import random
    
    pos = random.randrange(0, blank_count)  # 生成位置
    offset = 0  # 记录当前走到的位置
    for row in _map_data:   # row为行row
        for col in range(4):  # col 为列，column
            if 0 == row[col]:
                if offset == pos:
                    # 把2填充到第row行，第col列的位置，返回True
                    row[col] = random.choice(L)
                    return True
                offset += 1

def _left_move_number(line):
    for _ in range(3):
        for i in range(3):
            if line[i] == 0:
                line[i] = line[i+1]
                line[i+1] = 0

def _left_merge_number(line):
    for i in range(3):
        if line[i] == line[i+1]:
            line[i] *= 2
            line[i+1] = 0

def _left_move_aline(line):
    '''
    [2, 0, 2, 8]
    -->  [4, 8, 0, 0] 
    '''
    # 第一步， 让左侧有0的数字左移  【2,2,8,0】
    _left_move_number(line)
    # 第二步，让两个相邻的数合并
    _left_merge_number(line)
    _left_move_number(line)



def left():
    print("左键按下")
    for line in _map_data:
        _left_move_aline(line)

def right():
    print("右键按下")
    for line in _map_data:
        line.reverse()
        _left_move_aline(line)
        line.reverse()

def up():
    print("上键按下")
    # for c in range(4):
    #     line = [0,0,0,0]
    #     for r in range(4):
    #         line[r] = _map_data[r][c]
    #     _left_move_aline(line)
    #     for r in range(4):
    #         _map_data[r][c] = line[r]
    global _map_data
    data = transpose(_map_data)
    for line in data:
        _left_move_aline(line)
    _map_data = transpose(data)

def down():
    print("下键按下")
    global _map_data
    data = transpose(_map_data)
    for line in data:
        line.reverse()
        _left_move_aline(line)
        line.reverse()
    _map_data = transpose(data)



def main():
    import tkinter
    root = tkinter.Tk() 


    game_bg_color = "#bbada0"  # 设置背景颜色

    # 设置游戏中每个数据对应色块的颜色
    mapcolor = {
        0: ("#cdc1b4", "#776e65"),
        2: ("#eee4da", "#776e65"),
        4: ("#ede0c8", "#f9f6f2"),
        8: ("#f2b179", "#f9f6f2"),
        16: ("#f59563", "#f9f6f2"),
        32: ("#f67c5f", "#f9f6f2"),
        64: ("#f65e3b", "#f9f6f2"),
        128: ("#edcf72", "#f9f6f2"),
        256: ("#edcc61", "#f9f6f2"),
        512: ("#e4c02a", "#f9f6f2"),
        1024: ("#e2ba13", "#f9f6f2"),
        2048: ("#ecc400", "#f9f6f2"),
        4096: ("#ae84a8", "#f9f6f2"),
        8192: ("#b06ca8", "#f9f6f2"),
        # ----其它颜色都与8192相同---------
        2**14: ("#b06ca8", "#f9f6f2"),
        2**15: ("#b06ca8", "#f9f6f2"),
        2**16: ("#b06ca8", "#f9f6f2"),
        2**17: ("#b06ca8", "#f9f6f2"),
        2**18: ("#b06ca8", "#f9f6f2"),
        2**19: ("#b06ca8", "#f9f6f2"),
        2**20: ("#b06ca8", "#f9f6f2"),
    }


    def on_key_down(event):
        '''键盘按下事件处理函数'''
        if event.keysym in ('Left', 'a'):
            left()
        elif event.keysym in ('Right', 'd'):
            right()
        elif event.keysym in ('Up', 'w'):
            up()
        elif event.keysym in ('Down', 's'):
            down()
        update_ui() # 更新界面
        fill2()


    root.bind("<KeyPress>", on_key_down)

    def update_ui():
        '''根据地图数据，重新设置UI的label中的数字和颜色等信息'''
        for r in range(4):
            for c in range(4):
                number = _map_data[r][c]  # 获取数字
                label = map_labels[r][c]  # 获取数字对应的label
                label['text'] = str(number) if number > 0 else ''
                label['bg'] = mapcolor[number][0]
                label['foreground'] = mapcolor[number][1]
        # label_score['text'] = str(get_score())  # 重设置分数


    # 保存所有的显示数字的label, 后续修改时使用
    map_labels = []
    # 创建2048地图表格
    for r in range(4):
        row = []  # 创建一个新的列表，用来绑定一行label
        for c in range(4):
            txt = str(_map_data[r][c])
            if txt == '0':
                txt = ''
            label = tkinter.Label(
                    root, text=txt,
                    font=("youyuan", 30, "bold"), width=4, height=2, bg="#cdc1b4"
                    )
            label.grid(row=r, column=c, padx=5, pady=5)
            row.append(label)
        map_labels.append(row)

    root.mainloop()

main()