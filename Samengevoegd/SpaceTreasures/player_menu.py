import main_game, globals

bg_index = 0
frame = 1
words = ''
screen = 1
opacity_x = 0
opacity_x_change = True
players = globals.players

class Player:
    def __init__(self, name, cards = [], elements = []):
        self.name = name
        self.cards = cards
        self.elements = elements

def setup():
    loadImages()

def draw():
    global bg_index, frame, words, opacity_x, opacity_x_change, count
    
    players = globals.players
    
    cycleBackground()  
    mouseHoverHandler()
    imageShow(home_img, home2_img, 10,10,130,55)
    
    #Vak waarin je username kan typen, pijl om naar volgende speler te gaan, en pijl om terug te gaan
    if screen != 6:
        image(leeg_vak, 400, 350, 480, 100) 
        image(verder_pijl, 890, 350, 100, 100)
        
        if (len(words) == 0 and screen - 1 == len(players)) or screen == len(players):
            image(verder_pijl_idle, 890, 350, 100, 100)
        if len(words) > 0:
            imageShow(verder_pijl, verder_pijl_hover, 890, 350, 100, 100)    
              
    if screen == 1:
        image(terug_pijl_idle, 290, 350, 100, 100)
        if len(players) < 2:
            textSize(36)
            text('De speler met de hoogste\n dobbelscore is \'Speler 1\'', 640,625)
    elif screen != 6:
        imageShow(terug_pijl, terug_pijl_hover, 290, 350, 100, 100)
        
    # 'Start' knop als je minimaal twee spelers hebt ingevoerd
    
    if len(players) >= 2 and screen != 6:
        imageShow(start1, start2, 1105, 655, 165, 55)
        text('Druk op \'START\' om te spelen\nof voeg meer spelers toe', 640,625)
    elif screen == 6:
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
    global words, screen, players
    
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
        if screen <= len(players):
            player.cards = list([x for x in players[screen - 1].cards])
            players[screen - 1] = player
        else:
            players.append(player)
        screen += 1
        words = players[screen - 1].name if screen <= len(players) else ''
        
interval = 250
        
def cycleBackground():
    global bg_index, interval, play_stars_animation
    
    if interval <= 0:
        if bg_index < len(background_animation_images):            
            background(background_animation_images[bg_index])
            bg_index += 1
            if bg_index == 13:
                interval = 250
                bg_index = 0
    else:
        background(background_img)

    interval -= 1

def mousePressed():
    global screen, words, players
    
    #Start knop
    if screen == 6 and isMouseOnButton(1070, 650, 165, 55):
        main_game.setTurnPlayer()
        globals.scherm = 'main'
            
    # Als je op -verder- drukt op scherm 3/4/5 en je hebt input staan in de box, ga naar scherm 6 en sla de input op als speler
    if (screen == 3 or screen == 4 or screen == 5) and isMouseOnButton(1070, 650, 195, 55):
        if len(words) > 0:
            player = Player(words)
            if screen <= len(players):
                player.cards = list([x for x in players[screen - 1].cards])
                players[screen - 1] = player
            else:
                players.append(player)
        screen = 6
        words = ''
    
    #HOME button
    if isMouseOnButton(10,10,130,55):
        globals.scherm = 'home'
                        
    #Pijltje verder, zorg ervoor dat de lengte vd naam > 0 moet zijn            
    if screen != 6 and isMouseOnButton(890, 350, 100, 100) and len(words) > 0:
        player = Player(words)
        if screen <= len(players):
            player.cards = list([x for x in players[screen - 1].cards])
            players[screen - 1] = player
        else:
            players.append(player)
        screen += 1
        words = players[screen - 1].name if screen <= len(players) else ''
       
    #Pijltje terug
    if screen != 1 and screen != 6 and isMouseOnButton(290, 350, 100, 100):
        if screen <= len(players) and words == '':
            players.pop(screen - 1)
        screen -= 1
        words = players[screen - 1].name
        
    #terug knop op scherm 6, bij 5 spelers, 4 spelers, 3 spelers en 2 spelers
    if screen == 6 and isMouseOnButton(10, 655, 165, 55):
        screen = len(players)
        words = players[screen - 1].name
        
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def loadImages(): 
    global home_img, dobbel_img, home2_img, verder_img, verder_pijl, verder_pijl_hover, terug_pijl, terug_pijl_hover, leeg_vak, verder_pijl_idle, terug_pijl_idle, start1, start2, terug1, terug2, background_img, background_animation_images
    home_img = loadImage('assets/images/Home.png')
    dobbel_img = loadImage('assets/images/Dobbel.png')
    home2_img = loadImage('assets/images/Home2.png')
    dobbel2_img = loadImage('assets/images/Dobbel2.png')
    artifact_img = loadImage('assets/images/Artefact.png')
    artifact2_img = loadImage('assets/images/Artefact2.png')
    verder_img = loadImage('assets/images/Verder.png')
    verder_pijl = loadImage('assets/images/PijlVerderPaars.png')
    verder_pijl_hover = loadImage('assets/images/PijlVerder2Paars.png')
    verder_pijl_idle = loadImage('assets/images/PijlVerderIdle.png')
    terug_pijl = loadImage('assets/images/PijlTerugPaars.png')
    terug_pijl_hover = loadImage('assets/images/PijlTerug2Paars.png')
    terug_pijl_idle = loadImage('assets/images/PijlTerugIdle.png')
    leeg_vak = loadImage('assets/images/LeegVak.png')
    start1 = loadImage('assets/images/Start.png')
    start2 = loadImage('assets/images/Start2.png')
    terug1 = loadImage('assets/images/TerugKnop.png')
    terug2 = loadImage('assets/images/TerugKnop2.png')
    
    background_img = loadImage('background/bg0.jpg')
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 14)]
    
def imageShow(img, img2, x, y, wdth, hght, centered = False):
    if centered:
        imageMode(CENTER)
    else:
        imageMode(CORNER)
    if isMouseOnButton(x, y, wdth, hght, centered):
        image(img2, x, y, wdth, hght)
    else:
        image(img, x, y, wdth, hght)
        
def mouseHoverHandler():
    if isMouseOnButton(10, 10, 130, 55): # Home knop
        cursor(HAND)            
    elif (not (len(words) == 0 and screen - 1 == len(players)) or screen == len(players)) and isMouseOnButton(890, 350, 100, 100): #verderpijl
        cursor(HAND)    
    elif screen != 1 and isMouseOnButton(290,350,100,100): # terugpijl
        cursor(HAND)
    elif screen > 2 and isMouseOnButton(1105,655,165,55):  # Start knop
        cursor(HAND)
    else:
        cursor(ARROW)
        
    
    
