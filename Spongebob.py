import os
import json
from datetime import datetime
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import *
from time import *
from PIL import Image
from random import *
import sys

SCORES_FILE = 'scores.json'


def load_scores():
    """Load scores from the JSON file"""
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return []


def save_score(player_name, adventure, score):
    """Save a score to the JSON file"""
    scores = load_scores()
    scores.append({
        'player_name': player_name,
        'adventure': adventure,
        'score': score,
        'timestamp': datetime.now().isoformat()
    })
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=2)


def display_high_scores():
    """Display the top 10 high scores"""
    scores = load_scores()
    if not scores:
        print("\nNo high scores yet! Be the first to set a record!\n")
        return

    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:10]
    print("\n" + "=" * 50)
    print("           TOP 10 HIGH SCORES")
    print("=" * 50)
    for i, entry in enumerate(sorted_scores, 1):
        print(f"{i}. {entry['player_name']} - {entry['score']} points ({entry['adventure']})")
    print("=" * 50 + "\n")


def ask_to_save_score(player_name, adventure, score):
    """Ask the user if they want to save their score"""
    print(f"\nYour score: {score} points!")
    save_choice = input("Would you like to save your score? (y/n): ").lower()
    if save_choice == 'y':
        save_score(player_name, adventure, score)
        print("Score saved successfully!")
    else:
        print("Score not saved.")


def menu_sleep():
    # Sleep for 3.5 seconds during the menu presentation
    sleep(3.5)


def show_krabby_patty():
    # Opens image of a Krabby Patty
    with Image.open('Images/krabby_patty.png') as img:
        img.show()


def show_jellyfishing():
    # Opens image of Spongebob & Patrick jellyfishing in jelly fish fields
    with Image.open('Images/Jellyfishing.jpg') as img:
        img.show()


def show_karate():
    # Opens image of Spongebob in his karate gear
    with Image.open('Images/Karate.png') as img:
        img.show()


def play_again():
    """This function runs at the end of each adventure choice and
    asks the user if they'd like to play again"""
    play_again_input = input("Would you like to play again? Press q to quit, or press any key to go on another "
                             "adventure! ")

    if play_again_input == 'q':
        return False
    else:
        mixer.music.load('Songs/Menu_Music.mp3')
        mixer.music.play(-1)
        print("Yay! Let's play again!!")
        return True


def krusty_krab():
    """Adventure choice 1 - Make a Krabby Patty at the Krusty Krab
    This function runs when the user inputs 1 in the menu
    Returns the score based on performance"""
    mixer.music.load('Songs/krabby_patty.mp3')
    mixer.music.play(1)
    while mixer_music.get_busy():
        sleep(1)

    mixer.music.load('Songs/krusty_krab.mp3')
    mixer.music.play(-1)
    print("Hey, look! It's Mr. Krabs! ")
    sleep(2)
    print("Spongebob! Enough lolligagin' around me boy! It's time to make some krabby patties!")
    sleep(5)
    print("Mr. Krabs wants you to make krabby patties for some hungry customers!")
    sleep(4)
    print("To flip the patty, press 'f'. You'll know when it's ready!")
    sleep(3)
    print("Ready.....")
    sleep(2)
    print("Set.....")
    sleep(2)

    number_flips = randint(3, 7)
    while number_flips < 10:
        flip = input("Flip! ").lower()
        if flip == 'f':
            number_flips += 1
        elif flip == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            print("Wrong input! You need to press f to flip!")

    print("The krabby patty is cooked! Now we need to assemble it!")
    sleep(2)

    shown_ingredients = ['cheese', 'patty', 'pickles', 'ketchup', 'bottom bun', 'mustard', 'onions', 'top bun',
                         'tomato', 'lettuce']

    print("Place the below ingredients in the correct order to make a krabby patty! ")
    sleep(2)

    for shown_ingredient in shown_ingredients:
        print(shown_ingredient)
        sleep(1.5)

    correct_order_ingredients = ('bottom bun', 'patty', 'lettuce', 'cheese', 'onions', 'tomato', 'ketchup', 'mustard',
                                 'pickles', 'top bun')

    user_entered_ingredients = []

    user_input = input("Enter the first ingredient: ").lower()
    counter = 0
    wrong_input = 0

    while counter < 9:
        if user_input == correct_order_ingredients[counter]:
            counter += 1
            user_entered_ingredients.append(user_input)
            print(user_entered_ingredients)
            user_input = input("Correct! What's the next ingredient?! " + "\n").lower()
        elif user_input == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            wrong_input += 1
            user_input = input("Incorrect! Guess again! ")

    show_krabby_patty()

    print("Congratulations! You've made your first Krabby Patty!" + "\n")

    base_score = 100
    penalty = wrong_input * 10
    score = max(0, base_score - penalty)

    if wrong_input == 0:
        print("Wow - a perfect Krabby Patty on your first try! You deserve a promotion!" + "\n")
        score += 50
    elif wrong_input == 1:
        print("You only missed " + str(wrong_input) + " ingredient! You're a natural!" + "\n")
        score += 25
    elif 3 > wrong_input > 1:
        print("You only missed " + str(wrong_input) + " ingredients! You're a natural!" + "\n")
        score += 10
    elif 3 <= wrong_input < 6:
        print(str(wrong_input) + " missed ingredients - not bad!")
    else:
        print("You missed " + str(wrong_input) + " ingredients!")
        print("Mr. Krabs is not going to be happy - you need to brush up on your Krabby Patty training!")

    return score


