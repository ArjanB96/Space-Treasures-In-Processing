import globals, home_screen, artefact_screen, main_game, new_turn
from globals import Player, Card, Button

bg_index = 0

players = globals.players
buttons = []

selected_cards = []

first_turn = True

#Called once at start
def setup():
    loadImages()
    
    # Buttons
    buttons.append(Button('info', info_img, info2_img, (10, height - 69), (60, 60)))
    buttons.append(Button('delete_popup', delete_popup_img, delete_popup2_img, (width // 2 - delete_popup_img.width // 2, height // 2 - delete_popup_img.height // 2), (767, 432)))

#Called every frame
def draw():
    global players
    
    players = globals.players
    
    cycleBackground()
    
    drawCards(new_turn.player, None, (250, 125), (width / 2 - 300, height / 2 - 50))
    drawButtons()

    mouseHoverHandler()
    
def mousePressed():
    if not next((x for x in buttons if x.name == 'delete_popup'), None).visible:
        # Cards 
        for card in reversed(new_turn.player.cards):
            if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]):
                artifactClick(card)
                break

    for button in [x for x in buttons if x.visible]:
        if isMouseOnButton(button.pos[0], button.pos[1], button.size[0], button.size[1]):
            if button.name == 'info':
                pass
            elif button.name == 'delete_popup':
                button.visible = False
        
def mouseHoverHandler():
    card_hover = False
    
    if not next((x for x in buttons if x.name == 'delete_popup'), None).visible:
        # Cards
        for card in reversed(new_turn.player.cards):
            if isMouseOnButton(posX=card.pos[0], posY=card.pos[1], buttonWidth=card.size[0], buttonHeight=card.size[1]):
                drawCards(new_turn.player, card, (250, 125), (width / 2 - 300, height / 2 - 50))
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
        cursor(ARROW)
        
def artifactClick(card):
    pass
    

def drawCards(player, highlight_card = None, card_size = (200, 100), card_pos = (700, 600), font_size = 18):  
    for c_index, card in enumerate(player.cards):
        cooldown_left = card.cooldown - (main_game.turn - card.turn)
        if cooldown_left == card.cooldown and not card.on_cooldown or cooldown_left <= 0 or not card.on_cooldown:
            cooldown_left = 0            
                    
        card.pos = (card_pos[0] + (110 * c_index), card_pos[1] + (8 * c_index))
        
        card_img = amaterasu_card if card.element == 'Amaterasu' else aqua_card if card.element == 'Aqua' else kaytsak_card
        
        image(card_img, card.pos[0], card.pos[1], card_size[0], card_size[1])
        
        if card.on_cooldown:
            image(red_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            
        if card == highlight_card:
            image(white_card, card.pos[0], card.pos[1], card_size[0], card_size[1])
            
        text_to_draw = card.name + '\n' + card.element
        if cooldown_left > 0:
            text_to_draw += '\nAfkoeltijd: ' + str(cooldown_left)
        drawText(text_to_draw, (card.pos[0] + 15, card.pos[1] + (15 if not card.on_cooldown else 10)), (width, height), (0, 0, 0), font_size)

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
    delete_popup_img = loadImage('assets/buttons/element_popup.png')
    delete_popup2_img = loadImage('assets/buttons/element_popup2.png')
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
    
