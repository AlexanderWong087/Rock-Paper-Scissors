import random 

def winner(player1,player2): 
    winner='nil' 
    if player1=='rock' and player2=='scissors': 
        winner='You' 
    elif player1=='paper' and player2=='rock': 
        winner='You' 
    elif player1=='scissors' and player2=='paper': 
        winner='You' 
    elif player2=='rock' and player1=='scissors': 
        winner='Computer' 
    elif player2=='paper' and player1=='rock': 
        winner='Computer' 
    elif player2=='scissors' and player1=='paper': 
        winner='Computer' 
    else: 
        print('Tie') 
        winner='Nobody' 
    return winner

def request_input(): 
    decision=input('Choose rock, paper, or scissors: ').lower() 
    if decision not in ['rock','paper','scissors']: 
        print("That's not a valid choice. This round is a tie.") 
        return 'Nobody' 
    computer=random.choice(['rock','paper','scissors']) 
    print('Computer chose '+computer) 
    return(winner(decision,computer)) 

play=True 
print('Welcome to rock paper scissors!') 
outcome=request_input() 
if outcome=='Tie': 
    print('Its a tie!') 
else:
    print(outcome+' won!') 
play_again_request=input('Play again(yes/no)? ')

if play_again_request.lower()=='yes': 
    play=True 
else: 
    play=False

while play:
    print('Welcome to rock paper scissors!') 
    outcome=request_input() 
    if outcome=='Tie': 
        print('Its a tie!') 
    else:
        print(outcome+' won!') 
    play_again_request=input('Play again(yes/no)? ') 
    if play_again_request.lower()=='yes': 
        play=True 
    else: 
        play=False 
