bg_index = 0
frame = 1

cards = []

red_color = (255, 0, 0)

turn = 1
    
class Card:
    pos = ()
    color = (255, 255, 255)
    name = str
    cooldown = int
    turn = 1

#Called once at start
def setup():
    card = Card()
    card.name = 'Bruh'
    card.cooldown = 4
    card.pos = (150, 100)
    cards.append(card)
    
    size(1280, 720)

#Called every frame
def draw():
    cycleBackground()    
    
    #Cards
    for card in cards:    
        cooldown_left = card.cooldown - (turn - card.turn)
        if cooldown_left == card.cooldown and card.color != red_color or cooldown_left <= 0 or card.color != red_color:
            cooldown_left = 0
        drawRectangle(card.color, card.pos, (150, 230))
        drawText('Artefact\nCooldown:' + str(cooldown_left), (card.pos[0] + 20, card.pos[1] + 20), (width, height), (0, 0, 0), 20)
        
    drawTurnButton()
    
    # Home Button
    image(loadImage('assets/buttons/Home.png'), 10, 10, 130, 55)
    
    mouseHoverHandler()
    
def mousePressed():
    global turn
    
    #Artifact
    if isMouseOnButton(posX=150, posY=100, buttonWidth=150, buttonHeight=230):
        card = getCard(150, 100)
        artifactClick(card)
            
    #Artifact
    if isMouseOnButton(posX=300, posY=100, buttonWidth=150, buttonHeight=230):
        card = getCard(300, 100)
        artifactClick(card)
        
    #Turn
    if isMouseOnButton(posX=width - 125, posY=50, buttonWidth=75, buttonHeight=75):
        turn += 1
        cards_loop = [x for x in cards if x.color == red_color]
        for card in cards_loop:    
            if card.turn + card.cooldown <= turn:
                card.color = (255, 255, 255)
    
    if isMouseOnButton(posX=10, posY=10, buttonWidth=130, buttonHeight=55):
        exit()
        
def mouseHoverHandler():
    if isMouseOnButton(10, 10, 130, 55): # EXIT button
        cursor(HAND)
    elif isMouseOnButton(width - 125, 50, 75, 75): # Turn button
        cursor(HAND)
        drawTurnButton((255, 170, 0))
    elif isMouseOnButton(posX=150, posY=100, buttonWidth=150, buttonHeight=230):
        card = getCard(150, 100)
        if card and card.color is not red_color:
            cursor(HAND)
    else:
        cursor(ARROW)          
        
def artifactClick(card):
    global turn
    if card and card.color != red_color:    
        turn += 1
        card.color = red_color
        card.turn = turn
        
def drawTurnButton(color = (255, 231, 48)):
    turn_btn_pos = (width - 125, 50)
    drawRectangle(color, turn_btn_pos, (75, 75))
    if color == (255, 231, 48):
        drawText('Turn: ' + str(turn), (turn_btn_pos[0] + 3, turn_btn_pos[1] - 25), (width, height), (255, 0, 0), 20)

def drawRectangle(card_color, pos, card_size, stroke = ()):
    fill(card_color[0], card_color[1], card_color[2])
    
    if card_color != red_color and stroke != ():
        stroke(stroke_color[0], stroke_color[1], stroke_color[2])
        strokeWeight(stroke[3])
    elif stroke != ():
        strokeWeight(0)
        
    rect(pos[0], pos[1], card_size[0], card_size[1])
    
def drawText(draw_text, pos, size, color, font_size):
    fill(color[0], color[1], color[2])
    text(draw_text, pos[0], pos[1], size[0], size[1])    
    textSize(font_size)
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
    return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def getCard(posX, posY):
    return next(x for x in cards if x.pos == (posX, posY))

def cycleBackground():
    global bg_index, frame    
    frame = frame + 1 if frame < 60 else 1
    if frame % 2 == 0:
        background(loadImage('background/bg' + str(bg_index) + '.jpg'))
        bg_index = bg_index + 1 if bg_index < 32 else 0
    
