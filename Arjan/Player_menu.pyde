bg_index = 0
frame = 1
words = ''
screen = 1

def setup():
    size(1280,720)

def draw():
    global bg_index, frame
    
    cycleBackground()
    
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
        text('Player 1 is : ',340,250)
        text(player1, 800, 250)
        text('Player 2 is : ',340,300)
        text(player2, 800, 300)
        text('Player 3 is : ',340,350)
        text(player3, 800, 350)
        text('Player 4 is : ',340,400)
        text(player4, 800, 400)
        text('Player 5 is : ',340,450)
        text(player5, 800, 450)
        
def keyTyped():
    global letter, words, screen, player1, player2, player3, player4, player5
    if ((key >= 'A' and key <= 'z') or key == ' '):
        letter = key
        words = words + key
        println(key)
        
        #Backspace, als je op backspace drukt verwijder je nu je hele input
    if (key == BACKSPACE):
        letter = key
        words = ''
        println(key)
        
        #Enter, druk op enter om naar volgende scherm te gaan en de naam op te slaan in een variable
    if (key == ENTER):
        letter = key
        println(key)
        
        if screen == 1:
            player1 = words
            screen = screen + 1
            words = ''
        elif screen == 2:
            player2 = words
            screen = screen + 1
            words = ''
        elif screen == 3:
            player3 = words
            screen = screen + 1
            words = ''
        elif screen == 4:
            player4 = words
            screen = screen + 1
            words = ''
        elif screen == 5:
            player5 = words
            screen = screen + 1
            words = ''
            print(player1, player2, player3, player4, player5)


def cycleBackground():
    global bg_index, frame    
    frame = frame + 1 if frame < 60 else 1
    if frame % 2 == 0:
        background(loadImage('background/bg' + str(bg_index) + '.jpg'))
        bg_index = bg_index + 1 if bg_index < 32 else 0
        
