
# CS110 Project Proposal
# Natural Selection Simulator
## CS 110 Final Project
### Year 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

Repo: [https://github.com/bucs110a0fall21/final-project-k-double-j.git](#) 

Slides: [https://docs.google.com/presentation/d/1cJtlRZfYWTsoZJ__z2utDis9vI0sh03tDEEuy6hhnFQ/edit?usp=sharing](#) 

### Team: K Double J
#### Jonathon Glatzer, Kieran O'Connor, Jerry Lai

***

## Project Description *(Software Lead)*
Our project is a natural selection simulator. It models how in nature those animals that blend in with the environment tend to survive more often than those that don't blend in. To do this, we had multiple dots of different colors, black, tan, and green. We give the user 20 seconds to click as many buttons as they can. In theory the buttons that are left over should be the ones that blend in the most. These dots that are left over would move on to the next round and that shows the process of evolution. At the end of the round, the game over screen shows the amount of buttons left over after the round, the amount of buttons that would be in the next round if another were to be played, and the results of the three previous games.

***    

## User Interface Design *(Front End Specialist)*
* Old GUI:
       ![class diagram](https://github.com/bucs110a0fall21/final-project-k-double-j/blob/334b127337b3bb46eebe59a1e2cf596dc8538c11/assets/KDoubleJ%20Project%20GUI%20Template%20Main%20Menu.jpg)
This is the old main menu screen. This has buttons to start the game, view the leaderboard and view the instructions. 
      ![class diagram](https://github.com/bucs110a0fall21/final-project-k-double-j/blob/334b127337b3bb46eebe59a1e2cf596dc8538c11/assets/Game%20Screen.jpg)
This is the old gameplay screen. It has a basic model of how the layout would look, with a title stamp and pressice escape to pause the game. 
   
   ![class diagram](https://github.com/bucs110a0fall21/final-project-k-double-j/blob/ba90d55261f29d3a6e4eac8ea1a04fc43bc30efc/assets/GAME%20OVER%20SCREEN.jpg)
     This is the old game over screen. It has the total number of dots that are left after each round with the option to play again. 
* Final GUI:
![class diagram](https://github.com/bucs110a0fall21/final-project-k-double-j/blob/19da25a963436e912e85a3a67f99737afd39d8a3/assets/newgamescreen.png)
This is the new game screen. It has a title, the current number of dots and seconds left.

![class diagram](https://github.com/bucs110a0fall21/final-project-k-double-j/blob/19da25a963436e912e85a3a67f99737afd39d8a3/assets/newendscreen.png)
This is the new end screen. It displays the leftover dots from the curent round, and the values for the dots left of the last three rounds. It also contains an explanation of what would happen if the round were to continue, as well as a credits line and evolution image.
***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * datetime library
    * https://docs.python.org/3/library/datetime.html
    *This library is responsible for allow the game to keep track of time. Using this module we were able to create a timer which ends the game when the timer reaches 0 seconds. 
* Class Interface Design
        * ![class diagram](https://github.com/bucs110a0fall21/final-project-k-double-j/blob/51deddb5df79ba153af76849a6dbeed6d0305315/assets/newclass.png)

    * Controller class- This class contains most of the code for the function. It creates the window and screen, groups all the sprites together, keeps track of how many dots are left, creates the timer, writes the dot data to the JSON file, creates the gameloop, eventloop, as well as the gameover loop. It also contains the code which tracks whether the mouse pointer clicks a dot and if so, that dot is removed from the screen. 
    *Shape class- This class is responsible for creating the dot sprite and rect objects. It also puts the dots in a random location on the screen each time a new game is played. 

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* src
    -Controller.py
    -Icon
    -Shape.py
    -foldercontents.txt
* foldercontent.txt
* result.json
* assets
    -GAME OVER SCREEN.jpg
    -Game Screen.jpg
    -KDoubleJ Class Diagram.jpg
    -KDoubleJ Project GUI Template Main Menu.jpg
    -class_diagram.jpg
    -evolution.png
    -green.jpg
    -newclass.png
    -newendscreen.png
    -newgamescreen.png
    -result.json
* etc
    -foldercontents.txt

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Kieran O'Connor

Worked as integration specialist by checking in with both the front and back end specialists to make sure everyone is on the same page. If there were problems that occurred within the joining of the two parts, I would look to see what the problem is and fix it.

### Front End Specialist - Jonathon Glatzer

Front-end lead conducted significant research on pygame, along with finding a module for time. They made sure that the GUI was pleasing to look at, as well as intuitive for the user. 

### Back End Specialist - Jerry Lai
Back End Specialist created the class forthe dots and made sure they fully integrated with the controller to have a fully working program. 

*Overall, all group members frequently met up to work on the project together and provide insight into each others tasks. 

## Testing *(Software Lead)*
* We went through coding the program, as we went along we knew that there would be some bugs. We finished the majority of the program and fixed the errors stated in the terminal. We tried to test little parts as we could, but we did not test very often in the beginning. We mostly tested during the final stages when there were bugs affecting the parts of the game that we could see. We tested the program and made fixes so that the program cannot be killed by user input. 

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Open the terminal through the menu bar within X2Go, type "python3 main.py" and press Enter  | Program Opens  |      Correct   |
|  2  | Click black dot  | Black dot is removed from screen and dot counter goes down |  Correct               |
|  3  | Click tan dot| Tan dot is removed from screen and counter dot goes down| Correct        |
|  4  | Click green dot | Green dot is removed from screen and dot counter goes down | Correct           |
|  5  | No user input needed, game automatically ends when time reaches 0 seconds | End game window is displayed with game information |   Correct       |
|  6  | Press the red "X" button in the top right to exit the program | Program window exits |   Correct       |


