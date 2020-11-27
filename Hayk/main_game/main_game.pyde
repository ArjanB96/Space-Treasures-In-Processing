bg_index = 0

players = []

turn = 1
turn_player_index = 0
    
class Card:
    def __init__(self, size, name, cooldown, element): 
        self.pos = ()
        self.size = size
        self.name = name
        self.cooldown = cooldown
        self.element = element
        self.on_cooldown = False
        self.turn = 1

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.elements = []

#Called once at start
def setup():
    global turn_player
    
    p1 = Player('Hayk')    
    p1.cards.append(Card(size=(200, 100), name='Exchange', cooldown=6, element='Kaytsak'))
    p1.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Aqua'))
    p1.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Aqua'))
    players.append(p1)
    
    p2 = Player('Arjan')    
    players.append(p2)
    p2.cards.append(Card(size=(200, 100), name='Blockade', cooldown=3, element='Aqua'))
    p2.cards.append(Card(size=(200, 100), name='EyeDrop', cooldown=3, element='Amaterasu'))
    
    p3 = Player('Rayan')    
    players.append(p3)
    p3.cards.append(Card(size=(200, 100), name='Exchange', cooldown=4, element='Kaytsak'))
    p3.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Kaytsak'))
    p3.cards.append(Card(size=(200, 100), name='Haste', cooldown=3, element='Kaytsak'))
    p3.cards.append(Card(size=(200, 100), name='Exchange', cooldown=3, element='Amaterasu'))
    
    p4 = Player('Waros')    
    players.append(p4)
    p4.cards.append(Card(size=(200, 100), name='Blockade', cooldown=3, element='Amaterasu'))
    p4.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Amaterasu'))
    p4.cards.append(Card(size=(200, 100), name='Skip', cooldown=4, element='Amaterasu'))
    
    p5 = Player('Jeffrey')    
    players.append(p5)
    p5.cards.append(Card(size=(200, 100), name='Blockade', cooldown=3, element='Kaytsak'))
    p5.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Aqua'))
    
    turn_player = players[0]
    
    size(1280, 720)

#Called every frame
def draw():
    cycleBackground()
    
    drawAllCards()    
    drawTurnButton()
    drawPlayerNames()    
    
    # Buttons
    image(loadImage('assets/buttons/Home.png'), 10, 10, 130, 55)
    image(loadImage('assets/buttons/Dobbel.png'), width - 205, height - 65, 195, 55)
    
    mouseHoverHandler()
    
def mousePressed():
    global turn, turn_player_index
    goto_next_turn = False
    
    # Cards  
    for card in reversed(players[turn_player_index].cards):
        if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]) and not card.on_cooldown:
            artifactClick(card)
            goto_next_turn = True
            break        
        
    # Turn
    if isMouseOnButton(posX=width - 125, posY=50, buttonWidth=75, buttonHeight=75):
        turn += 1
        goto_next_turn = True
        for player in players: 
            cards_loop = [x for x in player.cards if x.on_cooldown]
            for card in cards_loop:    
                if card.turn + card.cooldown <= turn:
                    card.on_cooldown = False
    
    # Dobbel
    if isMouseOnButton(posX=width - 205, posY=height - 65, buttonWidth=195, buttonHeight=55):  
        link('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
    # Home
    if isMouseOnButton(posX=10, posY=10, buttonWidth=130, buttonHeight=55):
        exit()
        
    if goto_next_turn:
        turn_player_index = turn_player_index + 1 if turn_player_index < len(players) - 1 else 0     
        
def mouseHoverHandler():
    card_hover = False
    
    # Cards
    for card in reversed(players[turn_player_index].cards):
        if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]) and not card.on_cooldown:
            drawAllCards(card)
            cursor(HAND)
            card_hover = True
            break 
        
    if isMouseOnButton(10, 10, 130, 55): # Home button
        image(loadImage('assets/buttons/Home2.png'), 10, 10, 130, 55)
        cursor(HAND)
    elif isMouseOnButton(width - 205, height - 65, 195, 55): # Dobbel button
        image(loadImage('assets/buttons/Dobbel2.png'), width - 205, height - 65, 195, 55)
        cursor(HAND)
    elif isMouseOnButton(width - 125, 50, 75, 75): # Turn button
        cursor(HAND)
        drawTurnButton((255, 170, 0))
    elif not card_hover:
        cursor(ARROW)    
        
def artifactClick(card):
    global turn
    
    if card:    
        turn += 1
        card.on_cooldown = True
        card.turn = turn
    
    for player in players:
        cards_loop = [x for x in player.cards if x.on_cooldown]
        for card in cards_loop:    
            if card.turn + card.cooldown <= turn:
                card.on_cooldown = False    

def drawPlayerNames():
    for i, player in enumerate(players):
        if player == players[turn_player_index]:
            pos = (25, 70 + (i * 135))        
            drawText(players[i].name, pos, (200, 50), (255, 255, 255), 30, center = False)
            image(loadImage('assets/buttons/Verder.png'), pos[0] + 165, pos[1], 30, 45)
    
def drawAllCards(white_card = None):    
    for p_index, player in enumerate(players): 
        for c_index, card in enumerate(player.cards):                      
            cooldown_left = card.cooldown - (turn - card.turn)
            if cooldown_left == card.cooldown and not card.on_cooldown or cooldown_left <= 0 or not card.on_cooldown:
                cooldown_left = 0            
                        
            card.pos = (240 + (120 * c_index), 40 + (5 * c_index) + (135 * p_index))
            
            image(loadImage('assets/cards/' + card.element + '_card_flipped.png'), card.pos[0], card.pos[1], card.size[0], card.size[1])
                    
            if card.on_cooldown:
                image(loadImage('assets/cards/Red_card_flipped.png'), card.pos[0], card.pos[1], card.size[0], card.size[1]) 
            if player != players[turn_player_index]:                
                image(loadImage('assets/cards/Black_card_flipped.png'), card.pos[0], card.pos[1], card.size[0], card.size[1])           
            elif card == white_card:
                image(loadImage('assets/cards/White_card_flipped.png'), card.pos[0], card.pos[1], card.size[0], card.size[1])
                
            drawText(card.name + '\n' + card.element + '\nCooldown: ' + str(cooldown_left), (card.pos[0] + 15, card.pos[1] + 15), (width, height), (0, 0, 0), 16)

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
    global bg_index
    background(loadImage('background/bg' + str(bg_index) + '.jpg'))
    bg_index = bg_index + 1 if bg_index < 32 else 0
    
