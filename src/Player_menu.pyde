bg_index = 0
frame = 1
words = ''
screen = 1

def setup():
    size(1280,720)

def draw():
    global bg_index, frame
    
    frame = frame + 1 if frame < 60 else 1
    if frame % 2 == 0:
        background(loadImage('background/bg' + str(bg_index) + '.jpg'))
        bg_index = bg_index + 1 if bg_index < 32 else 0
        
    textSize(36)
    text(words, 50, 120, 540, 300)
    textFont(createFont('PressStart2P.ttf', 40))
    textAlign(CENTER, BOTTOM)
    
    if screen == 1:
        text('Player 1', 640, 250)
    elif screen == 2:
        text('Player 2', 640, 250)
    elif screen == 3:
        text('Player 3', 640, 250)
    elif screen == 4:
        text('Player 4', 640, 250)
    elif screen == 5:
        text('Player 5', 640, 250)
    elif screen == 6:
        text('bruh', 640, 250)
        
    
def keyTyped():
    global letter, words, screen, player1, player2, player3, player4, player5
    if ((key >= 'A' and key <= 'z') or key == ' '):
        letter = key
        words = words + key
        println(key)
        
        #Backspace in progress, werkt nog niet zoals die moet :p
    if (key == BACKSPACE):
        letter = key
        words = ''
        println(key)
        
        #Enter in progress, moet zorgen dat er een variable wordt aangemaakt met spelersnaam
    if (key == ENTER):
        letter = key
        println(key)
        
        if screen == 1:
            player1 = words
        elif screen == 2:
            player2 = words
        elif screen == 3:
            player3 = words
        elif screen == 4:
            player4 = words
        elif screen == 5:
            player5 = words
            print(player1, player2, player3, player4, player5)

        
        

        #Als er op enter gedrukt wordt, wordt naam opgeslagen in variable en wordt er gevraagd voor de volgende player input
    if (key == ENTER):
        screen = screen + 1
        words = ''
        
        
