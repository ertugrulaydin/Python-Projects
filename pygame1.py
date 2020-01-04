import pygame,sys,random


pygame.init()

boyut = (800,600)


font = pygame.font.SysFont("Helvetica",48)


clock = pygame.time.Clock()
screen = pygame.display.set_mode(boyut)



def startGame(numCount):
    numList = []
    for i in range (0,numCount):
        x=0
        y=0
        num=random.randint(0,9)
        numbers = font.render(str(num),1,(255,0,0),(0,0,0))
        numList.append(num)

        clock.tick(1.4)

        screen.fill((0, 0, 0))
        x += random.randint(0, 700)
        y += random.randint(0, 200)
        screen.blit(numbers, (x, y))
        pygame.display.update()
    numbers = font.render(" ",1,(255,0,0),(0,0,0))
    clock.tick(1.4)
    screen.fill((0, 0, 0))
    screen.blit(numbers, (x, y))
    pygame.display.update()
    getInput(numList,numCount)
    return numList

def getInput(numList, newCount):
    newCount +=1
    inputList=[]
    while True:
        screen.fill((0, 0, 0))
        enter_nums_font=pygame.font.SysFont("Helvatica",32)
        enter_nums_mess=enter_nums_font.render("Enter Numbers:",True,(250,230,30))
        screen.blit(enter_nums_mess,(300,250))

        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:sys.exit()
            if event.type == pygame.KEYDOWN and len(inputList) < len(numList):
                if event.key==pygame.K_0:
                    inputList.append(0)
                if event.key == pygame.K_1:
                    inputList.append(1)
                if event.key==pygame.K_2:
                    inputList.append(2)
                if event.key==pygame.K_3:
                    inputList.append(3)
                if event.key==pygame.K_4:
                    inputList.append(4)
                if event.key==pygame.K_5:
                    inputList.append(5)
                if event.key==pygame.K_6:
                    inputList.append(6)
                if event.key==pygame.K_7:
                    inputList.append(7)
                if event.key==pygame.K_8:
                    inputList.append(8)
                if event.key==pygame.K_9:
                    inputList.append(9)

                if(len(inputList)==len(numList)):
                    for i in range (0, len(numList)):
                        if(numList[i]==inputList[i]):
                            gameWon = font.render("CONGRATS", 1, (255, 0, 0), (0, 0, 0))
                            clock.tick(1.4)
                            screen.fill((0, 0, 0))
                            screen.blit(gameWon, (100, 200))
                            pygame.display.update()
                            startGame(newCount)
                        else:
                            gameOver = font.render("OOPS YOU'RE WRONG",1,(255,0,0),(0,0,0))
                            clock.tick(1.4)
                            screen.fill((0, 0, 0))
                            screen.blit(gameOver, (100, 200))
                            pygame.display.update()
                            startGame(5)




        pygame.display.update()



while True:
    start = startGame(5)
    inp = getInput()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()