def jellyfishing_patrick():
    """Adventure choice 2 - Go jellyfishing with Patrick
        This function runs when the user inputs 2 in the menu
        Returns the score based on performance"""
    mixer.init()
    mixer.music.load('Songs/Jellyfishing_Song.mp3')
    mixer.music.play(-1)

    print("Hey, look! It's Patrick! Hi Patrick! ")
    sleep(3)

    print("Hey Spongebob, are you ready to go jellyfishing?!")
    sleep(1)
    wrong_inputs = 0
    bring_net = input("Grab your net and enter 'go' to continue! ").lower()
    while bring_net != 'go':
        if bring_net == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            wrong_inputs += 1
            bring_net = input("Invalid input! Enter 'go' when you're ready! ").lower()

    print("Great! Let's go jellyfishing!")
    sleep(2)
    print("We have to keep running until we're close enough to catch a jellyfish.")
    sleep(4)
    print("Keep entering in 'r' to run until you're close enough to catch it.")
    sleep(4)
    print("When I tell you you're close enough, enter 'catch' to catch the jellyfish!")
    sleep(4)

    run_input = randint(5, 8)
    while run_input < 15:
        run = input("Run, Spongebob, run! ").lower()
        if run == 'r':
            run_input += 1
            if run_input == 14:
                print("You almost got it Spongebob!")
        elif run == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            wrong_inputs += 1
            print("Invalid input! You need to press r to run!")

    catch = input("Enter 'catch' to catch the jellyfish! ").lower()

    while catch != 'catch':
        wrong_inputs += 1
        catch = input("That won't work! Enter 'catch' to catch the jellyfish! ").lower()

    if catch:
        show_jellyfishing()

    print("Great job - you caught the jellyfish!")

    base_score = 100
    penalty = wrong_inputs * 5
    score = max(0, base_score - penalty)

    if wrong_inputs == 0:
        print("Perfect run! You're a natural jellyfish catcher!")
        score += 50

    return score


