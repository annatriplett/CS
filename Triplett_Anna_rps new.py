#cat
import random                                                                       
game=input("Which Game? rock,paper,scissors, or Magic 8 Ball, or guaranteed win or loose rock,paper,scissors")#Game asks Which Game? Rock, Paper, Scissors, or Magic 8 Ball, or Guaranteed Win or Lose Rock, Paper, Scissors"
print("  _")                                                                                                     #print part of snowman image 
print("_|_|_")                                                                                                   #print part of snowman image 
print(" ('')")                                                                                                   #print part of snowman image
print("<( . )>")                                                                                                 #print part of snowman image
print("(  .  )")                                                                                                 #print part of snowman image
print("_______")                                                                                                 #print part of snowman image

if game == "rock,paper,scissors":                                                                              #If user chooses "Rock, Paper, Scissors"
    options = ["Rock", "Paper", "Scissors","Fire"]                                                               #options to choose from are Rock, Paper, or Scissors
    p1_score = 0                                                                                                 #p1 score is 0
    p2_score = 0                                                                                                 #p2 score is 0
    score_limit = 100                                                                                            #score limit is 100

    p1_name = input("What's your name, player 1? ")                                                              #Player 1's name 
    while True:                                                                                                  #Forever loop
        multiplayer = input("Do you want to play against a bot or player? ")                                     #Displays message "Do you want to play against a bot or player? "

        if multiplayer == "bot":                                                                                 #If player chose bot 
            p2_name = "bot"                                                                                      #Then player two is bot
            break                                                                                                #ends forever loop
        elif multiplayer == "player":                                                                            #if player chose player
            p2_name = input("What's your name, player 2? ")                                                      #player 2's name 
            break                                                                                                #ends forever loop
        else:                                                                                                    #if user imputs anything else
            print("invalid")                                                                                     #display message Invalid
    while p1_score < score_limit and p2_score < score_limit:                                                     #While player 1's score is les than score limit and player 2's score is less than score limit
        p1_response = input (f"{p1_name}, choose Rock, Paper, Fire or Scissors").capitalize()                  #player one response
        if p1_response in options:                                                                             #if user response with something in list options
            if multiplayer == "bot":                                                                             #if player is bot
                p2_response = random.choice(options)                                                             #computer chooses a random option from the list above
            else:                                                                                                #if user inputs anythign else
                print("\n"*45)                                                                                   #display lots of lines 
                
                p2_response = input (f"{p2_name}, choose Rock, Paper, Fire or Scissors").capitalize()            #player 2 response
            print (f"p1 chose {p1_response}, p2 chose {p2_response}")                                          #display what player one chose and what player two chose
    
            if p1_response == p2_response:                                                                       #if player one chooses the same option as player two 
                print("Tie!")                                                                                    #display message you tied 
            elif p1_response == "Rock" and p2_response == "Paper":                                               #if player one chooses Rock and player two chooses paper
                print(f"{p1_name} loses!")                                                                       #display message player one Loses!
                p1_score -= 1                                                                                    #subact 1 from player one score 
                p2_score += 1                                                                                    #Add 1 to player twos score
            elif p1_response == "Rock" and p2_response == "Scissors":                                            #if player one chooses Rock and player two chooses paper
                print(f"{p2_name} win!")                                                                         #display message player two wins!
                p1_score += 1                                                                                    #add 1 to player ones score
                p2_score -=1                                                                                     #Subract 1 from player twos score
            elif p1_response == "Paper" and p2_response == "Rock":                                               #if player one chooses Paper and computer chooses rock
                print(f"{p2_name} win!")                                                                         #display message player two wins!
                p1_score -= 1                                                                                    #Subract one from player ones score
                p2_score +=1                                                                                     #Add 1 to player twos score 
            elif p1_response == "Paper" and p2_response == "Scissors":                                           #if player one chooses Paper and player two chooses Scissors
                print(f"{p1_name}lose!")                                                                         #display message player one loses!
                p2_score += 1                                                                                    #Add 1 to player twos score 
                p1_score -=1                                                                                     #Subract 1 from player ones score
            elif p1_response == "Scissors" and p2_response == "Rock":                                            #if player one chooses scissors and player two chooses rock
                print(f"{p1_name}lose!")                                                                         #display message player one lose!
                p2_score += 1                                                                                    #add 1 to player twos score 
                p1_score -=1                                                                                     #subract 1 from player ones score                                                          
            elif p1_response == "Scissors" and p2_response == "Paper":                                           #if player one chooses scissors and player two chooses paper
                print(f"{p2_name}win!")                                                                          #display message player two win!
                p1_score -= 1                                                                                    #subract 1 from player ones score
                p2_score +=1                                                                                     #Add 1 to player twos score
            elif p1_response == "Scissors" and p2_response == "Paper":                                           #if player one chooses scissors and player two chooses paper
                print(f"{p2_name} win!")                                                                         #display message player two win!
                p1_score -= 1                                                                                    #subract 1 from player ones score
                p2_score +=1                                                                                     #Add one to player twos score
            elif p1_response == "Fire" and p2_response == "Paper":                                               #if player one chooses fire and player two chooses paper
                print(f"{p2_name} win!")                                                                         #Display message player two wins
                p1_score -= 1                                                                                    #subract 1 from player ones score
                p2_score +=1                                                                                     #Add one to player twos score
            elif p1_name == "Fire" and p2_response == "Rock":                                                #if player one chooses fire and player two chooses rock
                print(f"{p1_name} lose!")                                                                        #Displayer message player 1 lose
                p2_score += 1                                                                                    #Add one to player twos score
                p1_score -=1                                                                                     #subract 1 from player ones score
            elif p1_name == "Fire" and p2_response == "Scissors":                                            #if player one chooses fire and player two chooses scissors
                print(f"{p2_name} win!")                                                                         #Display message player two wins
                p1_score -= 1                                                                                    #subract 1 from player ones score
                p2_score +=1                                                                                     #Add one to player twos score
            elif p1_response == "Paper" and p2_response == "Fire":                                               #if player one chooses scissors and player two chooses fire
                print(f"{p1_name} lose!")                                                                         #Display messgae player one loses
                p2_score += 1                                                                                    #Add one to player twos score
                p1_score -=1                                                                                     #subract 1 from player ones score
            elif p1_response == "Rock" and p2_response == "Fire":                                                #if player one chooses scissors and player two chooses fire
                print(f"{p2_name} win!")                                                                          #Display message player two wins
                p1_score -= 1                                                                                    #subract 1 from player ones score
                p2_score +=1                                                                                     #Add 1 to playert wos score 
            elif p1_response == "Scissors" and p2_response == "Fire":                                          #if player one chooses scissors and player two chooses fire
                print(f"{p1_name} lose!")                                                                        #Display messgae player one loses
                p2_score += 1                                                                                    #Add one to player twos score
                p1_score -=1                                                                                     #subract 1 from player ones score
        else:                                                                                                    #If user imputs anything other thanks Rock,Paper, or Scissors
            print ("invalid")                                                                                    #display message Invalid 
            
        play = input("Play Again?")                                                                              #Display message Play Again?
        print("  (\_/)")                                                                                         #Print part of image
        print(" (='.'=)")                                                                                        #Print part of image
        print("('')_('')")                                                                                       #Print part of image
           
        if play == "yes":                                                                                        #if user inputs yes 
            print("yay")                                                                                         #display message yay
        elif play == "no":                                                                                       #if user inputs no
            break                                                                                                #end the loop

