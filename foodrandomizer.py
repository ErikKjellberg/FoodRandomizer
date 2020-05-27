import pygame
import random
import math
import codecs
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
width, height = 1000, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("MATRANDOMIZERAREN")
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("courier", 20)
font2 = pygame.font.SysFont("comicsansms", 72)
font3 = pygame.font.SysFont("courier", 20)
pygame.mixer.init()
music = pygame.mixer.music
funk = "C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\funk.MP3"
jazz = "C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\jazz.MP3"
bamse_blues = "C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\bamseblues3.MP3"
music.load(funk)
evil_laugh = pygame.mixer.Sound("C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\evillaugh.wav")
swoosh = pygame.mixer.Sound("C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\swoosh.wav")


def printText(fontType, fontSize, textString, color, x, y):
    font = pygame.font.SysFont(fontType, fontSize)
    text = font.render(textString, True, color)
    if x < 0:
        x = width/2-text.get_width()/2
    if y < 0:
        y = height/2-text.get_height()/2
    screen.blit(text,(x,y))

def createImage(image, x, y):
    if x>0 and y>0:
        finishedImage = pygame.transform.scale(pygame.image.load("C:\\Users\\erikkg\\Pictures\\"+image).convert_alpha(),(x,y))
    else:
        finishedImage = pygame.image.load("C:\\Users\\erikkg\\Pictures\\"+image).convert_alpha()
    return finishedImage

def orderList(textList):
    count = 0
    listToReturn = []
    for i in range(0,len(textList)):
        count += textList[i]

def bamses():
    music.load(bamse_blues)
    x = width/2
    y = height/2
    w = 100
    h = 100
    t = 0.0
    hell = createImage("hell.jpg",width,height)
    bamse = createImage("bamsehaha.jpg",0,0)
    pizza = createImage("pizza.png", 64,64)
    big_pizza = createImage("pizza.png", 80,80)
    giant_pizza = createImage("pizza.png",120,120)
    music.play(-1)
    evil_laugh.play()
    while True:
        screen.blit(hell,(0,0))
        pizzacount = 2**int(1+t/4)
        if pizzacount>32:
            pizzacount=32
        for i in range(0,pizzacount):
            screen.blit(pizza,(i*width/pizzacount+random.randrange(0,2),400+50*math.sin(math.pi/2+i%2)))
        for i in range(0,pizzacount):
            screen.blit(big_pizza,((i-0.5)*width/(pizzacount*0.8)+random.randrange(0,2),450+50*math.sin(math.pi/2+i%2)))
        for i in range(0,pizzacount):
            screen.blit(giant_pizza,((i)*width/(pizzacount*0.6)+random.randrange(0,2),500+50*math.sin(math.pi/2+i%2)))
        printText("chiller",200,"BAMSES",(0,0,0),-1,34)
        printText("chiller",200,"BAMSES",(120,0,0),-1,30)
        bamse = createImage("devilbamse.png",w,h)
        screen.blit(bamse,(x-w/2,y-h/2))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
            quit
        pygame.display.update()
        if w < width*0.5:
            w+=15
        if h < width*0.5:
            h+=15
        if y < height/2+100:
            y += 4
        clock.tick(60)
        t += 0.1
        t = round(t,1)
        print(t)



