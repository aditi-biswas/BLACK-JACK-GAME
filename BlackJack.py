import random                     

sump=0
sumc=0
deck=[]

dict={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':11,'K':12}

def num_chk():    #function to check if number is entered or not
    while True:
        n=input()
        if(n.isdigit()):
            return int(n)
        else:
            print("Looks like you didn't enter number..please enter amount in number")

def tot_cards():     #function for total cards
    global deck
    global sumc                
    global sump
    sumc=0
    sump=0
    deck.clear()
    for i in range(4):
        deck.append('K')
        deck.append('Q')
        deck.append('J')
        deck.append('A')
        for i in range(2,10,1):
            deck.append('{}'.format(i))
    random.shuffle(deck)
    
def initial_cards(x,s):    #function to give each player their initial 2 cards
    global deck
    m=1
    k=len(deck)-1
    while(m<3):
        a=deck[k]
        if ((s+dict[a])<21):
            x.append(a)
            s=s+dict[a]
            deck.pop()
            m+=1
            k-=1
        else:
            k-=1
    return s

def bet():      #function to define bet amount
    print("Enter amount you want to keep as a bet")
    while True:
        b=num_chk()
        if(b>acc):
            print("Sorry, this transaction can be made! Bet amount exceeds your account balance ")
        elif(b==acc):
            print("This transaction will result in your account balance to be zero.Are you sure you want to make this transaction? Y or N")
            d=False
            while d==False:
                ch=input("Please enter 'Y' if yes else enter 'N'")
                if (ch.upper()=='Y'):
                    return b
                elif(ch.upper()=='N'):
                    d=True
                else:
                    print("Sorry, I didn't understand. Please make sure to choose Y or N.")
        else:
            return b


def first_display():      #function to display one of computer dealer's cards
    print("Cards human player has: ")
    for i in range(2):
        print(player[i],end="   ")
    print('\n')
    print("One of the 2 cards computer dealer has: ",comp[0])
    
def choice():
    choice1=' '
    while choice1.upper() not in ['HIT','STAND']:
        choice1=input("Would you like to HIT or STAND? ")
        if choice1.upper() not in ['HIT','STAND']:
            print("Sorry, I didn't understand. Please make sure to choose HIT or STAND.")
        else:
            if(choice1.upper()=='HIT'):
                return True
            else:
                return False

def hit(x,sum):     #function for "hit"
    x.append(deck[len(deck)-1])
    deck.pop()
    a=x[len(x)-1]
    sum=sum+dict[a]
    return (sum,a)

def win_lose(sum,txt1,txt2):    #function to determine who won
    global acc
    global acc_c
    global sumc
    global sump
    global b
    if(sum==21):
        print("{} is WINNER".format(txt1))
        if(txt1=='HUMAN PLAYER'):
            print("Congratulations!!!")
            acc=acc+b*2
        else:
            print("Oops, HUMAN PLAYER you did not win this match..better luck next time.")
            acc_c=acc_c+b
    elif(sum>21):
        print("{} has encountered BUST! {} is WINNER!!".format(txt1,txt2))
        if(txt2=='HUMAN PLAYER'):
            print("Congratulations!!")
            acc=acc+b*2
        else:
            print("Oops, HUMAN PLAYER you did not win this match..better luck next time.")
            acc_c=acc_c+b
    elif(sumc>sump):
        print("Seems like you did not win..COMPUTER DEALER's sum is GREATER than HUMAN PLAYER's sum! COMPUTER DEALER is WINNER!!")
        acc_c=acc_c+b
    else:
        pass

def gameon_choice():     #function to choose if player wants to continue the game
    choice1=' '
    while choice1.upper() not in ['Y','N']:
        choice1=input("Would you like to keep playing? Y or N ")
        if choice1.upper() not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
        else:
            if(choice1.upper()=='Y'):
                return True
            else:
                return False

print("BLACKJACK !!")
print("Reach 21 First and win the game...")
print("LET'S START !!!")
print("Enter total amount in your bank account: ") 
acc=num_chk()    
game_on=True
acc_c=0
while game_on==True:
    player=[]
    comp=[]
    moc=False
    b=bet()
    acc=acc- b
    tot_cards()
    sump=initial_cards(player,sump)
    sumc=initial_cards(comp,sumc)
    print("Human Player's sum of values of cards ",sump)
    print("Computer dealer's sum of values of cards ",sumc)
    first_display()
    while True:
        ch=choice()
        if(ch==True):
            tup=hit(player,sump)
            sump=tup[0]
            print("The card you picked: ",tup[1])
            print("Now your sum is: ",sump)
            win_lose(sump,'HUMAN PLAYER','COMPUTER DEALER')
            if(sump>=21):
                break
        else:
            break
    c=0
    if(sump<21):
        while True:
            if(sumc<=sump):
                c=c+1
                print("Computer's hit",c)
                tup2=hit(comp,sumc)
                sumc=tup2[0]
                print("Card Computer dealer picked: ",tup2[1])
                print("Computer dealer's total value of cards: ",sumc)
            else:
                break
        win_lose(sumc,'COMPUTER DEALER','HUMAN PLAYER')
    print("Total account balance of player: ",acc)
    print("Total account balance of dealer: ",acc_c)
    if(acc>0):
        game_on=gameon_choice()
    else:
        print("No more games can be played as your account balance is zero")
        game_on=False
        


