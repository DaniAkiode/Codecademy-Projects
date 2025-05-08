import time 

player_stats = {"Energy": 5,
                "Weapons": []}

def slow_print(text):
    for char in text: 
        print(char, end='', flush=True)
        time.sleep(0.07)
    print("\n")  

def into():
    slow_print("Welcome to the Mental Health Game!")
    slow_print("In this game, you will be asked a series of questions to assess your mental health.")
    slow_print("Please answer honestly to get the most accurate results.")
    slow_print("Let's get started!")
    input("Enter to start the game...")
    anxietyLevel()
    

def anxietyLevel():
    slow_print("")
    slow_print("")

    while True:
        pass
    


    

def depresssionLevel():
    pass

def stressLevel():
    pass

def check_status():
    print(f"\nCurrent Clarity: {player_stats['energy']}")
    print(f"Tools: {', '.join(player_stats['weapons']) if player_stats['weapons'] else 'None'}")

def main():
    into()


if __name__ == "__main__":
    main()


