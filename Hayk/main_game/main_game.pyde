bg_index = 0
frame = 1

cards = []

turn = 1
    
class Card:
    def __init__(self, pos, size, name, cooldown, element): 
        self.pos = pos
        self.size = size
        self.name = name
        self.cooldown = cooldown
        self.element = element
        self.on_cooldown = False
        self.turn = 1

#Called once at start
def setup():
    cards.append(Card(pos=(150, 100), size=(120, 200), name='Exchange', cooldown=6, element='Kaytsak'))
    cards.append(Card(pos=(300, 100), size=(120, 200), name='Swap', cooldown=3, element='Aqua'))
    cards.append(Card(pos=(150, 325), size=(120, 200), name='Blockade', cooldown=4, element='Amaterasu'))
    
    size(1280, 720)

#Called every frame
def draw():
    cycleBackground()
    
    drawAllCards()    
    drawTurnButton()
    
    # Buttons
    image(loadImage('assets/buttons/Home.png'), 10, 10, 130, 55)
    image(loadImage('assets/buttons/Dobbel.png'), 10, height - 65, 195, 55)
    
    mouseHoverHandler()
    
def mousePressed():
    global turn
    
    # Cards
    for card in cards:
        if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]):
            artifactClick(card)
            break        
        
    # Turn
    if isMouseOnButton(posX=width - 125, posY=50, buttonWidth=75, buttonHeight=75):
        turn += 1
        cards_loop = [x for x in cards if x.on_cooldown]
        for card in cards_loop:    
            if card.turn + card.cooldown <= turn:
                card.on_cooldown = False
    
    # Dobbel
    if isMouseOnButton(posX=10, posY=height - 65, buttonWidth=195, buttonHeight=55):  
        link('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
    # Home
    if isMouseOnButton(posX=10, posY=10, buttonWidth=130, buttonHeight=55):
        exit()
        
def mouseHoverHandler():
    card_hover = False
    
    # Cards
    for card in cards:
        if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]) and not card.on_cooldown:
            drawAllCards(card)
            cursor(HAND)
            card_hover = True
            break 
        
    if isMouseOnButton(10, 10, 130, 55): # Home button
        image(loadImage('assets/buttons/Home2.png'), 10, 10, 130, 55)
        cursor(HAND)
    elif isMouseOnButton(10, height - 65, 195, 55): # Dobbel button
        image(loadImage('assets/buttons/Dobbel2.png'), 10, height - 65, 195, 55)
        cursor(HAND)
    elif isMouseOnButton(width - 125, 50, 75, 75): # Turn button
        cursor(HAND)
        drawTurnButton((255, 170, 0))
    elif not card_hover:
        cursor(ARROW)          
        
def artifactClick(card):
    global turn
    if card and not card.on_cooldown:    
        turn += 1
        card.on_cooldown = True
        card.turn = turn
    
    cards_loop = [x for x in cards if x.on_cooldown]
    for card in cards_loop:    
        if card.turn + card.cooldown <= turn:
            card.on_cooldown = False

def drawAllCards(white_card = None):
    for card in cards:    
        cooldown_left = card.cooldown - (turn - card.turn)
        if cooldown_left == card.cooldown and not card.on_cooldown or cooldown_left <= 0 or not card.on_cooldown:
            cooldown_left = 0            
        image(loadImage('assets/cards/' + card.element + '_card.png'), card.pos[0], card.pos[1], card.size[0], card.size[1])
        if card.on_cooldown:
            image(loadImage('assets/cards/Red_card.png'), card.pos[0], card.pos[1], card.size[0], card.size[1])
        elif card == white_card:
            image(loadImage('assets/cards/White_card.png'), card.pos[0], card.pos[1], card.size[0], card.size[1])
        drawText(card.name + '\n\n' + card.element + '\n\n\nCooldown: ' + str(cooldown_left), (card.pos[0] - 578, card.pos[1] + 25), (width, height), (0, 0, 0), 16, True)

def drawTurnButton(color = (255, 231, 48)):
    btn_pos = (width - 125, 50)
    drawRectangle(color, btn_pos, (75, 75))
    if color == (255, 231, 48):
        drawText('Turn: ' + str(turn), (btn_pos[0] + 3, btn_pos[1] - 25), (width, height), color, 20)

def drawRectangle(color, pos, size):
    fill(color[0], color[1], color[2])        
    rect(pos[0], pos[1], size[0], size[1])
    
def drawText(draw_text, pos, size, color, font_size, center = False):
    fill(color[0], color[1], color[2])
    textAlign(CENTER) if center else textAlign(LEFT)
    textSize(font_size)
    text(draw_text, pos[0], pos[1], size[0], size[1])        
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def getCard(posX, posY):
    return next((x for x in cards if x.pos == (posX, posY)), None)

def cycleBackground():
    global bg_index, frame    
    frame = frame + 1 if frame < 60 else 1
    if frame % 2 == 0:
        background(loadImage('background/bg' + str(bg_index) + '.jpg'))
        bg_index = bg_index + 1 if bg_index < 32 else 0
    
