import json
import os

# Use script-relative path for data folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "students.json")


def ensure_data_folder():
    """Create data folder if it doesn't exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def load_students():
    """Load students from JSON file."""
    ensure_data_folder()
    
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print("Error while loading students:", e)
        return []


def save_students(students):
    """Save students to JSON file."""
    ensure_data_folder()
    
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(students, file, indent=4)
    except Exception as e:
        print("Error while saving students:", e)


def add_student():
    try:
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")

        students = load_students()
        
        new_student = {
            "id": student_id,
            "name": name,
            "age": age
        }
        
        students.append(new_student)
        save_students(students)

        print("Student record added successfully.")

    except Exception as e:
        print("Error while adding student:", e)


def view_students():
    try:
        students = load_students()

        if not students:
            print("No student records found.")
            return

        print("\nStudent Records:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

    except Exception as e:
        print("Error while reading records:", e)


def show_menu():
    print("\n--- Student Record Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
