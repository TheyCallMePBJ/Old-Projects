#task1
name=[]
player1scores=[]
player2scores=[]
player3scores=[]
player4scores=[]
sums=[]
score=[]

anychanges="yes"
while anychanges!="No" and anychanges!="NO" and anychanges!="no":
    numplayers=int(input("Enter the number of players as 2, 3 or 4: "))
    while numplayers<2 or numplayers>4:
        numplayers=int(input("Invalid. Number of players should be 2, 3 or 4. Please enter the number of players: "))
    for i in range (numplayers):
        name.append(" ")
        names=str(input("Enter player name: "))
        name[i]=names
    numberofholes= int(input("Enter the number of holes as 3 or 18: "))
    while numberofholes!= 3 and numberofholes!=18:
        numberofholes= int(input("INVALID: Please enter the number of holes as 3 or 18: "))
    
    parforthecourse= int(input("Enter the par for the course: "))
    print ("Number of players: ", numplayers)
    print ("Player names: ")
    for i in range (numplayers):
        playername=name[i]
        print ("Player ",i+1,": ",playername)
    print ("Number of holes: ",numberofholes)
    print ("Par for the course: ",parforthecourse)
    anychanges=str(input("Do you want to change any details? Enter 'yes' or 'no'"))
    
for i in range (numberofholes):
        player1scores.append(0)
        player2scores.append(0)
        player3scores.append(0)
        player4scores.append(0)
#task2
sum1=0
sum2=0
sum3=0
sum4=0


for holenum in range (numberofholes):
    playercount=1
    i=0
    while i!=numplayers:
        print (name[i], ", Please enter number of strokes played for hole ", holenum+1)
        scoreforhole=int(input())
        scoreforholetwo=int(input("Please enter number of strokes played again to verify "))
        while scoreforhole != scoreforholetwo:
            print ("Error: please enter number of strokes again: ")
            scoreforhole=int(input())
            scoreforholetwo=int(input("Please enter number of strokes played again to verify "))
        if playercount==1:
            player1scores[holenum]=scoreforhole
            playercount=playercount+1
            sum1=sum1+scoreforhole
        elif playercount==2:
             player2scores[holenum]=scoreforhole
             playercount=playercount+1
             sum2=sum2+scoreforhole
        elif playercount==3:
             player3scores[holenum]=scoreforhole
             playercount=playercount+1
             sum3=sum3+scoreforhole
        elif playercount==4:
             player4scores[holenum]=scoreforhole
             sum4=sum4+scoreforhole
        i=i+1
    
    for i in range (4):
        sums.append(0)
        score.append(0)
    sums[0]=sum1
    sums[1]=sum2
    sums[2]=sum3
    sums[3]=sum4
        
    for i in range (numplayers):
        print (name[i], ", do you want to see your total score? Enter 'Yes' or 'No'")
        yesorno= str(input())
        if yesorno=="yes" or yesorno=="Yes" or yesorno=="YES":
            print (name[i],"'s total score:", sums[i])
    
for i in range (numplayers):
    if sums[i]>parforthecourse:
        score[i]=sums[i]-parforthecourse
        print (name[i]," score: ", score[i], "over par")
    else:
        score[i]=parforthecourse-sums[i]
        print (name[i]," score: ", score[i], "under par")
    


    
if sums[2]==0:
    sums[2]=100000000
    
if sums[3]==0:
    sums[3]=100000000

highscore=sums[0]
highplayer=0

for i in range (numplayers):
    if sums[i]<highscore :
        highscore=sums[i]
        highplayer=highplayer+1
print("Congratulations ", name[highplayer], "! You are the winner with a score of", highscore)


options=1 
while options!=0:
    print ("Enter '1' to see every player's score for each hole")
    print("Enter '2' to see if anyone got a hole-in-one")
    print("Enter '3' to see the average for the round")
    print("Enter '4' to see the average for a particular hole")
    print("Enter '0' if you are finished")
    options=int(input())
    if options==0:
        break
        
    elif options==1:
        
        print (name[0],"'s scores:", player1scores)
        print (name[1],"'s scores:", player2scores)
        if (numplayers>2):
            print (name[2],"'s scores:", player3scores)
        if (numplayers>3):
            print (name[3],"'s scores:", player4scores)
    elif options==2:
        for i in range (numberofholes):
            if player1scores[i]==1:
                print ("Congratualations ", name[0], "! You scored a hole-in-one for hole ", i+1)
            if player2scores[i]==1:
                print ("Congratualations ", name[1], "! You scored a hole-in-one for hole ", i+1)
            if player3scores[i]==1:
                print ("Congratualations ", name[2], "! You scored a hole-in-one for hole ", i+1)
            if player4scores[i]==1:
                 print ("Congratualations ", name[3], "! You scored a hole-in-one for hole ", i+1)
    elif options==3:
        total=0
        if numplayers<3:
            sum3=0
        if numplayers<4:
            sum4=0
        total=sum1+sum2+sum3+sum4
        totalholes= numberofholes*numplayers
        roundaverage=total/totalholes
        print("Average score for the round is: ",roundaverage)
    elif options==4:
        which=int(input("Enter desired hole number: "))
        
        totalforhole= player1scores[which]+ player2scores[which]+ player3scores[which]+player4scores[which]
        holeaverage=totalforhole/numplayers
        print ("Average score for hole ",which, " is ", holeaverage)
    else:
        print ("INVALID: Please enter option from 0 to 4")
    
    
                 

    
