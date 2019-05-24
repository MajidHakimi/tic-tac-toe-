player_nud = ['O', 'X']
dic_table = {}

cell_1 = [False,'1']
cell_2 = [False,'2']
cell_3 = [False,'3']
cell_4 = [False,'4']
cell_5 = [False,'5']
cell_6 = [False,'6']
cell_7 = [False,'7']
cell_8 = [False,'8']
cell_9 = [False,'9']

def tic_Toc_To():


    def show_table():
        # show and refresh table when player put new nud
        print('|---|---|---|')
        print('| ' + cell_1[1] + ' ' + '| ' + cell_2[1] + ' ' + '| ' + cell_3[1] + '' + ' | ')
        print('|---|---|---|')
        print('| ' + cell_4[1] + ' ' + '| ' + cell_5[1] + ' ' + '| ' + cell_6[1] + '' + ' | ')
        print('|---|---|---|')
        print('| ' + cell_7[1] + ' ' + '| ' + cell_8[1] + ' ' + '| ' + cell_9[1] + '' + ' | ')
        print('|---|---|---|')
    def game_play_rule():
        if (cell_1[1] == 'O' and cell_2[1] == 'O' and cell_3[1] == 'O'):
            return 'O'
        elif (cell_4[1] == 'O' and cell_5[1] == 'O' and cell_6[1] == 'O'):
            return 'O'
        elif (cell_7[1] == 'O' and cell_8[1] == 'O' and cell_9[1] == 'O'):
            return 'O'
        elif (cell_1[1] == 'O' and cell_4[1] == 'O' and cell_7[1] == 'O'):
            return 'O'
        elif (cell_2[1] == 'O' and cell_5[1] == 'O' and cell_8[1] == 'O'):
            return 'O'
        elif (cell_3[1] == 'O' and cell_6[1] == 'O' and cell_9[1] == 'O'):
            return 'O'
        elif (cell_1[1] == 'O' and cell_5[1] == 'O' and cell_9[1] == 'O'):
            return 'O'
        elif (cell_3[1] == 'O' and cell_5[1] == 'O' and cell_7[1] == 'O'):
            return 'O'
        elif (cell_1[1] == 'X' and cell_2[1] == 'X' and cell_3[1] == 'X'):
            return 'X'
        elif (cell_4[1] == 'X' and cell_5[1] == 'X' and cell_6[1] == 'X'):
            return 'X'
        elif (cell_7[1] == 'X' and cell_8[1] == 'X' and cell_9[1] == 'X'):
            return 'X'
        elif (cell_1[1] == 'X' and cell_4[1] == 'X' and cell_7[1] == 'X'):
            return 'X'
        elif (cell_2[1] == 'X' and cell_5[1] == 'X' and cell_8[1] == 'X'):
            return 'X'
        elif (cell_3[1] == 'X' and cell_6[1] == 'X' and cell_9[1] == 'X'):
            return 'X'
        elif (cell_1[1] == 'X' and cell_5[1] == 'X' and cell_9[1] == 'X'):
            return 'X'
        elif (cell_3[1] == 'X' and cell_5[1] == 'X' and cell_7[1] == 'X'):
            return 'X'
        else:
            return 'none'
    def player_input():

        o_flag = False
        x_flag = False

        global cell_1
        global cell_2
        global cell_3
        global cell_4
        global cell_5
        global cell_6
        global cell_7
        global cell_8
        global cell_9

        # Realize who player start the game

        while True:
            player_input = input("Who start O or X : ").upper()
            if (player_input == 'X'):
                x_flag = True
                o_flag = False
                break
            elif(player_input == 'O'):
                x_flag = False
                o_flag = True
                break
            else:
                pass

        for i in range (1,10):
            if(o_flag ):
                num_cell = input('Player O Enter number of cell :')
                print("this is O area ")
                if(num_cell=="1"):
                    if(cell_1[0]):
                        pass
                    else:
                        cell_1[1] = 'O'
                        print(cell_1[1])
                        cell_1[0] = True
                        print(cell_1[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                elif(num_cell=='2'):
                    if (cell_2[0]):
                        pass
                    else:
                        cell_2[1] = 'O'
                        print(cell_2[1])
                        cell_2[0] = True
                        print(cell_2[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                elif (num_cell == '3'):
                    if (cell_3[0]):
                        pass
                    else:
                        cell_3[1] = 'O'
                        print(cell_1[1])
                        cell_3[0] = True
                        print(cell_3[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                elif (num_cell == '4'):

                    if (cell_4[0]):
                        pass
                    else:
                        cell_4[1] = 'O'
                        print(cell_1[1])
                        cell_4[0] = True
                        print(cell_4[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                elif (num_cell == '5'):

                    if (cell_5[0]):
                        pass
                    else:
                        cell_5[1] = 'O'
                        print(cell_1[1])
                        cell_5[0] = True
                        print(cell_5[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                elif (num_cell == '6'):

                    if (cell_6[0]):
                        pass
                    else:
                        cell_6[1] = 'O'
                        print(cell_1[1])
                        cell_6[0] = True
                        print(cell_6[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                elif (num_cell == '7'):

                    if (cell_7[0]):
                        pass
                    else:
                        cell_7[1] = 'O'
                        print(cell_1[1])
                        cell_7[0] = True
                        print(cell_7[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                elif (num_cell == '8'):

                    if (cell_8[0]):
                        pass
                    else:
                        cell_8[1] = 'O'
                        print(cell_1[1])
                        cell_8[0] = True
                        print(cell_8[0])
                        show_table()
                        o_flag = False
                        x_flag = True
                else:
                    if (cell_9[0]):
                        pass
                    else:
                        cell_9[1] = 'O'
                        cell_9[0] = True
                        show_table()
                        o_flag = False
                        x_flag = True
            elif(x_flag):
                num_cell = input('Player X Enter number of cell :')
                print('this is X area')
                if (num_cell == "1"):
                    if (cell_1[0]):
                        pass
                    else:
                        cell_1[1] = 'X'
                        print(cell_1[1])
                        cell_1[0] = True
                        print(cell_1[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                elif (num_cell == '2'):
                    if (cell_2[0]):
                        pass
                    else:
                        cell_2[1] = 'X'
                        print(cell_2[1])
                        cell_2[0] = True
                        print(cell_2[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                elif (num_cell == '3'):
                    if (cell_3[0]):
                        pass
                    else:
                        cell_3[1] = 'X'
                        print(cell_1[1])
                        cell_3[0] = True
                        print(cell_3[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                elif (num_cell == '4'):

                    if (cell_4[0]):
                        pass
                    else:
                        cell_4[1] = 'X'
                        print(cell_1[1])
                        cell_4[0] = True
                        print(cell_4[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                elif (num_cell == '5'):

                    if (cell_5[0]):
                        pass
                    else:
                        cell_5[1] = 'X'
                        print(cell_1[1])
                        cell_5[0] = True
                        print(cell_5[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                elif (num_cell == '6'):

                    if (cell_6[0]):
                        pass
                    else:
                        cell_6[1] = 'X'
                        print(cell_1[1])
                        cell_6[0] = True
                        print(cell_6[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                elif (num_cell == '7'):

                    if (cell_7[0]):
                        pass
                    else:
                        cell_7[1] = 'X'
                        print(cell_1[1])
                        cell_7[0] = True
                        print(cell_7[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                elif (num_cell == '8'):

                    if (cell_8[0]):
                        pass
                    else:
                        cell_8[1] = 'X'
                        print(cell_1[1])
                        cell_8[0] = True
                        print(cell_8[0])
                        show_table()
                        o_flag = True
                        x_flag = False
                else:
                    if (cell_9[0]):
                        pass
                    else:
                        cell_9[1] = 'X'
                        cell_9[0] = True
                        show_table()
                        o_flag = True
                        x_flag = False
            else:
                pass
            if(game_play_rule()== "X"):
                print("X player is WIN!")
                break
            elif(game_play_rule() == "O"):
                print("O plater is WIN!")
                break
            else:
                pass



    player_input()



tic_Toc_To()


