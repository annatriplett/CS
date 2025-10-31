'''
Author: Anna Triplett 
Due date: 9/30/2025 
Sources: Ms.Marciano, Mr.Campbell
Log: 1.0 initial release
'''

def get_type(length,height,thick):
    '''
    Classifies a mail item based on size and thickness measurments.
        Args:
            length: The length of the mail item in inches.
            height: The height of the mail item in inches.
            thick: The thickness of the mail item in inches.

        Returns:
            str: The classification of one of these mail items:
                - 'Post_Card'
                - 'Large_PostCard'
                - 'Envelope'
                - 'Large_Envelope'
                - 'Package'
                - 'Large_Package'
                - 'Unmailable'
        '''
  


    if 3.5<= length <= 4.25 and 3.5<= height <= 6 and .007<= thick <= .016:
        return 'Post_Card'
    if 4.25<= length <= 6 and 6<= height <= 11.5 and .007<= thick <= .015:
        return 'Large_PostCard'
    if 3.5<= length <= 6.125 and 5<= height <= 11.5 and .016<= thick <= .25:
        return 'Envelope'
    if 6.125<= length <= 24 and 11<= height <= 18 and .25<= thick <= .5:
        return 'Large_Envelope'
    if length > 24 or height > 18 or thick > .5 and length + 2*height + 2*thick <=84:
        return 'Package'
    if length > 24 or height > 18 or thick > .5 and 84 <= length + 2*height + 2*thick <=130:
        return 'Large_Package'
    else:
        return 'Unmailable'
 

def get_zone(zipcode):
    '''
    Determines the zone depending on the startzip and endzip 
        Arg:
            zipcode(int): series of numbers inputted by the user 
        Return:
            int: The classification of the zone:
                - 1
                - 2
                - 3
                - 4
                - 5
                - 6
                - -1
    '''

    if 1<=zipcode<=6999:
        return 1
    elif 7000<=zipcode<=19999:
        return 2
    elif 20000<=zipcode<=35999:
        return 3
    elif 36000<=zipcode<=62999:
        return 4
    elif 63000<=zipcode<=84999:
        return 5
    elif 85000<= zipcode <=99999:
        return 6
    else: 
        return -1

def get_distance(startzip, endzip):
    '''
    Calculates the zone difference between the startzip and the endzip
    Arg:
        startzip(int): Origional zipcode.
        endzip(int): Destination zipcode.
    Return:
        int: The  difference between the startzip and endzip.
             Returns -1 if either zipcode is invalid.
    '''


    startzone = get_zone(startzip)
    endzone = get_zone(endzip)

    if startzone == -1 or endzone == -1:
        return -1
    return abs(endzone - startzone)

def get_cost (post_type,distance):
    '''
    Calculates the total mailing cost based on mail type and zone distance.

    Arg:
        post_type (str): The category of mail
        distance (int): The zone difference 

    Returns:
        float or str:
            - The total mailing cost as a float (in dollars) if mailable,'Unmailable' if the post type or distance is invalid.
        
    '''
    if post_type =='Unmailable' or distance == -1:
        return 'Unmailable'
    elif post_type == 'Post_Card':
        return .2+ .03*distance
    elif post_type == 'Large_PostCard':
        return .37+ .03*distance
    elif post_type == 'Envelope':
        return .37+ .04*distance
    elif post_type == 'Large_Envelope':
        return .60+ .05*distance
    elif post_type == 'Package':
        return 2.95+ .25*distance
    elif post_type == 'Large_Package':
        return 3.95+ .35*distance
    else:
        return 'Unmailable'

def main():
    while True: 
        package = input('Enter your Mailing data (lenght, height, thickness, starzip, endzip)')
        package = package.split(",")
        length = float(package[0])
        height = float(package[1])
        thick = float(package[2])
        startzip = int(package[3])
        endzip = int(package[4])
    
        post_type = get_type(length,height,thick)
        distance = get_distance(startzip,endzip)
        cost = get_cost(post_type, distance)

        if cost == 'Unmailable':
            print('Unmailable')
        else:
            cost = f"{cost:.2f}" #converts cost to a string showing exactly two digits after the decimal point 
            cost = cost.lstrip('0')#removes zeros from the string 
            print(cost)


main()