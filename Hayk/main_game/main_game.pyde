bg_index = 0
current_screen = 'Hayk'

players = []

turn = 1
turn_player_index = 0
show_help = True
delete_mode = True
    
class Card:
    def __init__(self, size, name, cooldown, element): 
        self.pos = ()
        self.size = size
        self.name = name
        self.cooldown = cooldown
        self.element = element
        self.on_cooldown = False
        self.turn = 1
        self.dobbel = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.elements = []

#Called once at start
def setup():
    global turn_player 
    
    p1 = Player('VAC Efron')    
    #p1.cards.append(Card(size=(200, 100), name='Exchange', cooldown=6, element='Kaytsak'))
    #p1.cards.append(Card(size=(200, 100), name='Blockade', cooldown=4, element='Amaterasu'))
    #p1.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Aqua'))
    players.append(p1)
    
    p2 = Player('FlatN3ck')    
    players.append(p2)
    #p2.cards.append(Card(size=(200, 100), name='Blockade', cooldown=3, element='Aqua'))
    #p2.cards.append(Card(size=(200, 100), name='EyeDrop', cooldown=3, element='Amaterasu'))
    
    p3 = Player('Rayantjhu')    
    players.append(p3)
    #p3.cards.append(Card(size=(200, 100), name='Exchange', cooldown=4, element='Kaytsak'))
    #p3.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Kaytsak'))
    #p3.cards.append(Card(size=(200, 100), name='Haste', cooldown=3, element='Kaytsak'))
    #p3.cards.append(Card(size=(200, 100), name='Exchange', cooldown=3, element='Amaterasu'))
    
    p4 = Player('Ocean Man')    
    players.append(p4)
    #p4.cards.append(Card(size=(200, 100), name='Blockade', cooldown=3, element='Amaterasu'))
    #p4.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Amaterasu'))
    #p4.cards.append(Card(size=(200, 100), name='Skip', cooldown=4, element='Amaterasu'))
    
    p5 = Player('Jeffrey')    
    players.append(p5)
    #p5.cards.append(Card(size=(200, 100), name='Blockade', cooldown=3, element='Kaytsak'))
    #p5.cards.append(Card(size=(200, 100), name='Swap', cooldown=4, element='Aqua'))
    
    turn_player = players[0]
    
    background(0)
    
    loadImages()
    
    size(1280, 720)

#Called every frame
def draw():
    cycleBackground()
    
    if current_screen == 'Hayk':
        drawAllCards()    
        drawTurnButton()
        drawPlayerNames()
        
        if show_help:
            image(tutorial_img, 0, 0)
        
        # Buttons
        image(home_img, 10, 10, 130, 55)
        image(artifact_img, width - 265, height - 65, 255, 55)
        image(info_img, 10, height - 69, 60, 60)
        
        mouseHoverHandler()
    
def mousePressed():
    global turn, turn_player_index, current_screen, show_help
    
    goto_next_turn = False
    
    # Cards 
    if not delete_mode:
        for card in reversed(players[turn_player_index].cards):
            if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]) and not card.on_cooldown:
                artifactClick(card)
                goto_next_turn = True
                break
    else:
        for player in players:
            for card in reversed(player.cards):
                if isMouseOnButton(card.pos[0], card.pos[1], card.size[0], card.size[1]):
                    player.cards.remove(card)
                    break
        
    # Turn
    if isMouseOnButton(posX=width - 125, posY=50, buttonWidth=75, buttonHeight=75):
        turn += 1
        goto_next_turn = True
        for player in players: 
            cards_loop = [x for x in player.cards if x.on_cooldown]
            for card in cards_loop:      
                if player != players[turn_player_index]:
                    card.turn += 1
                    continue    
                if card.turn + card.cooldown <= turn:
                    card.on_cooldown = False
        
    # Artifact
    if isMouseOnButton(posX=width - 265, posY=height - 65, buttonWidth=255, buttonHeight=55):  
        link('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
    # Info
    if isMouseOnButton(posX=10, posY=height - 69, buttonWidth=60, buttonHeight=60):
        show_help = True
    
    # Home
    if isMouseOnButton(posX=10, posY=10, buttonWidth=130, buttonHeight=55):
        exit()
        
    if goto_next_turn:
        show_help = False
        turn_player_index = turn_player_index + 1 if turn_player_index < len(players) - 1 else 0     
        
def mouseHoverHandler():
    card_hover = False
    
    # Cards
    if not delete_mode:
        for card in reversed(players[turn_player_index].cards):
            if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]) and not card.on_cooldown:
                drawAllCards(card)
                cursor(HAND)
                card_hover = True
                break
    else:
        for player in players:
            for card in reversed(player.cards):
                if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]):
                    drawAllCards(card)
                    cursor(HAND)
                    card_hover = True
                    break
        
    if isMouseOnButton(10, 10, 130, 55): # Home button
        image(home2_img, 10, 10, 130, 55)
        cursor(HAND)
    elif isMouseOnButton(width - 265, height - 65, 255, 55): # Artefact button
        image(artifact2_img, width - 265, height - 65, 255, 55)
        cursor(HAND)
    elif isMouseOnButton(width - 125, 50, 75, 75): # Turn button
        cursor(HAND)
        drawTurnButton((218, 127, 251), True)
    elif isMouseOnButton(10, height - 69, 60, 60): # Info button
        image(info2_img, 10, height - 69, 60, 60)
        cursor(HAND)
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
            if player != players[turn_player_index]:
                card.turn += 1
                continue 
            if card.turn + card.cooldown <= turn:
                card.on_cooldown = False

