from src import Shape



import pygame
import random
import sys
import datetime
import json
class Controller:
    def __init__(self):
        """This function is responsible for initializing the various aspects of the game. It creates the window, sets the background, groups the dots into a sprite group, and sets the font and window size. 
Args: self"""
        self.window_width = 800
        self.window_height = 600
        self.state = "GAME"
        pygame.init()
        pygame.font.init()
        self.gameFont = pygame.font.SysFont('Comic Sans MS', 30)
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.endScreen = pygame.Surface((self.window_width, self.window_height))
        self.endScreen.fill((0, 76, 153 ))
        numDots = 6

        
        self.clock = pygame.time.Clock()
        self.time = 20000

        self.greenDot = pygame.sprite.Group()
        for dot in range(numDots):
            self.greenDot.add(Shape.Shape(Shape.GREEN, self.window_width, self.window_height))
        
        self.blackDot = pygame.sprite.Group()
        for dot in range(numDots):
            self.blackDot.add(Shape.Shape(Shape.BLACK, self.window_width, self.window_height))

        self.tanDot = pygame.sprite.Group()
        for dot in range(numDots):
            self.tanDot.add(Shape.Shape(Shape.TAN, self.window_width, self.window_height))

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add((i for i in self.greenDot), (i for i in self.blackDot), (i for i in self.tanDot))

        self.objects = []

    def SetBackground(self):
        """This function is responsible for loading the background image into the screen and drawing it to the correct dimensions.
Args: self
Returns: N/A"""
        self.green = pygame.image.load('assets/green.jpg').convert_alpha()
        self.green = pygame.transform.scale(self.green, (self.window_width, self.window_height))
        self.screen.blit(self.green, (0,0))
        
    def timeDisplay(self):
        """This function is responsible for setting the time parameters as well as drawing the time stamp to the window. 
Args: self
Returns: N/A"""
        seconds = self.time//1000
        minutes = seconds//60
        seconds = seconds%60
        
        time = self.gameFont.render(f"Time Left - Minutes: {minutes} Seconds: {seconds}"  , False, (255,255,0))
        self.screen.blit(time, (0,0))

    def numDotLbl(self,x=0,y=25):
        """This function is responsible for drawing the current number of dots left during the game.
Args: self, x value and y value for location of stamp
Returns: N/A"""
        numDotsLeft = self.gameFont.render(f"This Round - Green Dots: {len(self.greenDot)} Black Dots: {len(self.blackDot)} Tan Dots: {len(self.tanDot)}" , False, (255,255,0))
        self.screen.blit(numDotsLeft, (x,y))

    def title(self, x=525, y=0):
        """This function is responsible for drawing the title to the screen.
Args: self, x value and y value for location of stamp
Returns: N/A"""
        topTitle = self.gameFont.render("Natural Selection Simulator", False, (255,255,0))
        self.screen.blit(topTitle, (x,y))

    def credits(self, x=10, y=550):
        """This function is responsible for drawing the credits stamp to the screen.
Args: self, x value and y value for location of stamp
Returns: N/A"""
        creditText = self.gameFont.render("Created by Jonathon Glatzer, Jerry Lai, Kieran O'Connor", False, (255,255,0))
        self.screen.blit(creditText, (x,y))

    def endPic(self, x=10, y=250):
        """This function is responsible for drawing the end screens supplementary graphical image to the screen.
Args: self, x value and y value for location of stamp
Returns: N/A"""
        endPic = pygame.image.load('assets/evolution.png')
        self.screen.blit(endPic, (x,y))

    def mainLoop(self):
        """This functions defines the states of the game. While the game is running the state is 'GAME' and when the game ends the state is 'GAME OVER'.
Args: self
Returns: N/A"""
        while True:
            if self.state == "GAME":
                self.gameLoop()
            elif self.state == "GAME OVER":
                self.gameOverLoop()
            
    def gameLoop(self):
        """This function is responsible for executing the instructions that are involved while the game is running. These responsibilities are: ending the game when the timeer is less than or equal to 0, updating the count for all the dots, drawing the background and sprites, and drawing all of the title stamps to the screen.
Args: self
Returns: N/A"""
        self.clock.tick()
        self.time -= self.clock.get_rawtime()
        if self.time <= 0:
            self.state = "GAME OVER"

        self.eventloop()
        
        self.greenDot.update()
        self.blackDot.update()
        self.tanDot.update()
            
        self.SetBackground()
        self.all_sprites.draw(self.screen)
            
        self.timeDisplay()
        self.numDotLbl()
        self.title()
        pygame.display.flip()

    def gameOverLoop(self):
        """This function is responsible for executing the instructions for when the game is over. It consits of: drawing the end game screen, putting the end game image on the screen as well as all the title stamps, lists the rounds dot count as well as the previous 3 rounds dot count, and provides an explanation for the meaning behind the dot count. Lastly, this function also executes the code which save the previous game states and their dot count values in a JSON file. These values are then displayed in a list on the end screen which keeps data permanence. 
Args: Self
Returns: N/A"""
        if not self.objects:
            fptr = open("assets/result.json", "r")
            objects = json.load(fptr)
            fptr.close()

            endResult = {"green":len(self.greenDot), "black":len(self.blackDot), "tan":len(self.tanDot)}
            self.objects = objects
            objects = [endResult] + objects
            objects.pop()
            fptr = open("assets/result.json", "w")
            json.dump(objects, fptr)
            fptr.close()

        self.screen.blit(self.endScreen, (0,0))
        self.title(10,0)
        self.numDotLbl(10,50)
        numDotsLeft2 = self.gameFont.render(f"If the game were to continue", False, (255,255,0)) 
        self.screen.blit(numDotsLeft2, (10,150))
        numDotsLeft3 = self.gameFont.render(f"assuming that the leftover dots reproduce by a factor of 2", False, (255,255,0))
        self.screen.blit(numDotsLeft3, (10,175))
        numDotsLeft4 = self.gameFont.render(f"next round's values would be Green Dots: {len(self.greenDot)*2} Black Dots: {len(self.blackDot)*2} Tan Dots: {len(self.tanDot)*2}" , False, (255,255,0))
        self.screen.blit(numDotsLeft4, (10,200))
        oldGameHeader = self.gameFont.render("Previous Rounds", False, (255,255,0))
        self.screen.blit(oldGameHeader, (325,375))
        for i in range(len(self.objects)):
            tempString = ""
            if self.objects[i]:
                tempString = f"Green dot: {self.objects[i]['green']} Black dot: {self.objects[i]['black']} Tan dot: {self.objects[i]['tan']}"
            oldGame = self.gameFont.render(f"{i+1}: " + tempString, False, (255,255,0))
            self.screen.blit(oldGame, (325,400+i*25))
            

        self.credits()
        self.endPic()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        

    def eventloop(self):
        """This function handles the events for the game. It checks to see if the position of the mouse is within the bounds of the dot sprites and if it is, it kills that sprite. 
Args: self
Returns: N/A"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                collideList = [i for i in self.all_sprites if i.rect.collidepoint(pos)]
                for i in collideList:
                    i.kill()
            else:
                pass
            
