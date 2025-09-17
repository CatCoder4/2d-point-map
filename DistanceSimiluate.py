import pygame


def Simulate(X, Y, B, C, E, ae, be, ce):
    # converts the X and Y of each point to pixels; using the scale factor of 25 pixel per 1 meter.

    ScaleFactor = 25
    Ap = ((X/2), (Y/2))
    # Y converted to negative because Pygame.
    Bp = (B[0] * ScaleFactor + Ap[0], (-B[1]) * ScaleFactor + Ap[1]) 
    Cp = (C[0] * ScaleFactor + Ap[0], (-C[1]) * ScaleFactor + Ap[1])
    Ep = (E[0] * ScaleFactor + Ap[0], (-E[1]) * ScaleFactor + Ap[1])


    # Draws the similutaion as a map using Pygame

    pygame.init()
    clock = pygame.time.Clock()
    pygame.font.init()
    font = pygame.font.SysFont(None, 24)
    screen = pygame.display.set_mode((X, Y))

    Acolor = (255, 0, 0)
    Bcolor = (0, 255, 0)
    Ccolor = (0, 0, 255)
    Ecolor = (255, 255, 255)

    animated_EA = [Ap[0], Ap[1]]
    animated_EB = [Bp[0], Bp[1]]
    animated_EC = [Cp[0], Cp[1]]


    def animate_E(stoppedA, stoppedB, stoppedC):
        # Move toward Ep gradually
        speed = 1

        if stoppedA == False:
            if animated_EA[0] < Ep[0]:
                animated_EA[0] += speed
            elif animated_EA[0] > Ep[0]:
                animated_EA[0] -= speed

            if animated_EA[1] < Ep[1]:
                animated_EA[1] += speed
            elif animated_EA[1] > Ep[1]:
                animated_EA[1] -= speed
            
            if animated_EA[0] == Ep[0] and animated_EA[1] == Ep[1]:
                stoppedA = True

        if stoppedB == False:
            if animated_EB[0] < Ep[0]:
                animated_EB[0] += speed
            elif animated_EB[0] > Ep[0]:
                animated_EB[0] -= speed

            if animated_EB[1] < Ep[1]:
                animated_EB[1] += speed
            elif animated_EB[1] > Ep[1]:
                animated_EB[1] -= speed
            
            if animated_EB[0] == Ep[0] and animated_EB[1] == Ep[1]:
                stoppedB = True

        if stoppedC == False:
            if animated_EC[0] < Ep[0]:
                animated_EC[0] += speed
            elif animated_EC[0] > Ep[0]:
                animated_EC[0] -= speed

            if animated_EC[1] < Ep[1]:
                animated_EC[1] += speed
            elif animated_EC[1] > Ep[1]:
                animated_EC[1] -= speed
            
            if animated_EC[0] == Ep[0] and animated_EC[1] == Ep[1]:
                stoppedC = True
        

        pygame.draw.rect(screen, Ecolor, [animated_EA[0], animated_EA[1], 10, 10], 5)
        pygame.draw.rect(screen, Ecolor, [animated_EB[0], animated_EB[1], 10, 10], 5)
        pygame.draw.rect(screen, Ecolor, [animated_EC[0], animated_EC[1], 10, 10], 5)



    # function to draw the points every frame
    def draw():
        # Draw points
        pygame.draw.rect(screen, Acolor, [Ap[0], Ap[1], 10, 10], 5)
        pygame.draw.rect(screen, Bcolor, [Bp[0], Bp[1], 10, 10], 5)
        pygame.draw.rect(screen, Ccolor, [Cp[0], Cp[1], 10, 10], 5)
        #pygame.draw.rect(screen, (255, 255, 255), [Ep[0], Ep[1], 10, 10], 5)
        stoppedA = False
        stoppedB = False
        stoppedC = False
        animate_E(stoppedA, stoppedB, stoppedC)


        # draw lines
        pygame.draw.line(screen, (255, 255, 0), Ap, Ep, 2)
        pygame.draw.line(screen, (255, 255, 0), Bp, Ep, 2)
        pygame.draw.line(screen, (255, 255, 0), Cp, Ep, 2)


        # draw labels
        screen.blit(font.render("A", True, Acolor), (Ap[0] - 15, Ap[1] + 15))
        screen.blit(font.render("B", True, Bcolor), (Bp[0] - 15, Bp[1] + 15))
        screen.blit(font.render("C", True, Ccolor), (Cp[0] - 15, Cp[1] + 15))
        screen.blit(font.render("E", True, Ecolor), (Ep[0] - 15, Ep[1] + 15))

        screen.blit(font.render(str(round(ae)), True, Acolor), ((Ap[0] + Ep[0])/2 - 15, (Ap[1] + Ep[1])/2 + 20))
        screen.blit(font.render(str(round(be)), True, Bcolor), ((Bp[0] + Ep[0])/2 - 15, (Bp[1] + Ep[1])/2 + 20))
        screen.blit(font.render(str(round(ce)), True, Ccolor), ((Cp[0] + Ep[0])/2 - 15, (Cp[1] + Ep[1])/2 + 20))



    # main loop of the similutaion.

    run = True
    while run:
        clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0, 0, 0))
        draw()

        
        pygame.display.update()


    pygame.quit()