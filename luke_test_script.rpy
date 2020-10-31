# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chris", who_color="#66aaaa", what_color="#66aaaa")
define cq = Character("???", who_color="#66aaaa", what_color="#66aaaa")
define g = Character("Gilby Cross", who_color="#d9210d", what_color="#d9210d")
define gq = Character("???", who_color="#d9210d", what_color="#d9210d")
define pov = Character("[povname]", who_color="#a89445", what_color="#a89445")

image goatChris = "goatChris.png"
image forestbg = "forestbg.png"
image gilby = "gilby.jpg"
image volcanobg = "volcanobg.jpg"


#transforms
transform goatChris:
    xalign 0.25
    yalign 2.0

transform gilby:
    xalign 0.75
    yalign -1.0

transform forestbg:
    zoom 0.25
    
transform volcanobg:
    zoom 1.7

# The game starts here.

label start:

    # https://www.renpy.org/doc/html/quickstart.html
    python:
        flag_forest = 0
        flag_volcano = 0
        flag_rice = 0

    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "Philip Chumbo"

    scene forestbg at forestbg, truecenter

    pov "My name is [povname], a student of the magical arts."
    pov "My latest task is to wander in the magical lands and talk to any interesting creatures I may find."
    pov "Where should I go?"

menu:
    "Magical Forest":
        jump forest
    "Volcano":
        jump volcano
    "Exit":
        jump earlyExit


label earlyExit:
    pov "You know what? Fuck this assignment! I'm going home and playing Warframe."
    jump end


label forest:
    $ flag_forest = 1
    scene forestbg at forestbg, truecenter
    "You walk over hills and under hills until you reach the magical forest"
    pov "Hey look, a satyr!"

    show goatChris

    c "Hey there, I'm Chris. I would ask if you wanted to have a picnic, but I don't have any food on me?"

menu:
    "Sure! I brought rice!" if flag_rice == 1:
        jump picnic
    "Sorry, I don't have any food.":
        jump noPicnic

label picnic:
    c "Oh sweet! Thanks for the rice!"
    c "I would have brought pasta, but the only kind they had at the store had sauce in it..."
    c "Anyways, should we start eating?"

    "Chris sits on a stump and grabs a bowl of rice"
    "He then proceeds to eat. He takes three bites and stands up on the stump"

    c "Thanks for sharing with me, I enjoyed it a lot"
    c "Anyways, I got class soon. We are learning about making visual novels in RenPy!"

    hide goatChris

    "Chris leaps off the stump and playfully trots away into the forest"

    jump merge
    
label noPicnic:

    c "aww, that's too bad..."
    c "I was really hoping to have a good time and hang out as buddies you know?"
    c "Maybe get to know each other, eat some rice, program some assignments..."
    c "All well, if you need me just push a picnic invitation onto my github repository."

    hide goatChris

    "Chris leaves"

    pov "Well, that was strange... Hopefully I can find more creatures for this assignment. "

    jump merge



label volcano:
    scene volcanobg at volcanobg, truecenter
    $ flag_volcano = 1
    pov "Wow, it's super warm here. I wonder what sort of creatures live around here!"
    gq "Hey there!"
    pov "huh?"
    "You look around and notice a red man holding a box"

    show gilby

    gq "Could you give me a hand?!"
    "He seems to be struggling a lot"

menu:
    "Give hand":
        jump giveHand
    "Watch him suffer":
        jump suffer


label giveHand:
    pov "Here, let me help you with that."
    "You grab the box from his hands... Surprisingly, it is not heavy at all."
    gq "Whew! Thanks for helping me out with that."
    pov "uhh, sure I guess..."
    gq "I'm Gilby Cross!"
    "He flaunts his cloak"
    g "At your service!"
    pov "Oh wow, you are pretty flashy."
    g "The flashiest!"
    g "I was just going to throw that box of rice in the volcano over there. You want it?"
menu:
    "Take rice":
        $flag_rice = 1
        pov "I'll take the rice, thank you!"
        "Gilby hands you the rice!"
        jump gilby_continue
    "No thanks.":
        pov "No thanks."
        jump gilby_continue

label gilby_continue:
    pov "I'm here to write an assignment on interesting creatures. You wouldn't know where I could find any, would you?"
    g "No need to play coy with me. Of course I will let you write about me!"
    pov "umm... What?"
    g "I've been waiting for someone to write about my exploits in defeating the horseman of death!"
    pov "..."
    "You start slowly backing away. Gilby doesn't seem to notice"
    g "You see, back when myself and Pajaro were..."
    "You escaped successfully!"
    jump merge





label suffer:
    "You monster!"
    gq "Uhnn, oh no!"
    "His knees buckle under the weight of the box and he tumbles to the ground"
    gq "sigh, I *gasp* the great *gasp*"
    "He takes a second to catch his breath"
    gq "...The great Gilby Cross has been defeated..."
    pov "Gilby Cross?"
    g "WHAT!? You haven't heard of the great Gilby Cross??"
    g "Why I slayed the great evil Harroc horseman of Death myself and saved the entire world!"
    pov "...really?"
    g "I know, I know. You are stunned from meeting your hero in the flesh"
    "He flashes a smile, showing a snag tooth"
    g "I the great Gilby Cross is here!"
    "He strikes a heroic pose, displaying his biceps"
    pov "Umm, I'm just going to leave now"
    g "No wait come back!!"
    "You leave before any more nonsense happens. I mean, what even is a Harroc?"
    hide gilby
    jump merge





label merge:
    "Where to next?"
menu:
    "Forest":
        jump forest
    "Volcano":
        jump volcano
    "Exit":
        jump end


label end:
    "end game"
    return
