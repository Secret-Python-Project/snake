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
