import pygame, sys
import ML as ml
import main as m
import PatternFinder as pf
import numpy as np
from enum import Enum

pygame.init()

class PositionType(Enum):
    BASE = 1
    CENTER = 2
    OFFSET = 3
    XOFFSET = 4

#screen
screenWidth = 400
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight) ,pygame.SCALED)

#Colors
white = (255,255,255)
smallWhite = (238,238,238)
black = (0,0,0)
gray = (210, 210, 210)
lightBlue = (145, 193, 225)
darkGray = (169,169,169)
gold = (255,215,0)
silver = (192, 192, 192)
bronze = (110, 77, 37)

#Input
player_inputField = ''

#TEXT
playerInput = "Input:  "
accText = "Accuracy: "
aiText = "AI Guess: "
rightText = "Right: "
guessesText = "Guesses: "

scene = "game"
newScene = ""

#Button
buttonRect = pygame.Rect(100,500, 200, 50)

highscores = ["1: ","2: ","3: ","4: ","5: ","6: ","7: ","8: ","9: ","10: "]

inputed = []
patternFinder, nn = m.initalizeNewGame()
acc = 0
right = 0.0

f = open("humanInput.txt", "a")
f.write('\n \n')


def predict():
    global input, nn, patternFinder, acc, accText, playerInput, aiText, right, rightText, guessesText
    inputs = np.array(m.get_last_three_elements(inputed)).reshape(1, -1)
    aiConfidence = nn.predictRaw(inputs)
    depthNumber, patternDepth = patternFinder.aritmeticPredictor(inputed, 4)
    number, numberConfidence = patternFinder.strictPatternPredictor(inputed, 15)

    guess = np.argmax(aiConfidence)
    if (numberConfidence > 1):#confidence is very high meaning it probely is a pattern
        guess = number
    elif (patternDepth >= 3): #3 numbers has been incresing contunisly in a direction example 1,2,3
        guess = depthNumber
    elif (len(inputed) == 0):
        guess = 7

    if (input == guess):
        right = right + 1

    print(guess)
    
    inputed.append(input)
    f.write(str(input) + ", ")

    acc = right/len(inputed)
    accText = "Accuracy: " + str(round(acc*100, 3)) + "%"
    playerInput = "Input:  " + str(input)
    aiText = "AI Guess: " + str(guess)
    rightText = "Guessed Right: " + str(int(right))
    guessesText = "Gusses: " + str(len(inputed))

    
    

def renderText(text, screen, font_size, color, posType, parent, offsetX, offsetY):
    font = pygame.font.Font(None, font_size)
    text = font.render(text, True, color)

    if (posType == PositionType.BASE):
        screen.blit(text, (0,0))
    elif (posType == PositionType.CENTER):
        screen.blit(text, (parent.centerx-text.get_width()/2 + offsetX, parent.centery-text.get_height()/2 + offsetY))
    elif (posType == PositionType.OFFSET):
        screen.blit(text, (offsetX, offsetY))
    elif (posType == PositionType.XOFFSET):
        screen.blit(text, (screenWidth/2-text.get_width()/2 + offsetX, offsetY))

def changeSceneButton(inputScene, rect, buttonColor, text, screen, font_size, textColor):
    global newScene
    pygame.draw.rect(screen, buttonColor, rect)

    renderText(text, screen, font_size, textColor, PositionType.CENTER, rect, 0,0)
    newScene = inputScene
    

run = True
while run:    
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(smallWhite)

    if scene == "game":
        #Input text
        inputrect = pygame.Rect(100,100, 200, 32)
        pygame.draw.rect(screen, darkGray, inputrect)

        renderText("ARE YOU PREDICTABLE?", screen, 32, black, PositionType.XOFFSET, None, 0,30)
        renderText(player_inputField, screen, 32, black, PositionType.CENTER, inputrect, 0,0)
        renderText("Please only enter in a number 1-9", screen, 18, gray, PositionType.CENTER, inputrect, 0,25)

        renderText(aiText, screen, 32, black, PositionType.XOFFSET, None, 0,200)
        renderText(playerInput, screen, 32, black, PositionType.XOFFSET, None, 0,230)
        renderText(accText, screen, 32, black, PositionType.XOFFSET, None, 0,260)
        renderText(rightText, screen, 32, black, PositionType.XOFFSET, None, 0,290)
        renderText(guessesText, screen, 32, black, PositionType.XOFFSET, None, 0,320)

        changeSceneButton("Highscores", buttonRect, lightBlue, "Highscores", screen, 32, black)
    elif scene == "Highscores":
        renderText("ARE YOU PREDICTABLE?", screen, 32, black, PositionType.XOFFSET, None, 0,30)
        renderText("Highscores", screen, 28, black, PositionType.XOFFSET, None, 0,60)

        renderText(highscores[0], screen, 65, gold, PositionType.XOFFSET, None, 0,85)
        renderText(highscores[1], screen, 63, silver, PositionType.XOFFSET, None, 0,135)
        renderText(highscores[2], screen, 61, bronze, PositionType.XOFFSET, None, 0,185)
        renderText(highscores[3], screen, 58, black, PositionType.XOFFSET, None, 0,235)
        renderText(highscores[4], screen, 58, black, PositionType.XOFFSET, None, 0,285)
        renderText(highscores[5], screen, 58, black, PositionType.XOFFSET, None, 0,335)
        renderText(highscores[6], screen, 58, black, PositionType.XOFFSET, None, 0,385)
        renderText(highscores[7], screen, 58, black, PositionType.XOFFSET, None, 0,435)
        renderText(highscores[8], screen, 58, black, PositionType.XOFFSET, None, 0,485)
        renderText(highscores[9], screen, 58, black, PositionType.XOFFSET, None, 0,535)
            



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                player_inputField = player_inputField[0:-1]
            elif event.key == pygame.K_RETURN:
                if len(player_inputField) == 1:
                    
                    predict()
                    playerInput = playerInput[0:-1]
                    playerInput += player_inputField

                    player_inputField = ''
                    input = 0

            elif len(player_inputField) >= 1:
                pass
            elif event.key == pygame.K_1:
                player_inputField += '1'
                input = 1
            elif event.key == pygame.K_2:
                player_inputField += '2'
                input = 2
            elif event.key == pygame.K_3:
                player_inputField += '3'
                input = 3
            elif event.key == pygame.K_4:
                player_inputField += '4'
                input = 4
            elif event.key == pygame.K_5:
                player_inputField += '5'
                input = 5
            elif event.key == pygame.K_6:
                player_inputField += '6'
                input = 6
            elif event.key == pygame.K_7:
                player_inputField += '7'
                input = 7
            elif event.key == pygame.K_8:
                player_inputField += '8'
                input = 8
            elif event.key == pygame.K_9:
                player_inputField += '9' 
                input = 9
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonRect.collidepoint(mouse_pos):
                scene = newScene
    pygame.display.flip()   


f.close()
pygame.quit()
