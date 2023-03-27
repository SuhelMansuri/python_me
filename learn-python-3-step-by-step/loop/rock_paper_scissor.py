player1 = input("Player 1 enter value(Rock,Paper,Scissor): ")
player2 = input("Player 2 enter value(Rock,Paper,Scissor): ")

winner = ''
if player1 == player2:
    winner = 'tie'
elif player1 == 'Rock' and player2 == 'Paper':
    winner = 'player2'
    
elif player1 == 'Paper' and player2 == 'Scissor':
    winner = 'player2' 
    
elif player1 == 'Scissor' and player2 == 'Rock':
    winner = 'player2' 
    
elif player2 == 'Rock' and player1 == 'Paper':
    winner = 'player1'
    
elif player2 == 'Paper' and player1 == 'Scissor':
    winner = 'player1' 
    
elif player2 == 'Scissor' and player1 == 'Rock':
    winner = 'player1' 
else:
    print('invalid')
    
print(winner)