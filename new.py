import random

# List of truth questions
truth_questions = [
    "What's the most terrifying thing that's ever happened to you?",
    "What's the darkest secret you've ever kept?",
    "What's the most disturbing thing you've ever seen?",
    "What's the scariest thing you're afraid of?",
    "What's the most unsettling experience you've ever had?"
]

# List of dare tasks
dare_tasks = [
    "Go to the darkest corner of the room and scream at the top of your lungs.",
    "Tell a scary story to the group without looking at them.",
    "Walk around the room with your eyes closed and try to find your way back to your seat.",
    "Make a creepy face at the person to your left.",
    "Get up and do a creepy dance in front of the group."
]

# List of horror scenarios
horror_scenarios = [
    "You're trapped in a haunted mansion with no way out.",
    "You're being stalked by a serial killer.",
    "You're in a creepy asylum with no lights.",
    "You're on a deserted island with a mysterious figure lurking in the shadows.",
    "You're in a haunted carnival with creepy clowns everywhere."
]

def play_game():
    print("Welcome to Truth and Dare: Horror Edition!")
    print("You'll be presented with a series of truth questions, dare tasks, and horror scenarios.")
    print("You can choose to answer a truth question, complete a dare task, or face a horror scenario.")
    print("But be warned, the choices you make will determine your fate...")

    while True:
        choice = input("Do you want to answer a truth question (T), complete a dare task (D), or face a horror scenario (H)? ")

        if choice.upper() == "T":
            question = random.choice(truth_questions)
            print("Your truth question is:", question)
            answer = input("Answer: ")
            print("You've answered the question. You're safe for now...")
        elif choice.upper() == "D":
            task = random.choice(dare_tasks)
            print("Your dare task is:", task)
            input("Press enter when you're ready to complete the task...")
            print("You've completed the task. You're safe for now...")
        elif choice.upper() == "H":
            scenario = random.choice(horror_scenarios)
            print("You're facing a horror scenario:", scenario)
            input("Press enter to continue...")
            print("You've survived the scenario. But be warned, the next one might be worse...")
        else:
            print("Invalid choice. Try again!")

        play_again = input("Do you want to play again? (Y/N) ")

        if play_again.upper()!= "Y":
            break

    print("Thanks for playing Truth and Dare: Horror Edition!")

play_game()