def intro():
    #bamses()
    textString = "Matrandomizeraren"
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render(textString, True, (0,0,0))
    frames = 0
    x = -1*text.get_width()
    y = 0
    while frames < 1200:
        screen.fill((255,255,255))
        for i in range(0,int(height/5)):
            pygame.draw.line(screen,(255-255*i/(height/5),255-255*i/(height/5),255),(0,height-i*5),(width,height-i*5),5)
        if frames < 150:
            x += 10
        elif frames < 300:
            x -= 10
            y = 500
        elif frames < 750 and x < width+100:
            y = 300+int(200*math.sin(frames/20))
            x += 4
        elif frames < 1000:
            y = height+(x+text.get_width())*(x-1000)/1500-200
            x -= 10
        elif x < width/2-text.get_width()/2:
            y = height+(x+text.get_width())*(x-1000)/1500-200
            x += 10
            print(y)
        else:
            frames = 1200
        if frames == 0 or frames == 150 or frames == 300 or frames == 350 or frames == 400 or frames == 475 \
            or frames == 550 or frames == 600 or frames == 750 or frames == 1025:
            swoosh.play()
        screen.blit(text,(x,y))
        if frames <= 300:
            printText("impact",20,"Tryck på en knapp för att skippa introt...",(255,0,0),10,height-25)
        elif frames > 300 and frames < 450:
            printText("impact",20,"Tryck på en knapp för att skippa introt...",(255,int((frames-300)*255/150),int((frames-300)*255/150)),10,height-25)
        else:
            printText("impact",20,"Tryck på en knapp för att skippa introt...",(255,255,255),10,height-25)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                frames = 1200
        pygame.display.update()
        clock.tick(120)
        frames += 1
    main()


    

def main():
    shrek = createImage("spookyshrekv4.png", 200, 200)
    questionMarks = createImage("questionmarks.png",200,200)
    sub = createImage("sub.jpg",200,75)
    sevenEleven = createImage("7eleven.jpg",200,100)
    berlinerKebab = createImage("berlinerkebab.jpg", 0, 0)
    bigRice = createImage("bigrice.jpg", 150, 150)
    maxMal = createImage("maxmal.jpg", 0, 0)
    mandarin = createImage("mandarin.jpg", 0, 0)
    hermans = createImage("hermans.jpg", 0, 0)
    bamses = createImage("bamses.jpg", 100, 130)
    magneto = pygame.font.SysFont("magneto",40)
    click_text1 = magneto.render("Klicka på en knapp för att starta!",True,(0,0,255))
    click_text2 = magneto.render("Klicka på en knapp för att starta!",True,(255,0,255))
    click_text3 = magneto.render("Klicka på en knapp för att starta!",True,(255,0,0))
    click_text4 = magneto.render("Klicka på en knapp för att starta!",True,(255,255,0))
    click_text5 = magneto.render("Klicka på en knapp för att starta!",True,(0,255,0))
    click_text6 = magneto.render("Klicka på en knapp för att starta!",True,(0,255,255))
    click_text7 = magneto.render("Klicka på en knapp för att starta!",True,(0,0,255))
    click_text_list = [click_text1,click_text2,click_text3,click_text4,click_text5,click_text6,click_text7]
    music.play(-1)
    y = 0
    v = 0
    ychange = 1
    inMenu = True
    while inMenu:
        screen.fill((255,255,255))
        """for i in range(0,int(height/5)):
            pygame.draw.line(screen,(255-255*i/(height/5),0,255*i/(height/5)),(0,height-i*5),(width,height-i*5),5)"""
        pygame.draw.ellipse(screen, (0,0,0), (230,30,width-450,125))
        pygame.draw.ellipse(screen, (255,120,120), (225,25,width-450,125))
        printText("comicsansms",10, "Copyright Erik Kjellberg 2019",(random.randrange(100,255),0,random.randrange(177,255)),0,0)
        printText("comicsansms", 50, "Matrandomizeraren", (0,0,0), -1, y+45)
        screen.blit(shrek,(width/2-shrek.get_width()/2,height/2-shrek.get_height()/2))
        screen.blit(questionMarks,(width/2-shrek.get_width()/2-questionMarks.get_width(),height/2-shrek.get_height()/2))
        screen.blit(questionMarks,(width/2+shrek.get_width()/2,height/2-shrek.get_height()/2))
        screen.blit(pygame.transform.rotate(sub,(v*10)), (50,125))
        screen.blit(sevenEleven,(10,300))
        screen.blit(berlinerKebab,(0,height-berlinerKebab.get_height()))
        screen.blit(bigRice,(width-bigRice.get_width()-10,height-bigRice.get_height()-10))
        screen.blit(maxMal,(width-maxMal.get_width()-10,20))
        screen.blit(mandarin,(width/2-mandarin.get_width()/2,400))
        screen.blit(hermans,(width-hermans.get_width()-10,height/2-hermans.get_height()/2))
        screen.blit(bamses,(width-bamses.get_width()-bigRice.get_width()-50,450))
        printText("times", 30, "Vad blir det för mat idag?", (180,0,0), -1, 160)
        for i in range(len(click_text_list)):
            screen.blit(click_text_list[i],(width/2-click_text_list[i].get_width()/2+i*2+20*math.cos(v)+5*y,400+i*2+20*math.sin(v)))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    music.stop()
                    chooseFood()
        y += ychange
        if y == 10 and ychange == 1:
            ychange = -1
        if y == -10 and ychange == -1:
            ychange = 1
        v += 0.1+random.randrange(0,10)/100
        pygame.display.update()
        clock.tick(60)

