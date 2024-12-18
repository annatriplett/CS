import random

def print_colored_text(text, color_name):                               #creates a function print_colored_text that takes in text and color_name 
    colors = {                                                          #Color dictionary that maps color names to their ANSI escape code for terminal text coloring 
        'black': '\033[30m',                                            #Black text color code 
        'red': '\033[31m',                                              #red text color code
        'green': '\033[32m',                                            #green text color code 
        'yellow': '\033[33m',                                           #yellow text color code 
        'blue': '\033[34m',                                             #blue text color code 
        'magenta': '\033[35m',                                          #magenta text color code
        'cyan': '\033[36m',                                             #cyan text color code
        'white': '\033[37m',                                            #white text color code
        'reset': '\033[0m',                                             # Reset color (black) to defult 
    }

    color_code = colors.get(color_name.lower(), '\033[37m')             # finds color code for certain color if color not found, resets to defult color black 
    print(f"{color_code}{text}\033[0m")                                 # prints text in given color, has reset code to ensure no color leaks
    
name = input("What's your name, player 1? ")                            #allows user to enter their name
print(name, ", the goal of this game is to say the color the text is in and not the text itself")          #prints users name and goal of the game
correct = 0                                                             #set correct to 0
rounds = 0                                                              #set rounds to 0
colors = ['black', 'red', 'green', 'yellow','blue','magenta', 'cyan','white'] #creates color list 

while True:                                                             #forever loop
    text_color = random.choice(colors)                                  #text_color = random color choice 
    print_color = random.choice(colors)                                 #print_color = random color choice 
    print_colored_text(text_color, print_color)                         #call function with 2 variables above 
    user_color = input ("Enter the color of the text")                  #user_color = input the color of the text 

    print (f"{name} chose {user_color}, the text is {print_color}")     #display what the user chose and what the print color is 

    if user_color == print_color:                                       #if users guess equals color 
        print('you got it!')                                            #print you got it 
        correct += 1                                                    #add a point to correct 
    else:                                                               #if user says anything else 
        print('wrong')                                                  #print wrong 

    rounds += 1                                                         #adds one to rounds 

    while True:                                                         #forever loop
        play_again =input(f"{name} has {correct} out of {rounds} games. Play again? y/n: ")  #play_again = input users name and dispkay message you have gotten (However many you got correct) out of rounds, would you like to play agin? enter yes or no
        if play_again == "y":                                           #if play_again = y
            print("yay")                                                #display message yay 
            break                                                       #end forever loop
        elif play_again == "n":                                         #if play_again = n
            exit()                                                      #exit game 
        else:                                                           #if user inputs anything else
            print("invalid")                                            #display message invalid 