elif game== "Magic 8 Ball":                                                                                      #If user chooses game Magic 8 Ball
    responses = ["Yes", "definitely","No","ask again later","unclear","definitely not","1000000% yes"]           #Responses for bot to choose
    question_words = ["What", "When","Where","Who","Whom","Which","Whose","Why","Wow","Or","Am","As","Did","Does"]#Valid words user can use

    while True:                                                                                                  #Forever loop
        question = input("Ask magic 8 ball a question")                                                          #Display message Ask magic 8 ball a question
        if ("?")in question and question.split()[0] in question_words:                                           #if ? in question and first word of question is in question words 
            print (random.choice(responses))
            play = input("Play Again?")                                                                          #Display message Play Again
                                                                                             
            if play == "yes":                                                                                    #if user inputs yes 
                print("yay")                                                                                     #display message yay
            elif play == "no":                                                                                   #if user inputs no
                break                                                                                           #But then picks a random choice from responses 
        else:                                                                                                    #If user inputs anything else
            print ("invalid")
            
                                                                                                                   #End forever loop
                                                                                                               #Display message invalid

if game == "guaranteed win or loose rock,paper,scissors":                                                      #If game chosen is Guerenteed Win or Loose Rock, Paper, Scissors"                 
   
    while True:                                                                                                  #Forever loop
        user_response = input ("Choose Rock, Paper, Scissors")                                           #display message Choose Rock, Paper or Scissors

        if user_response == "Rock":                                                                              #if user chooses Rock 
            print("Computer picks scissors. You Win!")                                                           #display message "Computer picks scissors. You Win!"!
            play = input("Play Again?")                                                                          #Display message Play Again                                                                                   #Print part of image 
               
            if play == "yes":                                                                                    #if user inputs yes 
                print("yay")                                                                                     #display message yay
            elif play == "no":                                                                                   #if user inputs no
                break                                                                                          #Add 1 to score 
        elif user_response == "Scissors":                                                                        #if user chooses Scissors
            print("Computer picks Paper. You Win!")                                                              #Display message Computer picks Paper. You Win!                                                
            play = input("Play Again?")                                                                          #Display message Play Again                                                                                   #Print part of image 
               
            if play == "yes":                                                                                    #if user inputs yes 
                print("yay")                                                                                     #display message yay
            elif play == "no":                                                                                   #if user inputs no
                break                                                                                            #Add 1 to score 
        elif user_response == "Paper":                                                                           #if user chooses paper
            print("Computer Picks Rock You Win!")
                                                                                                                        #display message Computer Picks Rock You Win!!
            play = input("Play Again?")                                                                          #Display message Play Again                                                                                   #Print part of image 
               
            if play == "yes":                                                                                    #if user inputs yes 
                print("yay")                                                                                     #display message yay
            elif play == "no":                                                                                   #if user inputs no
                break                                                                                           #Add 1 to score 
        else:                                                                                                    #If user imputs anything other thanks Rock,Paper, or Scissors
            print ("invalid")                                                                                    #display message Invalid 
                
                                                                                                    #End forever loop
