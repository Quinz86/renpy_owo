# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Donarin", who_color="#66aaaa", what_color="#66aaaa")
define x = Character("Xerzol", who_color="#772222", what_color="#772222")


#transforms
transform don:
    xalign 0.25
    yalign -1.0
    
transform forest:
    zoom 1.7
    


# The game starts here.

label start:

    # https://www.renpy.org/doc/html/quickstart.html
    
    scene bg woods at forest, truecenter
    
    show donarin stab at don
    
    x "hello world!"

menu:
    "Stab":
        jump stabbed
    "Do not stab":
        jump fine
        
label stabbed:

    d "*stabs you*"
    x "I cant belive youve done this"
    jump merge
    
label fine:

    x "Im glad you didnt stab me"
    
label merge:
    
    x "this is the end"
    

    return
