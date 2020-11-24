bg_index = 0
frame = 1
words = ''

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
    
    
    
    
    
def keyTyped():
    global letter, words
    if ((key >= 'A' and key <= 'z') or key == ' '):
        letter = key
        words = words + key
        println(key)
        
        #Backspace in progress, werkt nog niet zoals die moet :p
    if (key == BACKSPACE):
        letter = key
        words = words + '#'
        println(key)
        
        #Enter in progress, moet zorgen dat er een variable wordt aangemaakt met spelersnaam
    if (key == ENTER):
        letter = key
        words = words + key + 'poop'
        println(key)
        
        
