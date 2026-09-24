import random 
import score as sl
import game as hl
print("welcome")
rn=random.randint(2,100)
attempt=0
for i in range(1,8):
    a=int(input("enter your no:"))
    if a==1:
        print("thankyou")
        break
    g1 = hl.guess(a,rn)
    if g1==1:
        attempt+=1
        print("you win no. is:",rn)
        print("your attempts are",attempt)
        s1 = sl.score(attempt)
        break
    elif g1==2:
        attempt+=1
        print("too high")
        print("attempts left",7-i)
    else:
        attempt+=1
        print("too low")
        print("attempts left",7-i)

if g1==1:
    print("your score is:",s1)
else:
    print("better luck next time")
    print("secret no. was",rn)