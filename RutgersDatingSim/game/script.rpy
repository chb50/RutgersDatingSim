## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

##characters##

#major characters
define o = Character(_('Olivia'), color = "#3366ff")
define a = Character('Avery')
define b = Character(_('Butch'), color = "#ff5050")
define c = Character(_('Cadee'), color = "#009933")

#side characters

#minor/ faceless characters
define professor = Character('Professor')

##define images

#backgrounds
image bg collegeAve1 = "bg_CollegeAve1.jpg"
image bg collegeAve2 = "bg_CollegeAve2.jpg"
image bg collegeAve3 = "bg_CollegeAve3.jpg"
image bg collegeAveN1 = "bg_CollegeAveNight1.jpg"
image bg collegeAveN2 = "bg_CollegeAveNight2.jpg"

image bg busch1 = "bg_Busch1.jpg"
image bg busch2 = "bg_Busch2.jpg"
image bg busch3 = "bg_Busch3.jpg"

image bg cook1 = "bg_Cook1.jpg"
image bg cook2 = "bg_Cook2.jpg"
image bg cookN1 = "bg_CookNight1.jpg"
image bg cookN2 = "bg_CookNight2.jpg"
image bg douglass1 = "bg_Douglass1.jpg"
image bg douglass2 = "bg_Douglass2.jpg"

image bg livi1 = "bg_Livi1.jpg"
image bg livi2 = "bg_Livi2.jpg"
image bg liviN1 = "bg_LiviNight1.jpg"
image bg liviN2 = "bg_LiviNight2.jpg"
image bg liviN2 = "bg_LiviNight2.jpg"

image bg class1 = "bg_Class1.jpg"
image bg library1 = "bg_library1.jpg"
image bg theater1 = "bg_Theater1.jpg"
image bg lab1 = "bg_Lab1.jpg"

#olivia
image olivia Speaking1 = "olivia_speaking1.png"
image olivia Speaking2 = "olivia_speaking2.png"
image olivia Happy2 = "olivia_happy2.png"
image olivia Angry1 = "olivia_angry1.png"

#avery
image avery Happy1Glasses = "avery_happy1glasses.png"

#cadee
image cadee Happy1 = "cadee_happy1.png"
image cadee Happy2 = "cadee_happy2.png"
image cadee Worried1 = "cadee_worried1.png"
image cadee Crazy1 = "cadee_crazy1.png"

#butch
image butch Neutral1 = "butch_neutral1.png"
image butch Neutral2 = "butch_neutral2.png"
image butch Happy1 = "butch_happy1.png"
image butch Happy2 = "butch_happy2.png"
image butch Confused1 = "butch_confused1.png"
image butch Confused2 = "butch_confused2.png"
image butch Thinking1 = "butch_thinking1.png"
image butch Thinking2 = "butch_thinking2.png"
image butch Worried1 = "butch_worried1.png"

#player character
define user = Character(_("[userName]"), color = "#ff9900")

## The game starts here.

