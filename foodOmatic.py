'''
Author: Anna Triplett
Date: 4/2/25
Description: Pick between two games and have a blast!
Bugs: None 
Challenges: All 
Sources: Ms. Marciano 
'''#Flower pot 

import random
while True:#forever loop 
    game=input("Which Game? rock, paper, scissors, or foodOmatic. Enter 'p' to exit: ")#ask player which game 

    if game == "p":#if player enters p
        break   #quit game 
    elif game == "foodOmatic": #game inputed by player is foodOmatic         
        snacks = ["chips", "cookies", "popcorn", "takis", "goldfish", "pretzel", "oatmeal bar", "candy", "chedder bunnies"]#list of snacks
        snack_prices = [10,12, 5, 15, 20, 3, 9, 8, 16]#list of snack prices 
        drinks = ["water","sprite", "coke", "coffee", "gingerale", "hint", "lemon perfect", "diet coke", "topochico"]#List of drinks 
        drink_prices = [12,3,5, 13, 14, 2, 17, 16, 20]#Drink price list 

        while True:#forever loop 
            try:#attempt 
                num_of_items = int(input('How Many Items Do You Want? '))#Display message How Many Items Do You Want? and the integer the player inputs is the number of items 

                if num_of_items < 9:#if number of items is less than 9 
                    print ("Damn you're hungry!")#display message Damn you're hungry 
                    break#end forever loop 
                else:#if number inputed is greater than 9 
                    print ("Must be less than 9 items!")#display message Must be less than 9 items!
            except ValueError:#
                print("Enter an Integer please")#Display message Enter an Integer please
        
        total = 0#Total is 0 

        for i in range(num_of_items): #repeats for the number of items user enters          
            snack = random.choice(snacks)#Pick random item from snack list 
            drink = random.choice(drinks)#Pick random item from drink list 
            snack_price = snack_prices[snacks.index(snack)]#Print price that corrilates to snack item chosen 
            drink_price = drink_prices[drinks.index(drink)]#Print price that corrilates to drink item chosen 
            print(f'{snack} with {drink}. Your cost is ${snack_price} + ${drink_price} = ${snack_price+drink_price}')#f chain - display snack and drink items, your costs and their total 
            total += snack_price + drink_price#add snack and drink price to total 
        print(f'${total}')#display entire price of all the items added up 
        
    elif game == "rock, paper, scissors":                                                                              #If user chooses "Rock, Paper, Scissors"
        options = ["Rock", "Paper", "Scissors"]                                                               #options to choose from are Rock, Paper, or Scissors
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
            p1_response = input (f"{p1_name}, choose Rock, Paper, or Scissors").capitalize()                  #player one response
            if p1_response in options:                                                                             #if user response with something in list options
                if multiplayer == "bot":                                                                             #if player is bot
                    p2_response = random.choice(options)                                                             #computer chooses a random option from the list above
                else:                                                                                                #if user inputs anythign else
                    print("\n"*45)                                                                                   #display lots of lines 
                    
                    p2_response = input (f"{p2_name}, choose Rock, Paper, or Scissors").capitalize()            #player 2 response
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
                                                                                                   #subract 1 from player ones score
            else:                                                                                                    #If user imputs anything other thanks Rock,Paper, or Scissors
                print ("invalid")                                                                                    #display message Invalid 
                
            print("  (\_/)")                                                                                         #Print part of image
            print(" (='.'=)")                                                                                        #Print part of image
            print("('')_('')")                                                                                       #Print part of image
