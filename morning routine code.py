import time
import datetime
def print_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }

    color_code = colors.get(color_name.lower(), '\033[37m')  # Default to white if color not found
    print(f"{color_code}{text}\033[0m")  # Print text with color and reset
def input_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }

    color_code = colors.get(color_name.lower(), '\033[37m')  # Default to white if color not found
    return input(f"{color_code}{text}\033[0m")  # Print text with color and reset

print_colored_text("hello world", 'red')
response = input_colored_text("user input: ", 'blue')
if response == "yes":
    print_colored_text('yay', 'green')



print_colored_text ("ALARM!", 'magenta')
current_time = datetime.datetime(2024, 10, 23, 6, 30, 0) 
print_colored_text(current_time.strftime("%H:%M:%S"), 'blue')

while True:
    snooze = input_colored_text ("snooze? y/n: ", 'red')

    if snooze == "y":
        print_colored_text("go back to sleep for 5 mins", 'black')
        time.sleep(2)
        current_time += datetime.timedelta(minutes=2)
    elif snooze == "n":
        print_colored_text ("get up",'red')
        current_time += datetime.timedelta(minutes=1)
        break
    else:
        print_colored_text("invalid reponse",'green')
    
print_colored_text(current_time.strftime("%H:%M:%S"), 'cyan')
print_colored_text("wake up",'yellow')

while True:
    get_ready = input_colored_text("get ready? yes/no",'cyan')
    if get_ready == "yes":
        print_colored_text ("go to school",'magenta')
        break
    elif get_ready == "no":
        print_colored_text ("Go to school, you cant stay home",'red')
        break
    else:
        print("Invalid")
while True:
    take_a_left = input_colored_text("take a left? yes/no",'blue')
    if take_a_left == "yes":
        print ("arrive on time to school")
        break 
    elif take_a_left == "no":
        print_colored_text ("arrive late to school",'black')
        break
    else:
        print("Invalid")
while True:
    Skip_Class = input("Skip Class? yes/no")
    if Skip_Class == "yes":
        print_colored_text("get detention",'cyan')
        break 
    elif Skip_Class == "no":
        print_colored_text("go to lunch",'blue')
        break
    else:
        print("Invalid")
while True:
    Eat_Lunch = input("Eat Lunch? yes/no")
    if Eat_Lunch == "yes":
        print_colored_text("sleepover at school!",'yellow')
        break 
    elif Eat_Lunch == "no":
        print_colored_text("go home",'magenta')
        break
    else:
        print("Invalid")

