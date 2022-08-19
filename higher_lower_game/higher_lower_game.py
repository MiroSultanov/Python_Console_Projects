from art import logo, vs
from game_data import data
import random

def print_logo():
    print(logo)


def get_account_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}."


def check_correctness(choice, first_followers, second_followers):
    if choice == "A":
        return first_followers > second_followers
    elif choice == "B":
        return second_followers > first_followers


print_logo()

account_b = random.choice(data)

score = 0
while True:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {get_account_info(account_a)}.")
    print(vs)
    print(f"Against B: {get_account_info(account_b)}.")

    guess = input("Who has more followers? Type A or B? ").upper()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    if check_correctness(guess, a_followers, b_followers):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        break