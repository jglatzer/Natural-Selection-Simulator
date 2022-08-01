from src import Controller
import pygame

def main2():
    pygame.init()
    team = {"lead": "Kieran O'Connor", "backend": "Jerry Lai", "frontend": "Jonathon Glatzer"}
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:" , team["frontend"])


#main()
def main():

    game = Controller.Controller()
    game.mainLoop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
