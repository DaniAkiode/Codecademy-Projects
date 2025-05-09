import time 

player_stats = {"Energy": 5,
                "Weapons": []}

def slow_print(text):
    for char in text: 
        print(char, end='', flush=True)
        time.sleep(0.01)
    print("\n")  

def into():
    slow_print("Welcome to the Mental Health Game!")
    slow_print("In this game, you will explore the inner world of you emotions.")
    slow_print("Prepare to be spiritually awakened. Starting with the Anxiety level")
    slow_print("Let's get started!")
    input("Enter to start the game...")
    anxietyLevel()
    

def anxietyLevel():
    slow_print("You're about to give a presentation.")
    slow_print("Your heart is pounding, your palms are sweaty, and you keep thinking, “What if I mess up? What if they laugh? What if I forget everything?”")
    slow_print("Everyone’s eyes are on you, and it feels like you can’t breathe properly")
    choice = input("What do you do?\n1. Take a deep breath and remind yourself that it's okay to be nervous.\n2. Avoid the presentation altogether.\n3. Practice your speech in front of a mirror.\n")
    while True:
        match choice:
            case "1":
                slow_print("You take a deep breath and remind yourself that it's okay to be nervous.")
                player_stats["Energy"] += 1
                break
            case "2":
                slow_print("You decide to avoid the presentation altogether.")
                player_stats["Energy"] -= 1
                break
            case "3":
                slow_print("You practice your speech in front of a mirror.")
                player_stats["Energy"] += 2
                break
            case _:
                slow_print("Invalid choice. Please try again.")
                choice = input("What do you do?")
    
def depresssionLevel():
    slow_print("You wake up and feel like you can't get out of bed.")
    slow_print("The world feels heavy, and you just want to hide away from everything.")
    choice = input("What do you do?\n1. Stay in bed all day.\n2. Call a friend and talk about how you're feeling.\n3. Go for a walk outside.\n")
    while True:
        match choice:
            case "1":
                slow_print("You stay in bed all day.")
                player_stats["Energy"] -= 2
                break
            case "2":
                slow_print("You call a friend and talk about how you're feeling.")
                player_stats["Energy"] += 1
                break
            case "3":
                slow_print("You go for a walk outside.")
                player_stats["Energy"] += 2
                break
            case _:
                slow_print("Invalid choice. Please try again.")
                choice = input("What do you do?")

def stressLevel():
    slow_print("You have a lot of work to do, and the deadline is approaching.")
    slow_print("You feel overwhelmed and don't know where to start.")
    choice = input("What do you do?\n1. Procrastinate and hope it goes away.\n2. Make a to-do list and tackle one task at a time.\n3. Ask for help from a colleague.\n")
    while True:
        match choice:
            case "1":
                slow_print("You procrastinate and hope it goes away.")
                player_stats["Energy"] -= 2
                break
            case "2":
                slow_print("You make a to-do list and tackle one task at a time.")
                player_stats["Energy"] += 2
                break
            case "3":
                slow_print("You ask for help from a colleague.")
                player_stats["Energy"] += 1
                break
            case _:
                slow_print("Invalid choice. Please try again.")
                choice = input("What do you do?")

def check_status():
    print(f"\nCurrent Clarity: {player_stats['energy']}")
    print(f"Tools: {', '.join(player_stats['weapons']) if player_stats['weapons'] else 'None'}")

def main():
    into()


if __name__ == "__main__":
    main()