def drawPlayerNames():
    for i, player in enumerate(players):
        if player == players[turn_player_index]:
            if len(player.name) > 10:
                pos = (35, 70 + (i * 135))                    
                image(verder_img, pos[0] + 240, pos[1], 30, 45)
            elif len(player.name) > 8:
                pos = (80, 70 + (i * 135))                    
                image(verder_img, pos[0] + 195, pos[1], 30, 45)
            else:
                pos = (125, 70 + (i * 135))                    
                image(verder_img, pos[0] + 150, pos[1], 30, 45)
                
            drawText(players[i].name, pos, (230, 100), (247, 151, 29), 30, center = False)
    
def drawAllCards(highlight_card = None):    
    for p_index, player in enumerate(players):
        
        if len(player.cards) == 0:
            card_pos = (330, 40 + (135 * p_index))
            card_size = (200, 100)
            card_size = card_size if player == players[turn_player_index] else (card_size[0] - 33, card_size[1] - 12)
            
            image(no_cards_card, card_pos[0], card_pos[1], card_size[0], card_size[1])
            
            if player != players[turn_player_index]:                
                image(black_card, card_pos[0], card_pos[1], card_size[0], card_size[1])
        
        for c_index, card in enumerate(player.cards):                      
            cooldown_left = card.cooldown - (turn - card.turn)
            if cooldown_left == card.cooldown and not card.on_cooldown or cooldown_left <= 0 or not card.on_cooldown:
                cooldown_left = 0            
                        
            card.pos = (330 + (120 * c_index), 40 + (5 * c_index) + (135 * p_index))
            card_size = card.size if player == players[turn_player_index] else (card.size[0] - 33, card.size[1] - 12)
            
            if card.element == 'Amaterasu':
                image(amaterasu_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            elif card.element == 'Aqua':
                image(aqua_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            elif card.element == 'Kaytsak':
                image(kaytsak_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            
            if card.on_cooldown:
                image(red_card, card.pos[0], card.pos[1], card_size[0], card_size[1]) 
            if player != players[turn_player_index] and not delete_mode:                
                image(black_card, card.pos[0], card.pos[1], card_size[0], card_size[1])           
            elif card == highlight_card:
                image(white_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
                
            text_to_draw = card.name + '\n' + card.element
            if cooldown_left > 0:
                text_to_draw += '\nCooldown: ' + str(cooldown_left)
            drawText(text_to_draw, (card.pos[0] + 15, card.pos[1] + 15), (width, height), (0, 0, 0) if player == players[turn_player_index] or delete_mode else (145, 145, 145), 16 if player == players[turn_player_index] else 14)

def drawTurnButton(color = (218, 127, 251), hover = False):
    img = verder_paars_img if not hover else verder_paars2_img
    
    btn_pos = (width - 125, 50)
    image(img, btn_pos[0], btn_pos[1], 75, 75)
    drawText('Beurt: ' + str(turn), (btn_pos[0], btn_pos[1] - 25), (width, height), color, 20)

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

def loadImages():
    global background_img, background_animation_images, home_img, home2_img, artifact_img, artifact2_img, verder_img, verder_paars_img, verder_paars2_img, info_img, info2_img
    global amaterasu_card, kaytsak_card, aqua_card, red_card, black_card, white_card, no_cards_card, tutorial_img, star_covers_img
    
    home_img = loadImage('assets/buttons/Home.png')
    home2_img = loadImage('assets/buttons/Home2.png')
    artifact_img = loadImage('assets/buttons/Artefact.png')
    artifact2_img = loadImage('assets/buttons/Artefact2.png')
    verder_img = loadImage('assets/buttons/Verder.png')
    verder_paars_img = loadImage('assets/buttons/VerderPaars.png')
    verder_paars2_img = loadImage('assets/buttons/VerderPaars2.png')
    info_img = loadImage('assets/buttons/Info.png')
    info2_img = loadImage('assets/buttons/Info2.png')
    amaterasu_card = loadImage('assets/cards/Amaterasu_card_flipped.png')
    kaytsak_card = loadImage('assets/cards/Kaytsak_card_flipped.png')
    aqua_card = loadImage('assets/cards/Aqua_card_flipped.png')
    red_card = loadImage('assets/cards/Red_card_flipped.png')
    black_card = loadImage('assets/cards/Black_card_flipped.png')
    white_card = loadImage('assets/cards/White_card_flipped.png')
    no_cards_card = loadImage('assets/cards/no_cards_flipped.png')
    tutorial_img = loadImage('assets/misc/tutorial.png')
    star_covers_img = loadImage('assets/misc/star_covers.png')
    
    background_img = loadImage('background/bg0.jpg')
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 13)]



interval = 300

def cycleBackground():
    global bg_index, interval
    
    background(background_img)
    background(background_animation_images[bg_index])
    image(star_covers_img, 0, 0)
    
    if bg_index < len(background_animation_images) - 1:
        bg_index += 1
    else:
        bg_index = 0
        interval = 300
        
    interval -= 1
    
