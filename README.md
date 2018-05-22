Snake Prototype
Candidate project for Python Course

## Setup Project
Adding Curses External Library
Adding pyGame External Library
NB, Try using both libraries will force a game logic and view layer separation

## Created Requirements.txt
In the terminal `pip install pygame`
`pip freeze > requirements.txt`

## Standard Curses Setup
Removed pygame for the moment.
Get game working, think about logic and view separately
Then logic can be used with any UI on top? :)
---
Standard Curses setup Made-
    but need a wrapper-
    if something breaks then because of the curses setup you wont see any useful de-bugging

## `curses.wrapper()`
Solves this issue and does all of the above resulting in:
+ Cleaner Code
+ Easier bug finding
+ Warm Fuzzies- much better

Documentation implies that it works inplace of the above code, but does not explicitly say so.

## Prove the Code Works
Quick `while` loop making sure the code is doing what we think it is.

## Print Using Curses

+ `stdscr.addstr`
+ `stdscr.refresh()`

## Get the Size Of Window

+ Add more text using `window.addstr`
+ A little while loop
+ next will bee setting the size of the window rather than just reading it.
+ resize terminal and check it is working
+ NOTE Curses has the paradigm y THEN x rather that the normal x,y order.

## Set Size Of Window

+ To play a game it would be great to have a set size window
+ Dynamic window size could be fun, but we'll keep it simple.
+ `curses.newwin()` and use set values of y and x
+ remember that we are talking about column height and row not pixels ;-)

## Fill Screen Space

+ Fill up window space with a symbol
+ Do it slowly so we can see it happen
+ column or row first doesn't matter

## Place "Food" In Random Place

+ Make piece of food appear every x secs

## Place Snake Head in Centre,  Add Border

+ using `window.box`
+ Place head in centre of play area

## Create and Use class snake()

+ Create a snake class
+ Place snake head from class

## Get User Input
+ Do something with user input for testing
