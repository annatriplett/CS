import os
import time
import random
import csv


def enter_code(password, tries):
    '''
Takes a secret password from the user and uses it to later let the user into the code.
    Arg:
        password(str): The correct password the user needs to enter
        tries(int): number of attempts the user is allowed to use when guessing the password
    Return:
        bool: True/False based on if password is correct
    '''
    for i in range(tries):
        check_password = input('Enter your secret code:')
       
        if check_password == password:
            print('welcome')
            time.sleep(1)
            return True
        else:
            print(f'incorrect. you have {tries-i-1} tries left')
    print ("oops bye ")
    time.sleep(1)
    return False
def add_entry(websites, usernames, passwords):
    '''
Lets user add a website, username, and/or password 
    Arg:
        websites(list):List to store inputted website
        usernames(list):List to store inputted username
        passwords(list):List to store inputted password
    Return:
        none
    '''


    website = input('Enter website: ')
    username = input('Enter username: ')
    password = input('Enter password (press "g" to generate): ')


    if password.lower() == "g":
        password = generate_password()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)
def get_password_length():
    '''
User enters length for the password they want 
        Arg:
            none
        Return:
            int: The password length (integer) entered by the user
        '''
    while True:
        try:
            length = int(input("Enter the desired length of your password: "))
            return length
        except ValueError:
            print('Please enter an integer')
def secure_password(password):
    '''
Checks if password is secure 
        Arg:
            password(str): The password used to determine whether it is secure or not
        Return:
            Print: If the password is secure or not
        '''
    length = get_password_length()
   
    if len(password) < length or password.lower() == password or password.upper() == password or not any(char.isdigit() for char in password) or not any(char in password for char in list('~!@#$%^&*')):                                                                  
        print('password insecure')
    else:
        print('password secure')
def generate_password():
    '''
Generates a password for the user based on the length they inputted above
    Arg:
        none
    Return:
        str: randomly generated password
    '''
    length = get_password_length()
    return ''.join(random.sample(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*1234567890'), length))
def print_entry(website, username, password):
    '''
Prints all the websites, usernames, and passwords 
    Arg:
        website(list): Name of website
        username(list):username belonging with the website
        password(list):password belonging with the website
    Return:
        Print: The username and password to the website inputted
    '''
    print(f'''
Website: {website}
Username: {username}
Password: {password}
    ''')  
def get_index(websites):
    '''
Prints the index of the specific website the user inputs
    Arg:
        websites(list): List containing all websites
    Return:
        int: The index of the website entered by the user
    '''
    while True:
        website = input(f'Pick a website ')
       
        if website in websites:
            return websites.index(website)
        else:
            print ('website not here')
def change_entry(websites, usernames, passwords):
    '''
Allows user to change an entry 
    Arg:
        websites(list): List of websites
        usernames(list):username belonging with the website
        passwords(list):password belonging with the website
    Return:
        none
    '''
    index = get_index(websites)
    websites[index] = input('Enter new website: ')
    usernames[index] = input('Enter new username: ')
    passwords[index] = input('Enter new password: ')


def delete_entry(websites, usernames, passwords):
    '''
Allows user to delete an entry 
    Arg:
        websites(list): List of websites
        usernames(list):username belonging with the website
        passwords(list):password belonging with the website
    Return:
        none
    '''
    index = get_index(websites)
    websites.pop(index)
    usernames.pop(index)
    passwords.pop(index)


def export_to_csv(filename, headers, *arrays):
    '''
Allows user to export websites, usernames, and passwords to a CSV file
    Arg:
        filename(str): The name of the CSV file to write to
        headers(list): List of headers to write as the first row in the CSV file
        arrays(list): One or more lists that will be written in the CSV file
    Return:
        none
    '''
    if not arrays:#if no data 
        raise ValueError("At least one array must be provided.")#If the user does not put in a value, it triggers a value error and asked the user to input at least one array 
   
    num_rows = len(arrays[0])#number of arrays/rows needed 


    for arr in arrays:# goes through each array and gets first element 
        if len(arr) != num_rows:#how many first elements it searches
            raise ValueError("All arrays must have the same length.")#Triggers value error if different length it inputted
   
    with open(filename, 'w', newline='') as csvfile:#Opens file - with inputted filename 
        csvwriter = csv.writer(csvfile)#takes file and writes rows of data
        csvwriter.writerow(headers)#takes file and writes rows of data


        for i in range(num_rows):#takes file and writes rows of data
            row = [arr[i] for arr in arrays]#takes file and writes rows of data
            csvwriter.writerow(row)#takes file and writes rows of data
def main():
    websites = []
    usernames = []
    passwords = []


    secret_code = input('What do you want your password to be? ')
    time.sleep(1)
    os.system('cls')


    add_entry(websites,usernames,passwords)
   
    if not enter_code(secret_code, 3):
        exit()


    while True:
        option = input ('''which one would you like to do
    1. Add more entries
    2. See all entries
    3. Access specific entry
    4. Delete an entry
    5. Generate or change password
    6. Check password security
    7. Export entries
    8. End Game
            ''')
        if option == "8":
            break
        elif option == "1":
            add_entry(websites,usernames,passwords)
        elif option == "2":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])  
        elif option == "3":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "4":
            delete_entry(websites, usernames, passwords)  
        elif option == '5':
            pwd_change = input('Would you like to change (1) or get a password? (2) ')


            if pwd_change == "1":
                index = get_index(websites)
                passwords[index] = generate_password()
            elif pwd_change == "2":
                print(generate_password())
        elif option =='6':
            index = get_index(websites)
            secure_password(passwords[index])
        elif option == '7':
            filename = input('Enter the filename for your csv: ')
            export_to_csv(filename+".csv", ["Website", "Username", "Password"], websites, usernames, passwords)
main()

