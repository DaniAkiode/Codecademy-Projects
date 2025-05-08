import time 

player_stats = {"Clarty": 5,
                "Arsenal": []}

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

def anxietyLevel():
    pass

def depresssionLevel():
    pass

def stressLevel():
    pass

def check_status():
    pass

def main():
    into()


if __name__ == "__main__":
    main()