def sandy_karate():
    """Adventure choice 3 - Practice karate with Sandy
    This function runs when the user inputs 3 in the menu
    Returns the score based on performance"""
    mixer.music.load('Songs/Kung_Fu.mp3')
    mixer.music.play(-1)
    print("It's our old friend, Sandy Cheeks! Hi Sandy! ")
    sleep(2)

    print("Howdy Spongebob! We better high tail it to karate practice!")
    sleep(3)
    print("I hope you've been practicing your karate chopping skills! Let's go! ")
    sleep(3)

    wrong_inputs = 0
    hiya_continue = input("Enter 'hi-ya!' to continue! ").lower()
    while hiya_continue != 'hi-ya!':
        if hiya_continue == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            wrong_inputs += 1
            hiya_continue = input("Invalid input! Enter 'hi-ya!' to continue! ").lower()

    print("Ok Spongebob, let's try to chop this dang-fangled piece of wood in half.")
    sleep(3)
    print("Keep chopping until the piece of wood is chopped in half.")
    sleep(3)
    print("After you see 'HIIII-YAA!', enter 'chop' until you've chopped through the wood!")
    sleep(3.5)

    chop = " "
    chop_num = randint(5, 7)
    while chop_num < 15:
        chop = input("HIIII-YAA! ").lower()
        if chop == 'chop':
            chop_num += 1
            if chop_num == 14:
                print("By golly Spongebob, one more chop should do it!")
        elif chop == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            wrong_inputs += 1
            print("Invalid input! You need to enter 'chop' to to chop the wood in half!")

    if chop:
        show_karate()

    print("You did it! HIIII-YAAAA!!!")

    base_score = 100
    penalty = wrong_inputs * 5
    score = max(0, base_score - penalty)

    if wrong_inputs == 0:
        print("Perfect karate session! Sandy is impressed!")
        score += 50

    return score


mixer.init()

print("Welcome to the SpongeBob SquarePants Adventure Game! Let's get started!")
mixer.music.load('Songs/Theme_Song.mp3')
mixer.music.play()
while mixer.music.get_busy():
    sleep(11)
    print("Who lives in a pineapple under the sea?")
    print("Spongebob Squarepants!")
    sleep(3.5)
    print("Absorbant, and yellow, and porous is he")
    print("Spongebob Squarepants!")
    sleep(3.7)
    print("If nautical nonsense be something you wish")
    print("Spongebob Squarepants!")
    sleep(3.8)
    print("Then drop on the deck and flop like a fish")
    print("Spongebob Squarepants!")
    sleep(4)
    print("Spongebob Squarepants!")
    sleep(2.2)
    print("Spongebob Squarepants!")
    sleep(2.2)
    print("Spongebob Squarepants!")
    sleep(2.2)
    print("Spongebob Squarepants!")
    sleep(10)
    mixer.music.stop()

mixer.music.load('Songs/Menu_Music.mp3')
mixer.music.play(-1)

player_name = input("What's your name, adventurer? ")
print(f"\nWelcome, {player_name}! Let's go on an adventure!")
sleep(2)

print(
    "There are so many adventures to go on, but SpongeBob is super busy today and can only choose from 3 of them! "
    "Select a number to choose: ")
menu_sleep()
print("Press 1 to go work at the Krusty Krab")
menu_sleep()
print("Press 2 to go jellyfishing with Patrick")
menu_sleep()
print("Press 3 to practice karate with Sandy")
menu_sleep()
print("Press 4 to view High Scores")
menu_sleep()
print("To quit, just enter the letter q")
menu_sleep()

adventure_choice = ' '

while adventure_choice != 'q':

    adventure_choice = input("What adventure would you like to go on today?! ")

    if adventure_choice == str(1):
        score = krusty_krab()
        mixer.music.stop()
        ask_to_save_score(player_name, "Krusty Krab", score)
        if not play_again():
            sys.exit()
    elif adventure_choice == str(2):
        score = jellyfishing_patrick()
        mixer.music.stop()
        ask_to_save_score(player_name, "Jellyfishing", score)
        if not play_again():
            sys.exit()
    elif adventure_choice == str(3):
        score = sandy_karate()
        mixer.music.stop()
        ask_to_save_score(player_name, "Karate", score)
        if not play_again():
            sys.exit()
    elif adventure_choice == str(4):
        display_high_scores()
    elif adventure_choice == 'q':
        print("Thanks for playing, we hope you had fun!!")
        sys.exit()
    else:
        print("Invalid input!")
