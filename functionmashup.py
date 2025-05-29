import random

def refrain():
    '''
    Seperates segments of the song into catagories to shorten the lengh needed to be writte. So when printed, if there is two verses that are the same, the same function will be printed twice so therfore the verse will be printed twince, but with less lines.

    Args:
        None
    Returns:
        print: refrain of song
    '''
    print("""
I'm fallin'
In all the good times, I find myself longin'
For change
And, in the bad times, I fear myself
    """)
def chorus():
    '''
    Prints the chorus

    Args:
        None
    Returns:
        print: chrous of song
    '''
    print("""
I'm off the deep end, watch as I dive in
I'll never meet the ground
Crash through the surface where they can't hurt us
We're far from the shallow now

In the sha-ha, shallow
In the sha-ha, sha-la-la-la-low
In the sha-ha, shallow
We're far from the shallow now
    """)
def song():
    '''
    Prints the entire song using refrain() and chorus()
    
    Args:
        None
    Returns:
        print: entire song
    '''
    print("""
Tell me somethin', girl
Are you happy in this modern world?
Or do you need more?
Is there somethin' else you're searchin' for?
""")
    refrain()
    print("""
Tell me something, boy
Aren't you tired tryna fill that void?
Or do you need more?
Ain't it hard keepin' it so hardcore?
""")
    refrain()
    chorus()
    print("""
Oh, ha, ah, ha
Oh-ah, ha
""")
    chorus()
def add(a, b):
    '''
    takes two integers ands adds them, printing the sum

    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of a and b
    '''
    print(a + b)
def print_list(array):
    
    '''
    Printing list veritcally
    
     Args:
        array (list): the list of items
        element (any): item to check
    Returns:
        print: the entire list alternating each element per line  
    '''
    for element in array:
        print(element)
def in_list(array, element):
    '''
    Determines whether the number is in the list 
    
     Args:
        array (list): someting from the list 
        element (any): something not in the list 
    Returns:
        bool: True/False based on if element is in array  
    '''
    return element in array
def get_integer():
    '''
    Get a single integer using user input
    
    Args:
        None
    Returns:
        int: number from user input
    '''
    while True:
        try:
            number = int(input('Enter an integer '))
            return number
        except ValueError:
            print('Not an integer!')
def get_integers():
    '''
    Takes two integers and adds them and prints the two numbers
    
     Args:
        None
    Returns:
        int: num1 and num2  
    '''

    num1 = get_integer()
    num2 = get_integer()         
    return num1, num2
def get_random ():
    '''
    Printing a random number between the users two inputs
    
    Args:
        None 
    Returns:
        print: A random number between the two numbers 
    '''
    a, b = get_integers()
    print(random.randint(a,b))
    
def count_vowels(string):
    '''
    takes the users words and prints the amount of vowels
    
     Args:
        string (str): word or phrase  
    Returns:
        int: total vowels in string 
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0

    for char in string:
        if char in vowels:
            total += 1 
    return total

def reverse_string(string):
    '''
    takes the users words and prints the reverse
    
    Args:
         string (str): word or phrase 
    Returns:
        str: string reversed  
    '''    
    return string[::-1]

def is_palindrome(string):
    '''
    takes the users words and sees if it is a palindrome
    
    Args:
        string (str): word or phrase 
    Returns:
        bool: True/False depending on if string is the same when it is reversed 
    '''
    return string == reverse_string(string)

def get_initials(fullname):
    '''
    takes the users full name and prints the first letter of each words, their initials
    
    Args:
        fullname (str):  fullname (first, middle, Last)
    Returns:
        str: the first letter of each name  
    '''
    name_list = fullname.split()
    initials = ''

    for name in name_list:
        initials += name[0]
    return initials

def replace_character(string, old_character, new_character):
    '''
    takes a word and replaces a letter with another letter
    
    Args:
        string (str): Word that is to be replaced
        old_character (str): The letter getting replaced
        new_character (str): The letter now going into the word
    Returns:
        str: the replacement, new word (if the word has L, replaces it with D)
    '''
    new_string = ''

    for char in string:
        if char == old_character:
            new_string += new_character
        else:
            new_string += char
    return new_string
        
def main():
    while True:
        option = input('What would you like to do: 1. Sing a song, 2. Add two numbers, 3. Print a list, 4. Return element in a list, 5. Add Integers, 6. How many vowels, 7. Reverse your word, 8. Is it a palindrome?, 9. Return your Initials!, 10. replace a character')

        if option =='1':
            song()
        elif option == '2':
            a, b = get_integers()
            add(a, b)
        elif option =='3':
            candies = ['hershey', 'lollipop', 'airheads', 'skittles']
            print_list(candies)
        elif option =='4':
            print(in_list(candies, 'lollipop'))
            print(in_list(candies, 1))
        elif option =='5':
            get_random()
        elif option =='6':
            word = input('Enter a word or phrase: ')
            print(count_vowels(word))
        elif option =='7':
            blabla = input('Enter a word or phrase: ')
            print(reverse_string(blabla))
        elif option =='8':
            googl = input('Enter a word or phrase: ')
            print(is_palindrome(googl))
        elif option =='9':
            fullname = input('What is your full name')
            print(get_initials(fullname))
        elif option =='10':
            string = input('pick a word')
            old_character = input('Pick letter in word to be replaced')
            new_character = input('Pick letter to replace old letter')
            print(replace_character (string, old_character, new_character))
        else:
            print('invalid')

main()










