students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")
    students.append({"name": name, "roll": roll, "branch": branch})
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n🎓 Student Records:")
    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']} | Roll: {s['roll']} | Branch: {s['branch']}")
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"\n🎯 Found: Name: {s['name']}, Roll: {s['roll']}, Branch: {s['branch']}\n")
            return
    print("❌ Student not found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for i, s in enumerate(students):
        if s['roll'] == roll:
            del students[i]
            print("🗑️ Student record deleted.\n")
            return
    print("❌ Student not found.\n")

def menu():
    while True:
        print("===== Student Management Menu =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.\n")

# Run the app
menu()
