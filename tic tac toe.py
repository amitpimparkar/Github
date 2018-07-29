def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])



dummy=['#','X','O','X','O','X','O','X','O','X','O']
display_board(dummy)



def place_marker(board):
    #Declaring the variables 
    Player1='Amit'
    Player2='Mohit'
    symbol=['*','#','@','$']
    z=0
    
    if ((board[7] == '#' and board[8] == '#' and board[9] == '#') or # across the top
            (board[4] == '#' and board[5] == '#' and board[6] == '#') or # across the middle
            (board[1] == '#' and board[2] == '#' and board[3] == '#') or # across the bottom
            (board[7] == '#' and board[4] == '#' and board[1] == '#') or # down the middle
            (board[8] == '#' and board[5] == '#' and board[2] == '#') or # down the middle
            (board[9] == '#' and board[6] == '#' and board[3] == '#') or # down the right side
            (board[7] == '#' and board[5] == '#' and board[3] == '#') or # diagonal
            (board[9] == '#' and board[5] == '#' and board[1] == '#')
           ):
        
        print('Game is already over')
        return
    elif  ((board[7] == '*' and board[8] == '*' and board[9] == '*') or # across the top
            (board[4] == '*' and board[5] == '*' and board[6] == '*') or # across the middle
            (board[1] == '*' and board[2] == '*' and board[3] == '*') or # across the bottom
            (board[7] == '*' and board[4] == '*' and board[1] == '*') or # down the middle
            (board[8] == '*' and board[5] == '*' and board[2] == '*') or # down the middle
            (board[9] == '*' and board[6] == '*' and board[3] == '*') or # down the right side
            (board[7] == '*' and board[5] == '*' and board[3] == '*') or # diagonal
            (board[9] == '*' and board[5] == '*' and board[1] == '*')
           ):
        print('Game is already over')
        return
    else:
        pass
   
    print(f'Welcome {Player1} & {Player2} to the game Tic Tac Toe!')
    
    # below command is to increse a space betwen output displayed.
    print('\n'*1)
    
    
    
    print('Current Board Position before your turn below :')
    
    print('\n'*1)
    display_board(dummy)
    
   
    
    pl=input('Input Player Name :').upper()
    print('\n'*1)
    pos=int(input('Player one input your position [0-9] ')) 
    
            
    
    #this is to check if the entered position is already in use or not.if yes, exit the code.
    
    #for pos in [1,2,3,4,5,6,7,8,9]:
    #print(board[pos])
    
    
        
    if (board[pos] =='*' or board[pos] =='#' ):
                  
        print(f'{pl},This position is already in use.Please Enter another number')
        return
                           
    else:
        pass
            
            
        
        
    
        
       
   

   # opt=input('Player one provide your input')
   # print(pl)
   # print(pos)
   # print(opt)
   # print(board)
   # display_board(dummy)
   # print(type(pos))
    #display_board(dummy[pos])
    
   # marker=['X','O']

#this code is to assign the symbol to the player.
    if pl=='AMIT':
        opt='*'
    else:
        opt='#'
        #assigning symbol to the position
    board[pos]=opt     
       # print(board[pos])
        
                
    #for pos in board:
       # board[pos]=mark
       # print(board[pos])
         
#if win_check(board,opt):

# below code checks if player has wining combination.
        
    if ((board[7] == opt and board[8] == opt and board[9] == opt) or # across the top
            (board[4] == opt and board[5] == opt and board[6] == opt) or # across the middle
            (board[1] == opt and board[2] == opt and board[3] == opt) or # across the bottom
            (board[7] == opt and board[4] == opt and board[1] == opt) or # down the middle
            (board[8] == opt and board[5] == opt and board[2] == opt) or # down the middle
            (board[9] == opt and board[6] == opt and board[3] == opt) or # down the right side
            (board[7] == opt and board[5] == opt and board[3] == opt) or # diagonal
            (board[9] == opt and board[5] == opt and board[1] == opt)
           ):
        print(f'Congratulations, {pl} :), Game Over. You Won!!')
        print('\n'*1)
        
        print('Final Board Position below :')
        print('\n'*1)
        display_board(dummy)
    else:
        
        if (board[7] not in ('X','O') and board[6] not in ('X','O') and board[5] not in ('X','O') and
                board[4] not in ('X','O')and board[3] not in ('X','O')and board[2] not in ('X','O') and
                 board[1] not in ('X','O') and board[0] not in ('X','O')
                ):
            print(f'{Player1} & {Player2}, Hard Luck!! :( Game Drawn. Please try again!!')
            print('\n'*1)
            
            print('Final Board Position below :')
            print('\n'*1)
            
            display_board(dummy)
        else:
            print("Go on,Its not over yet!")
            print('\n'*1)
            
            print('Current Board Position below :')
            print('\n'*1)
            display_board(dummy)
            
    
        
        
            