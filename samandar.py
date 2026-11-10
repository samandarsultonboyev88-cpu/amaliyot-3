
import csv
import os

FILE = "students.csv"

# Fayl mavjud bo'lmasa, yaratish
if not os.path.exists(FILE):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Ism", "Familiya", "Yosh", "Ball"])


def read_students():
    with open(FILE, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def add_student():
    students = read_students()
    new_id = max([int(s["ID"]) for s in students], default=0) + 1

    ism = input("Ism: ")
    familiya = input("Familiya: ")
    yosh = int(input("Yosh: "))
    ball = float(input("Ball: "))

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, ism, familiya, yosh, ball])

    print("O'quvchi qo'shildi!")


def show_students():
    students = read_students()

    if not students:
        print("O'quvchilar mavjud emas!")
        return

    for s in students:
        print(s)


def search_student():
    student_id = input("O'quvchi ID sini kiriting: ")

    for s in read_students():
        if s["ID"] == student_id:
            print(s)
            return

    print("O'quvchi topilmadi!")


def edit_student():
    students = read_students()
    student_id = input("Tahrirlash uchun ID: ")

    for s in students:
        if s["ID"] == student_id:
            print("Yangi ma'lumotlarni kiriting:")
            s["Ism"] = input("Ism: ")
            s["Familiya"] = input("Familiya: ")
            s["Yosh"] = input("Yosh: ")
            s["Ball"] = input("Ball: ")

            with open(FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["ID", "Ism", "Familiya", "Yosh", "Ball"]
                )
                writer.writeheader()
                writer.writerows(students)

            print("Ma'lumotlar yangilandi!")
            return

    print("O'quvchi topilmadi!")


def delete_student():
    students = read_students()
    student_id = input("O'chirish uchun ID: ")

    new_students = [s for s in students if s["ID"] != student_id]

    if len(new_students) == len(students):
        print("O'quvchi topilmadi!")
        return

    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["ID", "Ism", "Familiya", "Yosh", "Ball"]
        )
        writer.writeheader()
        writer.writerows(new_students)

    print("O'quvchi o'chirildi!")


def highest_score():
    students = read_students()

    if not students:
        print("O'quvchilar mavjud emas!")
        return

    best = max(students, key=lambda s: float(s["Ball"]))
    print("Eng yuqori ball olgan o'quvchi:", best)


def average_score():
    students = read_students()

    if not students:
        print("O'quvchilar mavjud emas!")
        return

    avg = sum(float(s["Ball"]) for s in students) / len(students)
    print("O'rtacha ball:", round(avg, 2))


while True:
    print("\n===== O'QUVCHILAR TIZIMI =====")
    print("1. O'quvchi qo'shish")
    print("2. Barcha o'quvchilar")
    print("3. ID orqali qidirish")
    print("4. Ma'lumotni tahrirlash")
    print("5. O'quvchini o'chirish")
    print("6. Eng yuqori ball")
    print("7. O'rtacha ball")
    print("0. Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        edit_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        highest_score()
    elif choice == "7":
        average_score()
    elif choice == "0":
        print("Dastur tugadi!")
        break
    else:
        print("Noto'g'ri tanlov!")
