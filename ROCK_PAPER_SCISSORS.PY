import random
cpu= random.randint(1,5)

# 1) ✊
# 2) ✋
# 3) ✌️
# 4) 🦎
# 5) 🖖
# Scissors cut Paper.
# Paper covers Rock.
# Rock crushes Lizard.
# Lizard poisons Spock.
# Spock smashes Scissors.
# Scissors beat Lizard.
# Lizard eats Paper.
# Paper disproves Spock.
# Spock vaporizes Rock.
# Rock breaks Scissors.

player = int(input("Enter your number: "))


if cpu ==1 :
    cpu = "✊"
elif cpu ==2 :
    cpu = "✋"
elif cpu ==3 :
    cpu = "✌️"
elif cpu ==4 :
    cpu = "🦎"
elif cpu ==5 :
    cpu = "🖖"
    
if player ==1 :
    player = "✊"
elif player ==2 :
    player = "✋"
elif player ==3 :
    player = "✌️"
elif player ==4 :
    player = "🦎"
elif player ==5 :
    player = "🖖" 


if player == cpu :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("Tie")
elif player == "✊" and cpu == "✌️" :
    print("Your: ",player)
    print("cpu: ",cpu)  
    print("You win")
elif player == "✊" and cpu == "🦎" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "✋" and cpu == "✊" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "✋" and cpu == "🖖" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "✌️" and cpu == "✋" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "✌️" and cpu == "🦎" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "🦎" and cpu == "🖖" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "🦎" and cpu == "✋" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "🖖" and cpu == "✊" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif player == "🖖" and cpu == "✌️" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("You win")
elif cpu == "✊" and player == "✌️" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "✊" and player == "🦎" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "✋" and player == "✊" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "✋" and player == "🖖" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "✌️" and player == "✋" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "✌️" and player == "🦎" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "🦎" and player == "🖖" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "🦎" and player == "✋" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "🖖" and player == "✊" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
elif cpu == "🖖" and player == "✌️" :
    print("Your: ",player)
    print("cpu: ",cpu)
    print("cpu win")
else:
    print("Invalid input")
