def rps(player_1,player_2):
    if player_1=='scissor' and player_2=='paper':
        return player_1
    elif player_1=='scissor' and player_2=='rock':
        return player_2
    elif player_1=='paper' and player_2=='paper':
        return 'Draw'


def main():
    player_1=input("enter your choice from rock paper scissor:\n")
    player_2=input("enter your choice from rock paper scissor:\n")
    if rps(player_1,player_2)==player_1:
        print("player_1 won the game!")
    elif rps(player_1,player_2)==player_2:
        print("player_2 won the game!")
    else:
        print("Draw!")
main()
