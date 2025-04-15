import random
l=["Rock","Scissor","Paper"]
while True:
  ccount=0
  ucount=0
  uc=int(input('''
  game start.....
  1 yes
  2 No / Exit
  '''))
  if uc==1:
     for a in range(1,6):
       userinput=int(input('''
       1 Rock
       2 Scissor
       3 Paper
       '''))
       if userinput==1:
          uchoice="rock"
       elif userinput==2:
             uchoice="scissor"
       elif userinput==3:
             uchoice="paper"
       else:
         print("invalid input")
         continue
       Cchoice=random.choice(l)
       if uchoice==Cchoice:
            print("tie")
       elif(uchoice=="rock"and Cchoice=="scissor") or (uchoice=="paper"and Cchoice=="rock") or (uchoice=="scissor"and Cchoice=="paper"):
            print("Computere value",Cchoice)
            print("User value",uchoice)
            print("You win")
            ucount=ucount+1
       else:
          print("Computere value",Cchoice)
          print("User value",uchoice)
          print("Computer win")
          ccount=ccount+1
  else:
    break