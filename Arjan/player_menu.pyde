bg_index = 0
frame = 1
words = ''
screen = 1

def setup():
    size(1280,720)
    
def draw():
    global bg_index, frame
    
    cycleBackground()
    image(loadImage('images/Home.png'), 10, 10, 130, 55)
        
    #Vak waarin je username kan typen
    
    if screen == 1 or screen == 2 or screen == 3 or screen == 4 or screen == 5:
        image(loadImage('images/LeegVak.png'), 400, 350, 480, 100) 
        
    #Pijltje waarmee je naar volgende naam kan:
    if screen == 1 or screen == 2 or screen == 3 or screen == 4 or screen == 5: 
        image(loadImage('images/verder.png'), 880, 350, 100, 100)
        
    #Pijltje waarmee je naar vorige naam kan:
        
    if screen == 1:
        image(loadImage('images/terug_grijs.png'), 300, 350, 100, 100)
    if screen == 2 or screen == 3 or screen == 4 or screen == 5:
        image(loadImage('images/terug.png'), 300, 350, 100, 100)
        
    textSize(36)
    text(words, 370, 120, 540, 300)
    textFont(createFont('PressStart2P.ttf', 40))
    textAlign(CENTER, BOTTOM) 
 
    if screen == 1:
        text('Player 1', 640, 250)
        if len(words) > 10:
            text('Max 12 characters!', 640,550)
    elif screen == 2:
        text('Player 2', 640, 250)
        if len(words) > 10:
            text('Max 12 characters!', 640,550)
    elif screen == 3:
        text('Player 3', 640, 250)
        if len(words) > 10:
            text('Max 12 characters!', 640,550)
    elif screen == 4:
        text('Player 4', 640, 250)
        if len(words) > 10:
            text('Max 12 characters!', 640,550)
    elif screen == 5:
        text('Player 5', 640, 250)
        if len(words) > 10:
            text('Max 12 characters!', 640,550)
    elif screen == 6:
        text('Player 1 is :   ',340,250)
        text(player1, 800, 250)
        text('Player 2 is :   ',340,300)
        text(player2, 800, 300)
        text('Player 3 is :   ',340,350)
        text(player3, 800, 350)
        text('Player 4 is :   ',340,400)
        text(player4, 800, 400)
        text('Player 5 is :   ',340,450)
        text(player5, 800, 450)
            
def keyTyped():
    global letter, words, screen, player1, player2, player3, player4, player5
    if ((key >= 'A' and key <= 'z') or key == ' '):
        if len(words) <= 12:
            letter = key
            words = words + key
            println(key)
        if len(words) > 12:
            words = ''    
        
        #Backspace
        
    if (key == BACKSPACE):
        letter = key
        words = words[:-1]
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
        
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  global screen, player1, player2, player3, player4, player5, words  
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def mousePressed():
    global screen, player1, player2, player3, player4, player5, words
    
    #EXIT button
    
    if screen == 2 or screen == 3 or screen == 4 or screen == 5 or screen == 6:
        if isMouseOnButton(10,10,130,55):
            screen = 1
            
    #Pijltje verder, zorg ervoor dat de lengte vd naam >0 moet zijn en dat de variable wordt gemaakt  
    
    if len(words) > 0 and screen == 1:
        if isMouseOnButton(880, 350, 100, 100):
            screen = screen + 1
            player1 = words
            words = ''
    elif len(words) > 0 and screen == 2:
        if isMouseOnButton(880, 350, 100, 100):
            screen = screen + 1
            player2 = words
            words = ''    
    elif len(words) > 0 and screen == 3:
        if isMouseOnButton(880, 350, 100, 100):
            screen = screen + 1
            player3 = words
            words = ''
    elif len(words) > 0 and screen == 4:
        if isMouseOnButton(880, 350, 100, 100):
            screen = screen + 1
            player4 = words
            words = ''
    elif len(words) > 0 and screen == 5:
        if isMouseOnButton(880, 350, 100, 100):
            screen = screen + 1
            player5 = words
            words = ''
    
    #Pijltje terug, werkt niet op screen 1 
    
    if  screen == 2 or screen == 3 or screen == 4 or screen == 5:
        if isMouseOnButton(300, 350, 100, 100):
            screen = screen - 1
            words = ''
            
