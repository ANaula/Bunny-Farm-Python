# Bunny Farm Simulation

##Purpose

This Python program was made to simulate a bunny farm over a long period of time. The simulation runs in real time and is organized into years and in each year information on each bunny is displayed as well as recorded in a text document. A grid is also displayed and recorded representing the pen the bunnies live in with each bunny being represented by a letter. The user is notified when a bunny is born, when one has passed away, when there is a culling, and when there is no where to move.  The simulation continues if there are living bunnies and ends when there are no more bunnies alive. 

## Simulation Rules

The simulation follows a set of rules that cover the bunnies and the bunny environment represented by the grid. Rules involving the bunnies include:
-	When a bunny is born, it has a 50/50 chance of being either male or female 
-	Their names are chosen at random from a name bank
-	There is a 2 percent chance that a bunny can be radioactive
-	Each bunny must have a unique identification number
-	Unless they are the starting bunnies, each bunny born must have their mother’s fur color
-	Once a bunny is two years or older, they will mate but a female can only have one bunny child per year
-	Normal bunnies will pass away when they are ten years old but radioactive bunnies don’t pass away until they are twenty
-	Radioactive bunnies cannot mate

Rules involving the bunny environment include:
-	A culling will occur when the bunny population reaches over twenty bunnies. Half the bunnies will be removed at random
-	A bunny mother cannot have a child if there is no space around her
-	Each bunny will move one space at any random direction if possible
-	If a bunny is next to a radioactive bunny, that bunny becomes radioactive
-	The user has the option each year to manually cull the population by pressing “k” when the prompt appears
-	On the grid, female and male bunnies under the age of two are represented by the letter’s “f” and “m”. Once they are over the age of two they are represented by “F” and “M”. Radioactive bunnies are represented by the letter “X” no matter their age. 

## How it works

The simulation runs on a linked list with the nodes being the bunnies themselves. There is a bunny class and a linked list class and both hold information and methods crucial to the running of the simulation. As mentioned earlier, the program runs in real time so each year is processed, outputted, and recorded one after the other. In each year, the year is stated and the grid is printed along with each bunny’s information. From there a function checks to see if there is any mating and another function checks the total population and culls if necessary. After that a series of functions focusing primarily on bunny information is run which ages them each by one year, checks to see if they get infected with radioactivity, updates their grid symbols if necessary and moves them one space in a random direction if possible. The linked list class variable that holds the current year is updated and there is a five second delay in which you could manually cull the population by pressing “k”. Finally a check is made to see if the simulation should end.

![Alt Text](https://media.giphy.com/media/lrgP4fwnz7t9zuNK9c/giphy.gif)

The program records all of this in a text file. In the repository, the text file "Bunny Year Activity.txt" is an example of what this program records.
