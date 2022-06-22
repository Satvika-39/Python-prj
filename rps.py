import random 
def is_win(player, opponent):
    #r > s , s > p,p > r 
    #returns ture if the user wins
    if  (player=='r'and opponent =='s') or (player=='s'and opponent =='p') or (player=='p'and opponent =='r'):
        return True

def play():
      user = input("Whats your choice? Rock is'r' Scissor is 's' Paper is 'p'\n")
      computer = random.choice(['r','s','p'])
      print(f"You chose {user} and the computer chose {computer}")
      if user == computer: 
        return 'It\'s a tie.' 

      if is_win(user,computer):
         return 'You won'
      
      return 'You lost.'

print(play())
