import random

l = []

def question(list):
    s = input("Enter yes/no(y/n):")
    length = len(list)
    housie(s,length,list)
def housie(str,leng,list):    
    if(str.upper()=='Y'):
        n = random.randint(1,90)
        if leng == 90:
            print("Game over!!")
            return
        elif n in list:
            housie(str,leng,list)
        else:
            print(n)
            l.append(n)
            question(list)
    elif(str.upper()=='N'):
        print("Ending the Game......\nThankyou for chosing my program!")
        return
    else:
        print("Invalid Choice!!")

question(l)
           