bg_index = 0
frame = 1

card_color = (255, 255, 255)
red_color = (255, 0, 0)

turn = 1
card_turn = 1
cooldown = 4
    
#Called once at start
def setup():
    size(1280, 720)

#Called every frame
def draw():
    global card_color, scherm
    
    cycleBackground()
  
    #Card
    card_pos = (100, 100)
    cooldown_left = cooldown - (turn - card_turn)
    if cooldown_left == cooldown and card_color != red_color or cooldown_left <= 0:
        cooldown_left = 0
    drawRectangle(card_color, card_pos, (150, 230))
    drawText('Artefact\nCooldown:' + str(cooldown_left), (card_pos[0] + 20, card_pos[1] + 20), (width, height), (0, 0, 0), 20)
    
    #Turn button
    turn_btn_pos = (width - 125, 50)
    drawRectangle((255, 231, 48), turn_btn_pos, (75, 75))
    drawText('Turn: ' + str(turn), (turn_btn_pos[0] + 3, turn_btn_pos[1] - 25), (width, height), (255, 0, 0), 20)
    
def mousePressed():
    global card_color, turn, card_turn
    
    #Artifact
    if isButtonClicked(100, 100, 150, 230) and card_color != red_color:
        turn += 1      
        card_color = red_color
        card_turn = turn
        
    #Turn
    if isButtonClicked(width - 125, 50, 75, 75):
        turn += 1
        if card_turn + cooldown <= turn:
            card_color = (255, 255, 255)

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
    
def isButtonClicked(pos_x, pos_y, btn_width, btn_height):
    return True if pos_x < mouseX < pos_x + btn_width and pos_y < mouseY < pos_y + btn_height else False

def cycleBackground():
    global bg_index, frame    
    frame = frame + 1 if frame < 60 else 1
    if frame % 2 == 0:
        background(loadImage('background/bg' + str(bg_index) + '.jpg'))
        bg_index = bg_index + 1 if bg_index < 32 else 0
    