def chooseFood():
    music.load(jazz)
    music.play(-1)
    with codecs.open("C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\restaurantlist.txt", "r", "utf-8") as file:
        lines = file.readlines()
    for i in range(0,len(lines)):
        if "\r" in lines[i]:
            lines[i] = lines[i].replace("\r","")
        if "\n" in lines[i]:
            lines[i] = lines[i].replace("\n","")
    print(lines)
    with open("C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\trueorfalselist.txt", "r") as file:
        boolLines = file.readlines()
    for i in range(0,len(boolLines)):
        if "\n" in boolLines[i]:
            boolLines[i] = boolLines[i].replace("\n","")
    print(boolLines)
    waitFrames = 0
    colorFrames = 0
    colorList = [(255,120,120),(255,200,120),(255,255,120),(180,255,120),(120,255,255),(120,180,255),(180,120,255),(255,120,200)]
    number = -1
    chosen = False
    running = True
    while running:
        screen.fill(colorList[int(colorFrames)%len(colorList)])
        if not chosen:
            printText("courier", 30, "Datorn kommer välja en av följande restauranger:", (0,0,0), -1, 50)
            printText("courier", 20, "Klicka på en knapp för att se vad det blir...", (0,0,0), -1, 500)
        if chosen:
            printText("courier", 30, "Det blev...", (0,0,0), -1, 50)
            if waitFrames<30:
                waitFrames+=1
            elif lines[number]!="Bamses":
                printText("magneto", 75, (lines[number]+"!"), (0,0,0), -1, 475)
                printText("magneto", 75, (lines[number]+"!"), (0,150,0), -1, 470)
            if lines[number]=="Bamses":
                bamses()
        for i in range(0,len(lines)):
            x = 20 + (i%4)*(width-40)/4
            y = 100+50*int(i/4)
            printText("comicsansms", 18, lines[i], (0,0,0), x+2, y+2)
            printText("comicsansms", 18, lines[i], (255,255,255), x, y)
            if i == number and waitFrames>=30:
                printText("comicsansms", 18, lines[i], (0,150,0), x, y)
            if boolLines[i]=="0" and i!= number:
                font = pygame.font.SysFont("comicsansms", 18)
                text = font.render(lines[i], True, (255,255,255))
                pygame.draw.line(screen,(255,0,0),(x, y), (x+text.get_width(), y+text.get_height()),5)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                chosen = True
                music.stop()
                while True:
                    number = random.randrange(0,len(lines))
                    if boolLines[number]!="0":
                        break
                #comment line below if you don't want restaurants to be deleted
                boolLines[number]="0"
                with open("C:\\Users\\erikkg\\Documents\\Dokument\\Python\\Food randomizer\\trueorfalselist.txt", "w") as file:
                    print(boolLines)
                    for line in boolLines:
                        file.write(line+"\n")
        pygame.display.update()
        clock.tick(60)
        colorFrames+=0.1


intro()
