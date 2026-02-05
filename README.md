# Student Record Manager

A simple command-line Python application for managing student records using file-based storage.

## Features

- **Add Student**: Add new student records with ID, name, and age
- **View Students**: Display all stored student records
- **Persistent Storage**: All data is automatically saved and persisted

## Folder Structure

```
student-record-manager/
├── data/
│   └── students.json
├── README.md
└── student_manager.py
```

## Requirements

- Python 3.x
- No external dependencies required

## How to Run

1. Navigate to the project directory:
   ```bash
   cd student-record-manager
   ```

2. Run the application:
   ```bash
   python student_manager.py
   ```

## Usage

When you run the application, you'll see a menu with the following options:

```
--- Student Record Manager ---
1. Add Student
2. View Students
3. Exit
```

### Adding a Student

1. Select option `1`
2. Enter the student ID (e.g., 101)
3. Enter the student name (e.g., Rahul)
4. Enter the student age (e.g., 20)
5. The record will be saved automatically

### Viewing Students

1. Select option `2`
2. All student records will be displayed in the format:
   ```
   ID: 101, Name: Rahul, Age: 20
   ```

### Exiting

Select option `3` to exit the program.
