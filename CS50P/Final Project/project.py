import random
# Explaining the game to the user!
print("Hello Let's play hand cricket!")
print("It's a luck based game")
print("Minimum 2 players are needed for this game")
print("Rules are simple!")
print("There's a Batsman and a Bowler")
print("Batter and Bowler are decided by toss")
print("If the batter chooses the same number as the bowler, ", end="")
print("The Batsman is out!")
print("If the batsman chooses zero", end="")
print(", then the batsman get's the runs chosen by the bowler.")
print("In Toss numbers(1-6) are allowed")
print("In Game numbers(0-6) are allowed")

# The is_user() hosts the toss!
def is_user():
    w = input("Odd or Even: ").lower()
    if w not in ["odd","even"]:
        raise ValueError("Please enter valid input.")
    s = int(input("Pick a number (1-6):"))
    c = random.randint(1, 6)
    print("Opponent picked:", c)
    t = s + c
    if t%2 == 0:
        d ="even"
    else:
        d ="odd"
    print(f"{t} is {d}")

    return (w == "even" and t % 2 == 0) or (w == "odd" and t % 2 != 0)

#The toss() announces winner of the toss!
def toss():
    if is_user():
        print("You won the Toss!")
        return 0
    else:
        print("Opponent won the toss.")
        return 1

# user_batting1() runs when the user is batting first and hosts the first innings!
def user_batting1():
    user_score = 0
    while True:
        score = int(input("choose your score(0-6): "))
        c = random.randint(0, 6)
        print("Opponent picked:", c)

        if c != score:
            if score == 0:
                user_score += c
                print(f"Score: {user_score}")
            else:
                user_score += score
                print(f"Score: {user_score}")
        else:
            return user_score

# user_bowling2() runs when the user is bowling first and it also hosts the first innings!


# Only one of comp_batting1 runs when comp is batting first!

#clearly, user_batting1() and comp_batting1() is for first innings for the game!
def comp_batting1():
    opponent_score = 0
    while True:
        bowl = int(input("your choice(0-6): "))
        batt = random.randint(0, 6)
        print(f"Opponent chooses {batt}")

        if bowl != batt:
            if batt == 0:
                opponent_score += bowl
                print(f"Opponent Score: {opponent_score}")
            else:
                opponent_score += batt
                print(f"Opponent Score: {opponent_score}")

        else:
            return opponent_score
#user_batting2() runs when user batting second


def user_batting2(target):
    user_score = 0
    print(f"You need {target + 1} to win!")

    while True:
        score = int(input("choose your score(0-6): "))
        c = random.randint(0, 6)
        print("Opponent picked:", c)

        if c != score:
            if score == 0:
                user_score += c
                print(f"Score: {user_score}")
            else:
                user_score+= score
                print(f"Score: {user_score}")

            if user_score > target:
                return "You chased the target and you won the match!"
        else:
            return f"You are out! You lost by {target - user_score} and Opponent won the match!"
#comp_batting2() runs when comp is batting is second

# user_batting2() and comp_batting2() are for second innings of the game

def comp_batting2(target):
    opponent_score = 0
    print(f"Opponent needs {target + 1} to win")

    while True:
        bowl = int(input("your choice(0-6): "))
        batt = random.randint(0, 6)
        print(f"Opponent chooses {batt}")

        if bowl != batt:
            if batt == 0:
                opponent_score += bowl
                print(f"Opponent Score: {opponent_score}")
            else:
                opponent_score += batt
                print(f"Opponent Score: {opponent_score}")
            if opponent_score > target:
                return "Opponent chased the target and you lost!"
        else:
            return f"You got the wicket! Oppo scored {opponent_score}. You won the match!"

# game_choice1() calls the specific function(according to the toss) for the first innings of the game
def game_choice1():

    if toss() == 0:
        user_choice = input("Batting or Bowling: ").lower()
        if user_choice == "batting":
            score = user_batting1()
            return ("user_bat", score)
        else:
            score = comp_batting1()
            return ("user_bowl", score)
    else:
        oppo = random.choice(['batting', 'bowling'])
        print(f"Opponent chooses {oppo}")
        if oppo == "bowling":
            score = user_batting1()
            return ("user_bat", score)
        else:
            score = comp_batting1()
            return ("user_bowl", score)

#game_choice2() calls the specific function for the second innings of the game
def game_choice2():
    result, score = game_choice1()

    if result == "user_bat":
        print(comp_batting2(score))
    else:
        print(user_batting2(score))


def main():
    game_choice2()

def is_userlogic(w, s, c):
    t = s + c
    return (w == "even" and t % 2 == 0) or (w == "odd" and t % 2 != 0)


def battinglogic(user_score, score, c):
    if c == score:
        return user_score, True
    if score == 0:
        return user_score + c, False
    return user_score + score, False

def bowlinglogic(current_score, bowl, batt):
    if bowl == batt:
        return current_score, True
    if batt == 0:
        return current_score + bowl, False

    return current_score + batt, False

def chaselogic(current_score, target):
    return current_score > target

def tosslogic(choice, total):
    return (choice == "even" and total % 2 == 0) or (choice == "odd" and total % 2 != 0)





if __name__ == "__main__":
    main()
