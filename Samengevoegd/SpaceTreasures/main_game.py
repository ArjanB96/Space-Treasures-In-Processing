import globals, home_screen, artefact_screen, new_turn
from globals import Player, Card, Button

bg_index = 0

players = globals.players
buttons = []

turn = 1
turn_player_index = 0

first_turn = True
show_help = True
delete_mode = False

exchange_mode = False
exchange_dict = { 'player': None, 'card': None }

hovered_card = None

#Called once at start
def setup():
    loadImages()
    
    # Buttons
    buttons.append(Button('regels', regels_img, regels2_img, (10, 10), (195, 55)))
    #buttons.append(Button('artifact', artifact_img, artifact2_img, (width - 265, height - 130), (255, 55)))
    #buttons.append(Button('delete', verwijder_img, verwijder2_img, (width - 315, height - 65), (305, 55)))
    buttons.append(Button('info', info_img, info2_img, (10, height - 69), (60, 60)))
    buttons.append(Button('delete_popup', delete_popup_img, delete_popup2_img, (width // 2 - delete_popup_img.width // 2, height // 2 - delete_popup_img.height // 2), (767, 432), False))

#Called every frame
def draw():
    global players, turn_player_index
    
    players = globals.players
    turn_player_index = turn_player_index if turn_player_index < len(players) else 0
    
    cycleBackground()
    
    drawAllCards()
    drawPlayerNames()
    drawButtons()

    mouseHoverHandler()
    
    if hovered_card and not show_help:
        drawCardInfo()
    
    if show_help and not next((x for x in buttons if x.name == 'delete_popup'), None).visible:
        image(tutorial_img, 0, 0)
    
    if delete_mode:
        image(delete_mode_img, 0, 0)
            
def setTurnPlayerIndex(i):
    global turn_player_index
    turn_player_index = i
    
def mousePressed():
    global turn, turn_player_index, current_screen, show_help, first_turn, delete_mode, buttons, exchange_mode, exchange_card
    
    goto_next_turn = False
    
    if not next((x for x in buttons if x.name == 'delete_popup'), None).visible:
        # Cards 
        if not delete_mode and not exchange_mode:
            for card in reversed(players[turn_player_index].cards):
                if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]):                
                    if not card.on_cooldown and card.name != 'Exchange':
                        goto_next_turn = True
                    if card.name == 'Exchange':
                        exchange_dict['player'] = players[turn_player_index]
                        exchange_dict['card'] = card
                    artifactClick(card)
                    break
        elif delete_mode:
            for player in players:
                for card in reversed(player.cards):
                    if isMouseOnButton(card.pos[0], card.pos[1], card.size[0], card.size[1]):
                        player.cards.remove(card)
                        break
        elif exchange_mode:
            for player in filter(lambda x: x != players[turn_player_index], players):
                for card in reversed(player.cards):
                    if isMouseOnButton(card.pos[0], card.pos[1], card.size[0], card.size[1]):
                        stolen_card = getCard(card.pos[0], card.pos[1])
                        exchange_player = exchange_dict['player']
                        exchange_card = exchange_dict['card']
                        
                        exchange_player.cards.remove(exchange_card)
                        player.cards.remove(stolen_card)
                        exchange_player.cards.append(stolen_card)
                        player.cards.append(exchange_card)
                        
                        exchange_mode = False
                        exchange_card = None
                        goto_next_turn = True
                        break

    for button in [x for x in buttons if x.visible]:
        if isMouseOnButton(button.pos[0], button.pos[1], button.size[0], button.size[1]):
            if button.name == 'artifact':
                artefact_screen.setSpelerIndex(turn_player_index)
                globals.scherm = 'artifact'
            elif button.name == 'turn':
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
            elif button.name == 'info':
                show_help = True if not show_help else False
            elif button.name == 'delete':
                delete_popup = next((x for x in buttons if x.name == 'delete_popup'), None)
                delete_popup.visible = True if not delete_popup.visible and not delete_mode else False
                if delete_mode:
                    delete_mode = False
            elif button.name == 'delete_popup':
                button.visible = False
                delete_mode = True if not delete_mode else False                
            elif button.name == 'regels':
                home_screen.screen = 1
                globals.scherm = 'home'
        
    if goto_next_turn:
        if first_turn:
            show_help = False
        first_turn = False
        turn_player_index = turn_player_index + 1 if turn_player_index < len(players) - 1 else 0
        new_turn.player = players[turn_player_index]
        globals.scherm = 'new_turn' 
        
def mouseHoverHandler():
    global hovered_card
    
    card_hover = False
    
    if not next((x for x in buttons if x.name == 'delete_popup'), None).visible:
        # Cards
        if not delete_mode and not exchange_mode:
            for card in reversed(players[turn_player_index].cards):
                if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]):
                    drawAllCards(card)
                    if not card.on_cooldown and not exchange_mode:
                        cursor(HAND)
                        card_hover = True
                    break
        elif delete_mode:
            for player in players:
                for card in reversed(player.cards):
                    card_size = card.size if player == players[turn_player_index] else (card.size[0] - 33, card.size[1] - 12)
                    if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card_size[0], buttonHeight=card_size[1]):
                        drawAllCards(card)
                        cursor(HAND)
                        card_hover = True
                        break
        elif exchange_mode:
            for player in filter(lambda x: x != players[turn_player_index], players):
                for card in reversed(player.cards):
                    card_size = card.size if player == players[turn_player_index] else (card.size[0] - 33, card.size[1] - 12)
                    if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card_size[0], buttonHeight=card_size[1]):
                        drawAllCards(card)
                        cursor(HAND)
                        card_hover = True
                        break
        
    # Buttons
    for button in [x for x in buttons if x.visible]:
        if isMouseOnButton(button.pos[0], button.pos[1], button.size[0], button.size[1]):
            image(button.hover_img, button.pos[0], button.pos[1], button.size[0], button.size[1])
            cursor(HAND)
            card_hover = True
            break

    if not card_hover:
        hovered_card = None
        cursor(ARROW)
        
