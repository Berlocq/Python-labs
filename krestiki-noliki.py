import os

board = [[' ',' ',' '],
       [' ',' ',' '],
       [' ',' ',' ']]

print(''+board[0][0]+'|'+board[0][1]+'|'+board[0][2])
print('-----')
print(''+board[1][0]+'|'+board[1][1]+'|'+board[1][2])
print('-----')
print(''+board[2][0]+'|'+board[2][1]+'|'+board[2][2])

choise = input('Выберите символ х или о : ')
if choise == 'x':
    icount = 1
elif choise == 'o':
    icount = 2
else:
    print('Символ не выбран')
    
while icount <= 9:
    
    if icount%2 == 0:
        player_id = 2
        player_move = 'o'
    else:
        player_id = 1
        player_move = 'x'
    
    while True:
        while True:
            column = int(input('Пользователь ' + str(player_id) + ' - введите номер столбца от 1 до 3: '))
            row = int(input('Пользователь ' + str(player_id) + ' - введите номер строки от 1 до 3: '))
            #os.system('cls' if os.name == 'nt' else 'clear')
            
            
            if column < 1 or column > 3 or row < 1 or row > 3:
                print('Пожалуйста введите номер от 1 до 3')
                #print(board)
                
            else:
                break
        
        if board[row-1][column-1] == ' ':
            board[row-1][column-1] = player_move
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print('Ячейка занята, выберите другую ячейку :')
            #print(board)
            

    print(''+board[0][0]+'|'+board[0][1]+'|'+board[0][2])
    print('-----')
    print(''+board[1][0]+'|'+board[1][1]+'|'+board[1][2])
    print('-----')
    print(''+board[2][0]+'|'+board[2][1]+'|'+board[2][2])
        
    for ii in range (0,3):
        if board[ii][:]==[player_move, player_move, player_move] or \
           board[0][ii]==board[1][ii]==board[2][ii]==player_move or \
           board[0][0]==board[1][1]==board[2][2]==player_move or \
           board[0][2]==board[1][1]==board[2][0]==player_move:
            #os.system('cls' if os.name == 'nt' else 'clear')
            print('Пользователь ' + str(player_id) + ' выиграл!')
            icount = 100
            break
    
    icount += 1

if icount==10:
    print("Это ничья!")
    


