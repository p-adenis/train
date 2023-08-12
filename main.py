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

if __name__ == '__main__':
    main()