def artifactClick(card):
    global turn, exchange_mode
    
    if card.on_cooldown:
        return

    if card:
        turn += 1
        card.on_cooldown = True
        card.turn = turn
    
    if card.name == 'Exchange':
        exchange_mode = True
    
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
                image(verder_img, pos[0] + 190, pos[1], 30, 45)
            elif len(player.name) >= 7:
                pos = (80, 70 + (i * 135))                    
                image(verder_img, pos[0] + 145, pos[1], 30, 45)
            else:
                pos = (125, 70 + (i * 135))                    
                image(verder_img, pos[0] + 100, pos[1], 30, 45)
                
            drawText(players[i].name, pos, (230, 100), (247, 151, 29), 30, center = False)
    
def drawAllCards(highlight_card = None):
    global hovered_card
    
    if highlight_card:
        hovered_card = highlight_card
        
    for p_index, player in enumerate(players):
        
        if len(player.cards) == 0:
            card_pos = (280, 40 + (135 * p_index))
            card_size = (200, 100)
            card_size = card_size if player == players[turn_player_index] else (card_size[0] - 33, card_size[1] - 12)
            
            image(no_cards_card if player == players[turn_player_index] else no_cards_white_card, card_pos[0], card_pos[1], card_size[0], card_size[1])
            
            if player != players[turn_player_index]:                
                image(black_card, card_pos[0], card_pos[1], card_size[0], card_size[1])
        
        for c_index, card in enumerate(player.cards):                      
            cooldown_left = card.cooldown - (turn - card.turn)
            if cooldown_left == card.cooldown and not card.on_cooldown or cooldown_left <= 0 or not card.on_cooldown:
                cooldown_left = 0            
                        
            card.pos = (280 + (115 * c_index), 40 + (5 * c_index) + (135 * p_index))
            card_size = card.size if player == players[turn_player_index] else (card.size[0] - 33, card.size[1] - 12)
            
            if card.element == 'Amaterasu':
                image(amaterasu_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            elif card.element == 'Aqua':
                image(aqua_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            elif card.element == 'Kaytsak':
                image(kaytsak_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            
            if card.on_cooldown:
                image(red_card, card.pos[0], card.pos[1], card_size[0], card_size[1]) 
            if (player != players[turn_player_index] and (not delete_mode and not exchange_mode)) or (player == players[turn_player_index] and exchange_mode):
                image(black_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
        
            if player == players[turn_player_index] and card == highlight_card and not card.on_cooldown:
                image(white_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            elif player != players[turn_player_index] and exchange_mode and card == highlight_card:
                image(white_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
                
            text_to_draw = card.name + '\n' + card.element
            if cooldown_left > 0:
                text_to_draw += '\nAfkoeltijd: ' + str(cooldown_left)
            drawText(text_to_draw, (card.pos[0] + 15, card.pos[1] + (15 if not card.on_cooldown else 10)), (width, height), (0, 0, 0) if player == players[turn_player_index] or delete_mode or exchange_mode else (145, 145, 145), 16 if player == players[turn_player_index] else 14)

def drawCards(player, card_size = (200, 100), card_pos = (540, 600), font_size = 14):
    if len(player.cards) == 0:
            image(no_cards_card if player == players[turn_player_index] else no_cards_white_card, card_pos[0], card_pos[1], card_size[0], card_size[1])
        
    for c_index, card in enumerate(player.cards):                      
        cooldown_left = card.cooldown - (turn - card.turn)
        if cooldown_left == card.cooldown and not card.on_cooldown or cooldown_left <= 0 or not card.on_cooldown:
            cooldown_left = 0            
                    
        card.pos = (card_pos[0] + (115 * c_index), card_pos[1] + (5 * c_index))
        
        card_img = amaterasu_card if card.element == 'Amaterasu' else aqua_card if card.element == 'Aqua' else kaytsak_card
        
        image(card_img, card.pos[0], card.pos[1], card_size[0], card_size[1])
        
        if card.on_cooldown:
            image(red_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            
        text_to_draw = card.name + '\n' + card.element
        if cooldown_left > 0:
            text_to_draw += '\nAfkoeltijd: ' + str(cooldown_left)
        drawText(text_to_draw, (card.pos[0] + 15, card.pos[1] + (15 if not card.on_cooldown else 10)), (width, height), (0, 0, 0), font_size)
        
def drawCardInfo():
    name = hovered_card.name
    image(groot_leeg_vak_img, width - 300, 50, 250, 400)
    drawText(hovered_card.name, (width - 275, 85), (200, 50), (255, 255, 255), 30, True)
    drawText('Cooldown: ' + str(hovered_card.cooldown), (width - 275, 130), (200, 50), (255, 255, 255), 20, True)
    
    if name == 'Swap':
        description = 'Ruil 2 spelers inclusief\njezelf van plek op het\nspeelbord.'
    elif name == 'Haste':
        description = 'Bij het stappen zetten mag\nje 1 extra stap zetten.'
    elif name == 'Eyedrop':
        description = 'Je mag 1 oog minder\ngooien bij het dobbelen\nvoor een artefact.'
    elif name == 'Skip':
        description = 'Kies een speler die zijn/haar\nbeurt moet overslaan.'
    elif name == 'Exchange':
        description = 'Ruil een artefact naar keuze\nmet iemand op dezelfde\nplaneet.\n\nBij gebruik: klik op een\nartefact van een andere\nspeler om te ruilen.'
    elif name == 'Blockade':
        description = 'Zet op het bordspel een\nblokkade neer om te\nvoorkomen dat andere\nspelers de planeet betreden.'
        
    drawText(description, (width - 285, 195), (500, 500), (255, 255, 255), 18)

def drawRectangle(color, pos, size):
    fill(color[0], color[1], color[2])        
    rect(pos[0], pos[1], size[0], size[1])
    
def drawText(draw_text, pos, size, color, font_size, center = False):
    fill(color[0], color[1], color[2])
    textAlign(CENTER) if center else textAlign(LEFT)
    textFont(createFont('SansSerif.plain', 10))
    textSize(font_size)    
    text(draw_text, pos[0], pos[1], size[0], size[1])
    
def drawButtons():
    for button in [x for x in buttons if x.visible]:
        image(button.img, button.pos[0], button.pos[1], button.size[0], button.size[1])    
    
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
    if centered:
        return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2 else False
    return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def getCard(posX, posY):
    cards = []
    for p in players:
        [cards.append(c) for c in p.cards]
            
    return next((x for x in cards if x.pos == (posX, posY)), None)

def loadImages():
    global background_img, background_animation_images, home_img, home2_img, artifact_img, artifact2_img, verder_img, verder_paars_img, verder_paars2_img, info_img, info2_img, regels_img, regels2_img
    global delete_mode_img, verwijder_img, verwijder2_img, delete_popup_img, delete_popup2_img, amaterasu_card, kaytsak_card, aqua_card, red_card, black_card, white_card, no_cards_card, no_cards_white_card, tutorial_img, star_covers_img
    global groot_leeg_vak_img
    
    home_img = loadImage('assets/buttons/Home.png')
    home2_img = loadImage('assets/buttons/Home2.png')
    artifact_img = loadImage('assets/buttons/Artefact.png')
    artifact2_img = loadImage('assets/buttons/Artefact2.png')
    verder_img = loadImage('assets/buttons/Verder.png')
    verder_paars_img = loadImage('assets/buttons/VerderPaars.png')
    verder_paars2_img = loadImage('assets/buttons/VerderPaars2.png')
    info_img = loadImage('assets/buttons/Info.png')
    info2_img = loadImage('assets/buttons/Info2.png')
    verwijder_img = loadImage('assets/buttons/Verwijder.png')
    verwijder2_img = loadImage('assets/buttons/Verwijder2.png')
    regels_img = loadImage('assets/images/Regels.png')
    regels2_img = loadImage('assets/images/Regels2.png')
    delete_popup_img = loadImage('assets/buttons/verwijder_popup.png')
    delete_popup2_img = loadImage('assets/buttons/verwijder_popup2.png')
    delete_mode_img = loadImage('assets/misc/delete_mode.png')
    amaterasu_card = loadImage('assets/cards/Amaterasu_card_flipped.png')
    kaytsak_card = loadImage('assets/cards/Kaytsak_card_flipped.png')
    aqua_card = loadImage('assets/cards/Aqua_card_flipped.png')
    red_card = loadImage('assets/cards/Red_card_flipped.png')
    black_card = loadImage('assets/cards/Black_card_flipped.png')
    white_card = loadImage('assets/cards/White_card_flipped.png')
    no_cards_card = loadImage('assets/cards/no_cards_flipped.png')
    no_cards_white_card = loadImage('assets/cards/no_cards_white_flipped.png')
    tutorial_img = loadImage('assets/misc/tutorial.png')
    star_covers_img = loadImage('assets/misc/star_covers.png')
    groot_leeg_vak_img = loadImage('assets/images/GrootLeegvak.png')
    
    background_img = loadImage('background/bg0.jpg')
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 14)]

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
            
    image(star_covers_img, 0, 0)
    interval -= 1
    
