
### Video Demo  
  
(https://youtu.be/cf-J-Q293Jg?si=pBrIjOjMBS_2Jlc_)  
  
### Description  
  
This project is a command-line Hand Cricket game implemented in Python.  
It simulates a traditional hand cricket match between a user and the computer using random number generation. The game includes a toss system, batting and bowling mechanics, and two innings with a chase, making it fully interactive and luck-based.  
  
The user plays against the computer, where both choose numbers according to the rules of hand cricket. If both choose the same number, the batsman is out. Special logic is applied when zero is chosen, closely resembling real hand cricket rules.  
  
### Files  
  
- project.py – Contains the complete game logic and execution flow   
- README.md – Project documentation  
  
### Libraries Used  
  
- random  
- Used to generate the computer’s choices during the toss, batting, and bowling.    
- No third-party libraries are required.  
  
### How to Run  
  
- Ensure you have Python 3 installed.   
- Run the program using:   
- python project.py  
  
### Game Rules  
  
Minimum 2 players (User vs Computer)  
  
#### Toss:  
  
- User selects Odd or Even  
- Both choose a number from 1–6  
  
#### Game:  

- Numbers allowed: 0–6  
- Same number chosen → Batsman is out  
- If batsman chooses 0, runs equal the opponent’s number  
  
### Game Flow  

#### Toss
  
- The user participates in an odd-or-even toss.  
- The winner decides whether to bat or bowl first.  
  
#### First Innings  
  
- The batting side scores runs until they get out.  
- Score is accumulated based on game rules.  
#### Second Innings  
  
- A target is set.  
- The second batting side attempts to chase the target.   
- The match ends when:    
- The target is successfully chased, or The batsman gets out.  
  
### Design Choices  
  
- The game is split into clear functional units for toss, batting, bowling, and chasing.   
- Helper logic functions are separated from input/output to improve readability and testability. 
- Randomization is used to fairly simulate an opponent.  
- The game runs fully in the terminal without external dependencies.  
  
### Functions Overview  

#### Toss Functions  
  
- is_user() – Handles user interaction for the toss.  
- toss() – Determines and announces the toss winner.  

#### Batting & Bowling  

- user_batting1() – User bats first.    
- comp_batting1() – Computer bats first.   
- user_batting2(target) – User chases the target.   
- comp_batting2(target) – Computer chases the target.  

#### Game Control  
  
- game_choice1() – Handles first innings decision.  
- game_choice2() – Controls second innings and prints result.    
- main() – Entry point of the program.   

#### Logic Helper Functions  
  
- is_userlogic()   
- battinglogic()  
- bowlinglogic()
