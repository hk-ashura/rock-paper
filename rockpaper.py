x=input("wanna play rock paper scissors").lower()
if x == "yes":

    import random 

    wins = {
        'r':'s',
        'p':'r',
        's':'p'
    }

    y = input("input r for rock 'p' for paper and 's' for scissors   ").lower()
    z = random.choice(['r','s','p'])

    if y not in ['r','s','p']:
        print("invalid input")
    elif z == y:
        print("draw")
    elif wins[y] == z:
        print(f'u win u chose {y}  and the computer chose {z}')
    else:
        print(f"u lose you chose {y} and the computer chose {z}")
    
