# CS222 Project: Interactive Web-Based Escape Room Game

# Introduction

We build a website which simulates an escape room with a computer science theme. The website includes several interactive features that allow users to unlock and solve puzzles. By providing the correct input (from solving them correctly), users can earn points and then move to the next stage. The webpages' main display is powered by HTML (using CSS for appearance), its interactive features are powered by JavaScript, and the puzzles and score calculators are powered by JavaScript and Python. This project is an alternative to an existing idea (quiz form sites, such as Google Forms, which take in users' responses and provide custom feedback based on them, already exist); however, out project has additional features that connect with the feedback of an input answer (such as the changing number of points depending on the game's progress, and displaying certain features--like moving to next stage--only when the user earns them)

# Technical Architecture

## Summary of Components


## Diagram of Project Development

![alt text](https://github.com/CS222-UIUC/course-project-group-13/blob/main/TechnicalArchitectureDiagram.JPG)

# Installation Instructions

To run the website, follow these steps:
- Download the entire ZIP folder of the repository. To do this, on the Repository's home page, click the green "Code" button on the top right, click "Download Zip", and open the folder containing the Zip file on your computer (usually the "Downloads" folder). 
- Extract all the contents of the Zip file (extracting the Zip folder contents importwnt to ensure the interaction between different files, necessary for the hyperlinks and features, works as intended). Right click the Zip file, click Extract All, and follow the on-screen instructions.
- Click on the new folder (titled "course-project-group-13-main", and navigate to the course-project-group-13-main\course-project-group-13-main\website\templates folder
- Inside the templates folder, locate the "register.html" file. Open this file on a browser (Chrome or Firefox is preferred, with JavaScript enabled). Enter a username/password to create an account, then click Submit, and then login with the same username and password. 
  - If you would like to try this game out as a guest (without signing in to an account), open the "game-begin.html" file from the templates folder.
- After logging in, you should see a Welcome web page (if you are not redirected to this page automatically, open the "game-begin.html" file in the templates folder). Read the instructions on this page, then click "Click Here to Enter Room 1".

## Instructions to Play the Game

- Once in the Stage One webpage, read the directions near the top (just below the green box on the top), and click the "Start" button (located right below the stage's directions) to start the timer. Then start searching for clues and entering answers in text box (click Submit Answers after entering an answer). Be aware that many text box answers have limited submissions (the number of submissions available can be seen in the "Attempts" indicator in the green box near the top of the website). This green box can also be used to keep track of your score throughout. If you get an answer correct, the number of points will increase based on the number of attempts left. If you answer incorrectly, your number of attempts will decrease by 1 (so the number of points you earn for future puzzles will be less). Once you earn the minimum number of required points (at least 4 points for stage one, at least 7 for stage 2, and at least 4 for stage 3), you can then move on to the next stage by finding the "Go to Next Stage" hyperlink and clicking it. If your timer runs out, or you have zero attempts left, the game is over and you cannot solve any more puzzles. 


# Group Members and Roles
## Members
Rohith Sanjay (backend developer)

Stephanie Patterson: (frontend developer)

Sydney Liu: (backend developer)

## Work Distribution
Creating puzzles and functions in Python: Rohith

Organizing puzzles from Python: Stephanie

Creating log-in/account feature for website, and maintaining website security: Sydney

React/Framework for Website: Sydney

Writing Features in JavaScript (e.g. level changer and points counter): Rohith, Sydney

Creating and Implementing HTML Webpages: Stephanie, Rohith

CSS/Website Styling: Stephanie





