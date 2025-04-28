import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",        # or your host
    user="root",              # your MySQL username
    password="@Parvez1221*", # your MySQL password
    database="course_management"
)

cursor = conn.cursor()


courses = []

def add_course():
    course_id = input("Enter Course ID: ")
    course_name = input("Enter Course Name: ")
    instructor = input("Enter Instructor Name: ")
    fees = input("Enter Academy fees (e.g., Rs:50000): ")
    duration = input("Enter Course Duration (e.g., 6 weeks): ")

    sql = "INSERT INTO courses (id, name, instructor, fees, duration) VALUES (%s, %s, %s, %s, %s)"
    val = (course_id, course_name, instructor, fees, duration)
    cursor.execute(sql, val)
    conn.commit()

    print("✅ Course added successfully.\n")



def view_courses():
    cursor.execute("SELECT * FROM courses")
    results = cursor.fetchall()

    if not results:
        print("❌ No courses available.\n")
        return

    print("\n📚 Course List:")
    for idx, course in enumerate(results, start=1):
        print(f"{idx}. ID: {course[0]} | Name: {course[1]} | Instructor: {course[2]} |Fees: {course[3]} |Duration: {course[4]}")
    print()

def delete_course():
    course_id = input("Enter Course ID to delete: ")
    sql = "DELETE FROM courses WHERE id = %s"
    val = (course_id,)
    cursor.execute(sql, val)
    conn.commit()

    if cursor.rowcount > 0:
        print("🗑 Course deleted.\n")
    else:
        print("❌ Course ID not found.\n")


def update_course():
    course_id = input("Enter Course ID to update: ")

    cursor.execute("SELECT * FROM courses WHERE id = %s", (course_id,))
    course = cursor.fetchone()

    if course:
        print("Leave field blank to keep current value.")

        new_name = input(f"Enter new Course Name (current: {course[1]}): ") or course[1]
        new_instructor = input(f"Enter new Instructor (current: {course[2]}): ") or course[2]
        new_fees = input(f"Enter new Fees (current: {course[3]}): ") or course[3]
        new_duration = input(f"Enter new Duration (current: {course[4]}): ") or course[4]

        sql = "UPDATE courses SET name=%s, instructor=%s, fees=%s, duration=%s WHERE id=%s"
        val = (new_name, new_instructor, new_fees, new_duration, course_id)
        cursor.execute(sql, val)
        conn.commit()

        print("🔄 Course updated.\n")
    else:
        print("❌ Course ID not found.\n")



def admin_menu():
    while True:
        print("📋 Course Administration Menu")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Delete Course")
        print("4. Update Course")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_course()
        elif choice == '2':
            view_courses()
        elif choice == '3':
            delete_course()
        elif choice == '4':
            update_course()
        elif choice == '5':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("⚠ Invalid option. Try again.\n")

if __name__ == "__main__":
    admin_menu()
    
if conn.is_connected():
    conn.close()
    print("✅ MySQL connection closed.")
