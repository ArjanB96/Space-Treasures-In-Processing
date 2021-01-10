bg_index = 0
frame = 1
words = ''
screen = 1
opacity_x = 0
opacity_x_change = True
players = []

class Player:
    def __init__(self, name, cards = [], elements = []):
        self.name = name
        self.cards = cards
        self.elements = elements

def setup():
    size(1280,720)
    loadImages()

    
def draw():
    global bg_index, frame, words, opacity_x, opacity_x_change
    
    cycleBackground()  
    imageShow(home_img, home2_img, 10,10,130,55)
    
    #Vak waarin je username kan typen, pijl om naar volgende speler te gaan, en pijl om terug te gaan
    if screen != 6:
        image(leeg_vak, 400, 350, 480, 100) 
        image(verder_pijl, 890, 350, 100, 100)
        
        if len(words) == 0:
            image(verder_pijl_idle, 890, 350, 100, 100)
        if len(words) > 0:
            imageShow(verder_pijl, verder_pijl_hover, 890, 350, 100, 100)    
              
    if screen == 1:
        image(terug_pijl_idle, 290, 350, 100, 100)
        text('De speler met de hoogste\n dobbelscore is \'Speler 1\'', 640,625)
    elif screen != 6:
        imageShow(terug_pijl, terug_pijl_hover, 290, 350, 100, 100)
        
    # 'Start' knop als je minimaal twee spelers hebt ingevoerd
    
    if screen == 3 or screen == 4 or screen == 5:
        imageShow(start1, start2, 1105, 655, 165, 55)
        text('Druk op \'START\' om te spelen\nof voeg meer spelers toe', 640,625)
    if screen == 6:
        imageShow(start1, start2, 1105, 655, 165, 55)
        text('Druk op \'START\' om te spelen', 640,570)
        
    # 'Terug' knop, om naar vorige speler te gaan op het laatste scherm
    
    if screen == 6:
        imageShow(terug1, terug2, 10, 655, 165, 55)
            
    textSize(36)
    text(words, 370, 120, 540, 300)
    textFont(createFont('PressStart2P.ttf', 40))
    textAlign(CENTER, BOTTOM)
 
    if screen != 6:
        fill(255, 255, 255)
        text('Speler ' + str(screen), 640, 250)
        
        if len(words) >= 12:
            #image(leeg_vak, 254,625,760,100)
            text('Max. 12 karakters!', 640,700)
            
        if len(words) == 0:
            fill(255, 255, 255, opacity_x)
            if opacity_x == 0:
                opacity_x_change = True
            elif opacity_x == 250:
                opacity_x_change = False
            
            if opacity_x_change:
                opacity_x += 10
            elif not opacity_x_change:
                opacity_x -= 10
            text('|', 440, 420)
                    
        fill(255, 255, 255)
        text(str(len(words)) + ' / 12', 855,505)
        
    else:
        for i, player in enumerate(players):            
            text('Speler ' + str(i + 1) + ' is :   ', 340, 250 + i * 50)
            text(player.name, 800, 250 + i * 50)
            
def keyTyped():
    global words, screen
    
    if screen == 6:
        return
    
    if (key >= 'A' and key <= 'z') or key == ' ' and len(words) < 12:
        words += key     
    if len(words) == 13:
        words = words [:-1]        
    
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
        

def mousePressed():
    global screen, words, players
    
    #Verder/Start (vanaf min. twee spelers) 
    if (screen == 3 or screen == 4 or screen == 5) and isMouseOnButton(1105, 655, 165, 55) and len(words) == 0:
        screen = 6
            
    # Als je op -verder- drukt op scherm 3/4/5 en je hebt input staan in de box, ga naar scherm 6 en sla de input op als speler
    if (screen == 3 or screen == 4 or screen == 5) and isMouseOnButton(1070, 650, 195, 55) and len(words) > 0:
        screen = 6
        player = Player(words)
        players.append(player)
        words = '' 
        print([x.name for x in players])
        
    #Start knop
    if screen == 6 and isMouseOnButton(1070, 650, 165, 55):
        screen = 6             #Hayk's scherm
    
    #HOME button
    
    if screen != 1 and isMouseOnButton(10,10,130,55):
        screen = 1
        players = []
        words = '' 
            
    #Pijltje verder, zorg ervoor dat de lengte vd naam > 0 moet zijn
    if screen != 6 and isMouseOnButton(890, 350, 100, 100) and len(words) > 0:    
        screen += 1
        player = Player(words)
        players.append(player)
        words = ''
        print([x.name for x in players])
       
    #Pijltje terug
    if screen != 1 and screen != 6 and isMouseOnButton(290, 350, 100, 100):
        screen -= 1
        players.pop(screen - 1)
        words = ''
        
        #terug knop op scherm 6, bij 5 spelers, 4 spelers, 3 spelers en 2 spelers
        
    if screen == 6 and isMouseOnButton(10, 655, 165, 55) and len(players) == 5:
        screen -= 1
        players.pop(screen - 1)
        words = ''
    
    if screen == 6 and isMouseOnButton(10, 655, 165, 55) and len(players) == 4:
        screen -= 2
        players.pop(screen - 2)
        words = ''
      
    if screen == 6 and isMouseOnButton(10, 655, 165, 55) and len(players) == 3:
        screen -= 3
        players.pop(screen - 3)
        words = ''
        
    if screen == 6 and isMouseOnButton(10, 655, 165, 55) and len(players) == 2:
        screen -= 4
        players.pop(screen - 4)
        words = ''
    
        
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def loadImages(): 
    global background_images, home_img, dobbel_img, home2_img, verder_img, verder_pijl, verder_pijl_hover, terug_pijl, terug_pijl_hover, leeg_vak, verder_pijl_idle, terug_pijl_idle, start1, start2, terug1, terug2
    home_img = loadImage('images/Home.png')
    dobbel_img = loadImage('images/Dobbel.png')
    home2_img = loadImage('images/Home2.png')
    dobbel2_img = loadImage('images/Dobbel2.png')
    artifact_img = loadImage('images/Artefact.png')
    artifact2_img = loadImage('images/Artefact2.png')
    verder_img = loadImage('images/verder.png')
    verder_pijl = loadImage('images/PijlVerderPaars.png')
    verder_pijl_hover = loadImage('images/PijlVerder2Paars.png')
    verder_pijl_idle = loadImage('images/PijlVerderIdle.png')
    terug_pijl = loadImage('images/PijlTerugPaars.png')
    terug_pijl_hover = loadImage('images/PijlTerug2Paars.png')
    terug_pijl_idle = loadImage('images/PijlTerugIdle.png')
    leeg_vak = loadImage('images/LeegVak.png')
    start1 = loadImage('images/Start.png')
    start2 = loadImage('images/Start2.png')
    terug1 = loadImage('images/TerugKnop.png')
    terug2 = loadImage('images/TerugKnop2.png')
    
def imageShow(img, img2, x, y, wdth, hght, centered = False):
    if centered:
        imageMode(CENTER)
    else:
        imageMode(CORNER)
    if isMouseOnButton(x, y, wdth, hght, centered):
        image(img2, x, y, wdth, hght)
    else:
        image(img, x, y, wdth, hght)
