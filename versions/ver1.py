import os
import random

def get_file_path(filename):
    if os.path.isfile(filename):
        print(f"Found {filename} in current directory.")
        return filename
    
    while True:
        path = input(f"{filename} not found in current directory. Please enter the full path to {filename}: ").strip()
        if os.path.isfile(path):
            return path
        else:
            print(f"File not found at {path}. Please try again.")

def load_names(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    surname_file = get_file_path("surname.txt")
    name_file = get_file_path("name.txt")

    surnames = load_names(surname_file)
    names = load_names(name_file)

    # Input validation for number of names, surnames, and people
    while True:
        try:
            num_names_per_person = int(input("How many names per person would you like to generate? "))
            num_surnames_per_person = int(input("How many surnames per person would you like to generate? "))
            num_people = int(input("How many people would you like to generate? "))
            if num_names_per_person > 0 and num_surnames_per_person > 0 and num_people > 0:
                break
            else:
                print("Please enter positive integers.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    print("\nGenerated random people:\n")

    for _ in range(num_people):
        # Sample without replacement if list is long enough, else with replacement
        chosen_names = random.sample(names, k=num_names_per_person) if len(names) >= num_names_per_person else [random.choice(names) for _ in range(num_names_per_person)]
        chosen_surnames = random.sample(surnames, k=num_surnames_per_person) if len(surnames) >= num_surnames_per_person else [random.choice(surnames) for _ in range(num_surnames_per_person)]

        full_name = " ".join(chosen_names + chosen_surnames)
        print(full_name)

if __name__ == "__main__":
    main()
