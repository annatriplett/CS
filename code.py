print("Alarm!")

while True:
    snooze = input("snooze? y/n: ")

    if snooze == "y":
        print("Sleep for 5 more minutes")
        print("Alarm!")
    elif snooze == "n":
        break
    else:
        print("Invalid")
print("wake up")

while True:
    get_ready = input("get ready? yes/no")
    if get_ready == "yes":
        print ("go to school")
        break
    elif get_ready == "no":
        print ("Stay home")
        break
    else:
        print("Invalid")
while True:
    take_a_left = input("take a left? yes/no")
    if take_a_left == "yes":
        print ("arrive on time to school")
        break 
    elif take_a_left == "no":
        print ("arrive late to school")
        break
    else:
        print("Invalid")
while True:
    Skip_Class = input("Skip Class? yes/no")
    if Skip_Class == "yes":
        print("go home")
        break 
    elif Skip_Class == "no":
        print("go to lunch")
        break
    else:
        print("Invalid")
while True:
    Eat_Lunch = input("Eat Lunch? yes/no")
    if Eat_Lunch == "yes":
        print("Finish")
        break 
    elif Eat_Lunch == "no":
        print ("go home")
        break
    else:
        print("Invalid")

    
