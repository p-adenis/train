# Challenge TikTok  : 20 nombres aléatoires. CLassement croissant sans connaître les précédents nombres

import random

def main():

    nombres = {}

    for i in range(20):
        key = 'rang' + str(i)
        value = ''
        nombres[key] = value

        rand_numb = random.randint(0,1000)

        choice = input('Choose rang to put this number')
        
        if choice is not None:
            print(choice,rand_numb)
    

if __name__ == '__main__':
    main()