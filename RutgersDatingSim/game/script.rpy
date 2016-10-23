## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

##characters##
#major characters
define o = Character('Olivia')
define a = Character('Avery')
define b = Character('Butch')
define c = Character('Cadee')

#side characters

#minor/ faceless characters
define professor = Character('Professor')

##define images

#backgrounds
image collegeAve1 = "bg_CollegeAve1.jpg"
image collegeAve2 = "bg_CollegeAve2.jpg"
image collegeAve3 = "bg_CollegeAve3.jpg"
image collegeAveN1 = "bg_CollegeAveNight1.jpg"
image collegeAveN2 = "bg_CollegeAveNight2.jpg"

image busch1 = "bg_Busch1.jpg"
image busch2 = "bg_Busch2.jpg"
image busch3 = "bg_Busch3.jpg"

image cook1 = "bg_Cook1.jpg"
image cook2 = "bg_Cook2.jpg"
image cookN1 = "bg_CookNight1.jpg"
image cookN2 = "bg_CookNight2.jpg"
image douglass1 = "bg_Douglass1.jpg"
image douglass2 = "bg_Douglass2.jpg"

image livi1 = "bg_Livi1.jpg"
image livi2 = "bg_Livi2"
image liviN1 = "bg_LiviNight1.jpg"
image liviN2 = "bg_LiviNight2.jpg"
image liviN2 = "bg_LiviNight2.jpg"

image class1 = "bg_Class1"
image library1 = "bg_library1"
image theater1 = "bg_Theater1.jpg"

#characters
image oliviaSpeaking1 = "olivia_speaking1.png"
image oliviaHappy2 = "olivia_happy2.png"


## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene collegeAve1

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show oliviaSpeaking1


    ## These display lines of dialogue.

    "Hello, world."

    o "You've created a new Ren'Py game."
    
    hide oliviaSpeaking1
    show oliviaHappy2
    o "Once you add a story, pictures, and music, you can release it to the world!"

    ## This ends the game.

    return
