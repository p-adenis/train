# Challenge TikTok  : 20 nombres aléatoires. CLassement croissant sans connaître les précédents nombres

import random

def check_number(integer):
    if isinstance(integer,int) == 'True':
        return True
    else:
        return False
    
def initialise_dict():
    """
        Function to create and initialise an new empty dictionnary with 20 values
    """

    liste_nombre = {}

    for i in range(1,21):
        key = 'rang ' + str(i)
        value = ''
        liste_nombre[key] = value
    
    print(liste_nombre)
    
def main():

  
    initialise_dict()

    rand_numb = random.randint(0,1000)

    choice = input('Choose rank to put this number')


    if choice is not None and int(choice) in range(1,21):
        print(choice,rand_numb)
    else:
        print("Please choose a rank between [1-20] !! ")

if __name__ == '__main__':
    main()