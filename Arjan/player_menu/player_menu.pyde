bg_index = 0
frame = 1
words = ''
screen = 1

players = []

class Player:
    def __init__(self, name, cards = [], elements = []):
        self.name = name
        self.cards = cards
        self.elements = elements

def setup():
    size(1280,720)
    
def draw():
    global bg_index, frame, words
    
    cycleBackground()
    
    loadImages()   
    
    image(home_img, 10, 10, 130, 55)
        
    #Vak waarin je username kan typen
    if screen != 6:
        image(loadImage('images/LeegVak.png'), 400, 350, 480, 100) 
        image(loadImage('images/PijlVerder.png'), 880, 350, 100, 100)
        if len(words) == 0:
            image(loadImage('images/PijlVerderIdle.png'), 880, 350, 100, 100)
        
    
        
    #Pijltje waarmee je naar vorige naam kan:  
              
    if screen == 1:
        image(loadImage('images/PijlTerugIdle.png'), 300, 350, 100, 100)
    elif screen != 6:
        image(loadImage('images/PijlTerug.png'), 300, 350, 100, 100)
        
    # 'Verder' knop als je minimaal twee spelers hebt ingevoerd
    
    if screen == 3 or screen == 4 or screen == 5:
        image(loadImage('images/VerderKnop.png'), 1070, 650)
        
    if screen == 6:
        image(loadImage('images/Start.png'), 1070, 650)
        
    textSize(36)
    text(words, 370, 120, 540, 300)
    textFont(createFont('PressStart2P.ttf', 40))
    textAlign(CENTER, BOTTOM)
 
    if screen != 6:
        text('Player ' + str(screen), 640, 250)
        if len(words) == 0 and key == ENTER:
            text('Min 1 character!', 640,550)
            
        if len(words) >= 11:
            text('Max 12 characters!', 640,550)
        if len(words) == 12:
            words = ''
    else:
        for i, player in enumerate(players):            
            text('Player ' + str(i + 1) + ' is :   ', 340, 250 + i * 50)
            text(player.name, 800, 250 + i * 50)
            
def keyTyped():
    global words, screen
    
    if screen == 6:
        return
    
    if (key >= 'A' and key <= 'z') or key == ' ' and len(words) < 12:
        words += key             
    
    #Backspace
    if key == BACKSPACE:
        words = words[:-1]
   
    #Enter, druk op enter om naar volgende scherm te gaan

    if key == ENTER and len(words) > 0:
        player = Player(words)
        players.append(player)
        
        screen += 1
        words = ''
        
        print([x.name for x in players])
        
        
def cycleBackground():
    global bg_index, frame    
    frame = frame + 1 if frame < 60 else 1
    if frame % 2 == 0:
        background(loadImage('background/bg' + str(bg_index) + '.jpg'))
        bg_index = bg_index + 1 if bg_index < 32 else 0
        
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def mousePressed():
    global screen, words, players
    
    #Verder (vanaf min. twee spelers)
    
    if (screen == 3 or screen == 4 or screen == 5) and isMouseOnButton(1070, 650, 195, 55):
        screen = 6
    
    #Start knop
    
    if screen == 6 and isMouseOnButton(1070, 650, 165, 55):
        screen = 6             #Hayk's scherm
    
    #HOME button
    
    if screen != 1 and isMouseOnButton(10,10,130,55):
        screen = 1
        players = []
        words = '' 
            
    #Pijltje verder, zorg ervoor dat de lengte vd naam > 0 moet zijn
    if screen != 6 and isMouseOnButton(880, 350, 100, 100) and len(words) > 0:    
        screen += 1
        player = Player(words)
        players.append(player)
        words = ''
        print([x.name for x in players])
       

    #Pijltje terug
    if screen != 1 and screen != 6 and isMouseOnButton(300, 350, 100, 100):
        screen -= 1
        players.pop(screen - 1)
        words = ''

    
def mouseHoverHandler():
    if isMouseOnButton(10, 10, 130, 55): # Home button
        image(home2_img, 10, 10, 130, 55)
        cursor(HAND)

# VERWIJDEREN ALS JE GAAT MERGEN
def loadImages(): 
    global background_images, home_img, dobbel_img, home2_img, verder_img
    home_img = loadImage('images/Home.png')
    dobbel_img = loadImage('assets/buttons/Dobbel.png')
    home2_img = loadImage('assets/buttons/Home2.png')
    dobbel2_img = loadImage('assets/buttons/Dobbel2.png')
    artifact_img = loadImage('assets/buttons/Artefact.png')
    artifact2_img = loadImage('assets/buttons/Artefact2.png')
    verder_img = loadImage('assets/buttons/Verder.png')
