import random
import time

paragraphs = [
    "Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. It is the world's fifth-most populous country, with a population of 241.5 million people, and has the world's largest Muslim population as of 2023.",
    "India, officially the Republic of India, is a country in South Asia. It is the seventh-largest country by area; the most populous country as of June 2023; and from the time of its independence in 1947, the world's most populous democracy.",
    "England is a country that is part of the United Kingdom. It shares land borders with Wales to its west and Scotland to its north, while Ireland is located across the Irish Sea to its west and northwest, and the Celtic Sea lies to its southwest.",
    "Russia or the Russian Federation, is a country spanning Eastern Europe and Northern Asia. It is the largest country in the world by area, extends across eleven time zones, and shares land boundaries with fourteen countries. It is the world's ninth-most populous country and Europe's most populous country.",
]

def generate_random_paragraph():
    return random.choice(paragraphs)

def calculate_typing_speed(start_time, end_time, typed_text):

    elapsed_time = end_time - start_time
    

    words = len(typed_text.split())
    wpm = words / (elapsed_time / 60)
    return wpm

def main():
    print("Welcome to the Typing Speed Tester!")
    input("Press Enter to start...")
    
    while True:
        random_paragraph = generate_random_paragraph()
        
        print("\nType the following paragraph:")
        print(random_paragraph)
        
        input("Press Enter when you are ready to start typing...")
        start_time = time.time()
        
        typed_text = input()
        end_time = time.time()
        
        wpm = calculate_typing_speed(start_time, end_time, typed_text)
        
        print(f"\nYour typing speed: {wpm:.2f} WPM")
        
        restart = input("Do you want to try again? (yes/no): ")
        if restart.lower() != "yes":
            break

if __name__ == "__main__":
    main()
