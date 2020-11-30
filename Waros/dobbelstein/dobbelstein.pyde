bg_index = 0
def cycleBackground():
    global bg_index
    background(loadImage('bg' + str(bg_index) + '.jpg'))
    bg_index = bg_index + 1 if bg_index < 32 else 0
def setup():
    global img1
    global img2
    global img3
    global img4
    global img5
    global img6
    img1 = loadImage("bot1.gif")
    img2 = loadImage("bot2.gif")
    img3 = loadImage("bot3.gif")
    img4 = loadImage("bot4.gif")
    img5 = loadImage("bot5.gif")
    img6 = loadImage("bot6.gif")
    size(1280, 720)
    frameRate(15)
def draw():
    global number
    cycleBackground()
    image(img1, 500, 250, 200, 200)
    fill(0)
    ellipse(mouseX, mouseY, 0, 0)
    if 500 < mouseX < 500 + 200 and 250 < mouseY < 250 + 200:
        number = str(int(random(1, 7)))
        if number == '1':
          image(img1, 500, 250, 200, 200)
        if number == '2':
          image(img2, 500, 250, 200, 200)
        if number == '3':
          image(img3, 500, 250, 200, 200)
        if number == '4':
          image(img4, 500, 250, 200, 200)
        if number == '5':
          image(img5, 500, 250, 200, 200)
        if number == '6':
          image(img6, 500, 250, 200, 200)
def mouseClicked():
    while True:
        if 500 < mouseX < 500 + 200 and 250 < mouseY < 250 + 200:
          number = str(int(random(1, 7)))
          while True:
            if number == '1':
              image(img1, 500, 250, 200, 200)
              break
            if number == '2':
              image(img2, 500, 250, 200, 200)
              break
            if number == '3':
              image(img3, 500, 250, 200, 200)
              break
            if number == '4':
              image(img4, 500, 250, 200, 200)
              break
            if number == '5':
              image(img5, 500, 250, 200, 200)
              break
            if number == '6':
              image(img6, 500, 250, 200, 200)
              break

        
        
        
   
        


         
    

        


         
    