label start:
    
    #stop config.main_menu_music
    #with Dissolve(.5)
    ##BEGIN PROLOGUE##
    
    scene black
    
    "{i}Welcome to the Rutgers Love-iversity program!{/i}"
    
    "{i}As part of our program, we will not only supplement you with a quality education,{/i}"
    
    "{i}As part of our program, we will not only supplement you with an education,{/i}"
    
    "{i}\As part of our program, we will not only supplement you with an education, but with an environment to find passion for others.{/i}"
    
    scene bg collegeAve1
    with Dissolve(.5)

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show butch Happy2
    with Dissolve(.5)

    
    ## These display lines of dialogue.

    b "Hi, everyone! I’m your orientation leader, Butch! Let’s do a quick icebreaker to get to know each other!"
    
    "{i}All students groan.{/i}"
    
    show butch Confused1
    
    b "Umm... ok. You, over there. Come on, why don’t you start?"
    
    "{i}All eyes turn to you.{/i}"
    
    python:
        userName = renpy.input("What is your name?")
        userName = userName.strip()
        
        if not userName:
            userName = "Loser"
    
    "What is your major?"
    menu:
        "Engineering":
            jump engineer
        
        "Business":
            jump business
        
        "Exercise Science":
            jump eScience
        
        "Undecided":
            jump undec
    
    #flags choose route
    label engineer:
        user "Um, my Name Is [userName] and I'm majoring in engineering."
        $ isEngineer = True
        $ isBusiness = False
        $ isESci = False
        $ isUndec = False
        jump charIntro
    label business:
        user "Um, my Name Is [userName] and I'm majoring in business."
        $ isEngineer = False
        $ isBusiness = True
        $ isESci = False
        $ isUndec = False
        jump charIntro
    label eScience:
        user "Um, my Name Is [userName] and I'm majoring in Exercise Science."
        $ isEngineer = False
        $ isBusiness = False
        $ isESci = True
        $ isUndec = False
        jump charIntro
    label undec:
        user "Um, my Name Is [userName] and I don't know what I wanna major in."
        $ isEngineer = False
        $ isBusiness = False
        $ isESci = False
        $ isUndec = True
        jump charIntro
    
    label charIntro:
        #dont need anything within this clause
    show butch Happy1
    
    b "Well, [userName], it's nice to meet you!"
    
    b "Well, next up is ..."
    
    hide butch Happy1
    show olivia Speaking2
    o "Olivia, Business and I don’t have time to make friends."
    
    hide olivia Speaking2
    show butch Confused1
    b "Err, well yes... okay then... next is..."
    
    hide butch Confused1
    show avery Happy1Glasses
    a "Aaaaaayyyyy. LMAO! I’m Avery. I’m studying Exercise Science. Whoooooo! ;)"
    
    hide avery Happy1Glasses
    show butch Neutral2
    b "Yes, well... A bit excessive, but regardless, nice to meet you."
    
    hide butch Neutral2
    show butch Happy1
    b "And last but not least, we have..."
    
    hide butch Happy1
    show cadee Worried1
    c "..."
    
    hide cadee Worried1
    show olivia Angry1
    o "Would you answer the man so I can go home?"
    
    hide olivia Angry1
    show cadee Crazy1
    c "!"
    
    hide cadee Crazy1
    show cadee Happy1
    c "O..Oh, Hello. I’m Cadee. My major is ???."
    
    hide cadee Happy1
    show olivia Speaking1
    o "What is {i}that{/i} supposed to mean?"
    
    hide olivia Speaking1
    show cadee Worried1
    c "..."
    
    c "I’m not like the other kids."
    
    hide cadee Worried1
    show butch Worried1
    b "Well then, Cadee, it's nice to meet you as well..."
    
    show butch Happy1
    b "With that done, shall we start our little tour of the campus?"

    hide butch
    scene black
    with Dissolve(.5)
    
    scene bg collegeAve2
    with Fade(.5,0.0,0.5)
    
    pause 1.5
    
    scene bg busch2
    with Fade(.5,0.0,0.5)

    pause 1.5
    
    show bg livi1
    with Fade(.5,0.0,.5)
    
    pause 1.5
    
    show bg douglass1
    with Fade(.5,0.0,.5)
    
    pause 1.5
    
    scene black
    with Dissolve(.5)
    
    "I don’t really know anybody that well…"
    
    "But I’m excited to start school in the fall!"
    
    " "
    
    #END PROLOGUE
    
    if isEngineer:
        jump butchroute
    
    ##BUTCH ROUTE (ROUTE H)##
    #BEGIN SCENE 1
        
    label butchroute:
    
    #Fade out music
    #Add in school bell sound
    
    "{i}A couple of months later...{/i}"
    scene bg busch1
    with Dissolve(.5)
    
    #Start new music
    
    "I have my first lab class today. Let’s see… it’s called…"

    "...Physical analysis of hyperdynamic thermonuclear fluid plasma synthesis I."
    
    "..."
    
    "I have to take a part two of this class?!?!"
    
    "Maybe I shouldn’t have gone into engineering..."

    "But I still have some time before class. What should I do?"
    
    menu:
        "Get something to eat":
            jump eat
        "Go to the library":
            jump library
        "Take a nap":
            jump nap
    
    label eat:
        scene black
        with Dissolve(.5)
        "{i}You grab a bite to eat.{/i}"
        scene bg busch1
        with Dissolve(.5)
        "Mmmm... that hit the spot!"
        jump panic
    label library:
        scene black
        with Dissolve(.5)
        "{i}You go to the library to fry your brain a bit.{/i}"
        scene bg busch1
        with Dissolve(.5)
        "Ugh.... I did so much studying... but didn't learn a thing."
        jump panic
    label nap:
        scene black
        with Dissolve(.5)
        "{i}You catch some much needed zzzzs.{/i}"
        scene bg busch1
        with Dissolve(.5)
        "Ahhh... That nap was nice!"
        jump panic
    
    label panic:
        "...."
        "...."
        "AHHHHHHH!!! WHAT TIME IS IT?!?!"
        "Oh no! I have to get to class!"
    
    scene black
    with Dissolve(.5)
    
    #END SCENE 1
    "{i}You rush to class.{/i}"
    
    #BEGIN SCENE 2
    scene bg busch3
    with Dissolve(.5)
    
    "Okay, I think my class is just around the corner!"
    
    #MAKE SCREEN SHAKE##
    scene bg busch3
    with Fade(.1, 0, .1, color="#fff") #flash effect
    show butch Confused1
    
    user "OOF!!"
    
    show butch Neutral1
    user "Ahhh! I'm sorry!"
    
    b "..."
    
    user "Uhh... okay then..."
    
    "Hmm this guy seems familiar... Ah! Right, I gotta get to class!"
    
    "{i}You both walk in the same direction awkwardly. You don’t know what to say, but he follows you all the way to your class.{/i}"
    
    user "Hey!"
    
    show butch Confused1
    
    b "!"
    
    user "Why are you following me, creep?!"
    
    show butch Neutral1
    
    b "Oh…"
    
    user "Wait… do you have class here too?"
    
    b "Sort of…"
    
    b "I'm the TA for this class."
    
    "Ah! well... that's awkward..."
    
    user "Oh... okay then."
    
    scene black
    with Dissolve(.5)
    
    #END SCENE 2
    
    "{i}All throughout class, you feel awkward. Afterwards, you go up to ask a question reluctantly.{/i}"
    
    #BEGIN SCENE 3
    scene bg lab1
    with Dissolve(.5)
    
    "I have a question, but… I feel really awkward… maybe I should just try to figure it out myself."
    
    "What should I do?"
    
    menu:
        "Ask Butch your question.":
            jump question
        "Try to figure it out yourself.":
            jump noquestion
    
    label noquestion:
        "Well, I'm sure with some time I'll understand the material."
        ##this route will be changed to allow the player to chose another route
        "{i}You failed your class and dropped out of school, thus becoming a bum for all eternity.{/i}"
        jump end
    label question:
        "Well, I get nothing out of avoiding him, so I might as well ask."
    
    user "Um…"
    
    show butch Neutral1
    with Dissolve(.5)
    
    b "Oh, hi."
    
    user "I have a question…"
    
    b "What’s your question?"
    
    label back2question:
    
    menu:
        "Is the graph of stochastic flow intervals of the hydrogen-based hyper-plasma 
         fluid related to the electric potential of the metallic material used to construct the plasmas 
         for the damping converter entities?":
            jump quest1
        "What’s the name of this class, again?":
            jump quest2
        "Want to go on a date?":
            jump quest3
    
    label quest2:
        user "What’s the name of this class, again?"
        
        b "Physical analysis of hyperdynamic thermonuclear fluid plasma synthesis I."
        
        user "What… is that?"
        
        show butch Thinking1
        
        b "..."
        
        user "..."
        
        b "...I don’t really know."
        
        user "Aren’t you the TA? How do you not know what this class is for?"
        
        b "Honestly… I’m doing so many other projects right now that I haven’t really studied up on this in a while."
        
        "Can you really be a TA for a class you don’t remember?!"
        
        show butch Neutral1
        
        b "Well, I’ll look it over tonight before practice."
        
        "How can you learn a whole semester’s worth of information in one night?"
        
        b "Anything else?"
        
        jump back2question
    
    label quest3:
        
        user "Want to go on a date?"
        
        b "Oh. The date is September 9th."
        
        user "No, I’m not asking for the date. I’m asking you on a date."
        
        b "You’re asking me… on September 9th? What are you asking me?"
        
        user "I’m asking… do you have plans later?"
        
        b "I have practice in an hour, so I’ll only be available for questions now."
        
        "He doesn’t seem to get it…"
        
        b "Anything else?"
        
        jump back2question
    
    label quest1:
        
        user "Is the graph of stochastic flow intervals of the hydrogen-based hyper-plasma 
              fluid related to the electric potential of the metallic material used to construct 
              the plasmas for the damping converter entities?"
        
        b "No."
        
        user "..."
        
        b "..."
        
        user "..."
        
        show butch Thinking1
        
        b "I can see why you’d think that, though."
        
        user "Huh?"
        
        show butch Happy1
        
        b "After all, the classical electrodynamic model seems to indicate particularly high Lorentz 
           forces on electrical particles could create a field that affects hyper-plasma when experiencing hydrostatic pressure."
        b "However, Newtonian mechanics is widely considered irrelevant for this case, so we have to turn to quantum field theory in order to..."
        
        scene black
        with Dissolve(.5)
        
        "{i}Butch goes on and on. You try to understand, but it's like he's speaking another language.{/i}"
        
        scene bg lab1
        with Dissolve(.5)
        
        show butch Neutral1
        
        b "Does that answer your question?"
        
        user "Yeah, I... think I get it now..."
        
        "My brain hurts..."
        
        show butch Worried1
        b "If you’re still struggling with this, you can always come to office hours on Wednesdays."
        
        user "Yeah… I think I’ll do that."
        
        b "Cool. I’ll see you then. I have practice soon, so I have to go."
        
        user "Oh. Thanks, bye!"
        
        show butch Happy2
        b "See ya!"
    
    #END SCENE 3
    
    

    ## This ends the game.
    
    label end:
    
    return
