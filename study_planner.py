# TIME MANAGEMENT ASSISTANT FOR STUDENT
# Student: Nishtha sahu , Reg. no.:25BEY10015

import os
import sys
from datetime import datetime

# --- CONFIGURATION ---
# The file where your data is saved automatically
DATABASE_FILE = "planner_data.txt"

# List to store your academic goals
academic_goals = []

def clean_screen():
    """Clears the terminal screen for a better look."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_database():
    """Loads existing tasks from the text file."""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as f:
            lines = f.readlines()
            for line in lines:
                # We expect the format: Subject | Details | Date
                parts = line.strip().split("|")
                if len(parts) == 3:
                    task = {
                        "subject": parts[0].strip(),
                        "details": parts[1].strip(),
                        "date": parts[2].strip()
                    }
                    academic_goals.append(task)

def save_database():
    """Saves the current list to the text file."""
    with open(DATABASE_FILE, "w") as f:
        for item in academic_goals:
            line = f"{item['subject']} | {item['details']} | {item['date']}\n"
            f.write(line)

def log_new_session():
    """Function to add a new study task."""
    clean_screen()
    print("=== LOG NEW STUDY SESSION ===")
    
    sub = input("Enter Subject (e.g., Math): ")
    desc = input("Enter Topic/Details: ")
    
    # Auto-generate today's date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    new_entry = {
        "subject": sub,
        "details": desc,
        "date": current_date
    }
    
    academic_goals.append(new_entry)
    save_database()
    print("\n[SUCCESS] Session logged successfully!")
    input("Press Enter to continue...")

def show_all_goals():
    """Function to view the schedule."""
    clean_screen()
    print("=== MY ACADEMIC SCHEDULE ===")
    
    if not academic_goals:
        print("\n[INFO] No study sessions found.")
    else:
        print(f"{'ID':<5} {'Date':<12} {'Subject':<15} {'Topic'}")
        print("-" * 60)
        
        for index, item in enumerate(academic_goals):
            print(f"{index + 1:<5} {item['date']:<12} {item['subject']:<15} {item['details']}")
            
    print("-" * 60)
    input("Press Enter to go back...")

def remove_goal():
    """Function to delete a finished task."""
    clean_screen()
    print("=== MARK TASK AS COMPLETE ===")
    
    if not academic_goals:
        print("[INFO] Nothing to remove.")
        input("Press Enter...")
        return

    # Show list so user knows what number to pick
    for index, item in enumerate(academic_goals):
        print(f"{index + 1}. {item['subject']} - {item['details']}")
    
    print("\n")
    try:
        choice = int(input("Enter the ID number to remove: "))
        if 1 <= choice <= len(academic_goals):
            removed = academic_goals.pop(choice - 1)
            save_database()
            print(f"\n[REMOVED] Finished: {removed['subject']}")
        else:
            print("[ERROR] Invalid ID number.")
    except ValueError:
        print("[ERROR] Please enter numbers only.")
        
    input("Press Enter to continue...")

def start_application():
    """Main loop of the program."""
    load_database()
    
    while True:
        clean_screen()
        print("###################################")
        print("#    STUDENT PLANNER TOOL v2.0    #")
        print("###################################")
        print(" [ 1 ] Add New Study Goal")
        print(" [ 2 ] View All Goals")
        print(" [ 3 ] Mark Goal as Done")
        print(" [ 4 ] Exit System")
        print("###################################")
        
        user_choice = input("Select Option: ")
        
        if user_choice == '1':
            log_new_session()
        elif user_choice == '2':
            show_all_goals()
        elif user_choice == '3':
            remove_goal()
        elif user_choice == '4':
            print("Exiting... Good luck with your studies!")
            sys.exit()
        else:
            print("Invalid selection. Try again.")

# Run the app
start_application()