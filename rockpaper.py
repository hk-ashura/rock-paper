import random 
def userInput():
                return input("input r for rock 'p' for paper and 's' for scissors   ").lower()
def whowon( y):   
        wins = {
                'r':'s',
                'p':'r',
                's':'p'}
        emoji= {
                "r": '🪨',
                'p':'📃',
                's':'✂️'
            }
        z = random.choice(['r','s','p'])

        if y not in ['r','s','p']:
                    print("invalid input")
        elif z == y:
                    print("draw")
        elif wins[y] == z:
                    print(f'u win u chose {y} {emoji[y]}   and the computer chose {z} "{emoji[z]}')
            
        else:
                    print(f"u lose you chose {y}  {emoji[y]} and the computer chose {z} {emoji[z]}")
def main():
    x=input("wanna play rock paper scissors\t").lower()
    if x == "yes":
        y=userInput()
        whowon(y)


            
    elif x =="no":
            print("oky ")
    else :
            print("invalid input")

main()
