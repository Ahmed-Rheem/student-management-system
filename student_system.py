import os

# Database
students = {}


def load_data():
    if os.path.exists("students.txt"):
        f = open("students.txt", "r")
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                s_id = parts[0]
                name = parts[1]
                age = int(parts[2])
                courses_tuple = tuple(parts[3].split(","))
                students[s_id] = {
                    "name": name,
                    "age": age,
                    "courses": courses_tuple,
                }
        f.close()


def save_data():
    f = open("students.txt", "w")
    for s_id in students:
        s = students[s_id]
        courses_str = ",".join(s["courses"])
        f.write(s_id + "|" + s["name"] + "|" + str(s["age"]) + "|" + courses_str + "\n")
    f.close()
    print("Saved successfully!")


def add_student():
    print("\n--- Add Student ---")
    s_id = input("Enter ID: ")
    if s_id in students:
        print("This ID already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    c_input = input("Enter courses (separated by comma): ")

    # convert list to set to remove duplicates, then to tuple
    course_list = c_input.split(",")
    course_set = set(course_list)
    courses_tuple = tuple(course_set)

    students[s_id] = {"name": name, "age": age, "courses": courses_tuple}
    print("Student added!")


def view_students():
    print("\n--- All Students ---")
    if len(students) == 0:
        print("No students found.")
    else:
        for s_id in students:
            s = students[s_id]
            print(
                "ID:",
                s_id,
                "| Name:",
                s["name"],
                "| Age:",
                s["age"],
                "| Courses:",
                s["courses"],
            )


def search_student():
    print("\n--- Search ---")
    query = input("Enter ID or Name: ").lower()
    found = False
    for s_id in students:
        s = students[s_id]
        if s_id == query or query in s["name"].lower():
            print("Found -> ID:", s_id, "| Name:", s["name"], "| Age:", s["age"], "| Courses:", s["courses"])
            found = True
    if not found:
        print("Not found!")


def update_courses():
    print("\n--- Update Courses ---")
    s_id = input("Enter Student ID: ")
    if s_id not in students:
        print("ID not found!")
        return

    s = students[s_id]
    c_set = set(s["courses"])

    print("Current courses:", c_set)
    print("1. Add Course")
    print("2. Remove Course")
    choice = input("Choice (1/2): ")

    if choice == "1":
        new_c = input("Enter new course: ")
        c_set.add(new_c)
        s["courses"] = tuple(c_set)
        print("Course added!")
    elif choice == "2":
        rem_c = input("Enter course to remove: ")
        if rem_c in c_set:
            c_set.remove(rem_c)
            s["courses"] = tuple(c_set)
            print("Course removed!")
        else:
            print("Course not found!")


def delete_student():
    print("\n--- Delete Student ---")
    s_id = input("Enter ID: ")
    if s_id in students:
        del students[s_id]
        print("Student deleted!")
    else:
        print("ID not found!")


# Login Check
print("=== Login ===")
user = input("Username: ")
password = input("Password: ")

if user == "admin" and password == "1234":
    print("Welcome Admin!")
    load_data()

    while True:
        print("\n--- MENU ---")
        print("1. Add Student")
        print("2. View All")
        print("3. Search")
        print("4. Update Courses")
        print("5. Delete Student")
        print("6. Save & Exit")

        choice = input("Select: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_courses()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
else:
    print("Wrong username or password!")
