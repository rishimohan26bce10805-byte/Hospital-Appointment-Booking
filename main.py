doctors = [
    ["D01", "Dr. Sharma", "General Physician", 400],
    ["D02", "Dr. Mehta", "Cardiologist", 800],
    ["D03", "Dr. Singh", "Dermatologist", 600],
    ["D04", "Dr. Verma", "Pediatrician", 500]
]

appointments = []


def show_doctors():
    print("\nAVAILABLE DOCTORS")

    for d in doctors:
        print("ID:", d[0])
        print("Name:", d[1])
        print("Specialization:", d[2])
        print("Fee: Rs.", d[3])
        print()


def search_doctor():
    print("\nFIND A DOCTOR")

    problem = input("Enter your problem: ").lower()
    budget = int(input("Enter your budget: "))

    specialization = ""

    if "heart" in problem:
        specialization = "Cardiologist"
    elif "skin" in problem:
        specialization = "Dermatologist"
    elif "child" in problem:
        specialization = "Pediatrician"
    elif "fever" in problem or "cold" in problem:
        specialization = "General Physician"

    found = False

    for d in doctors:
        if d[2] == specialization and d[3] <= budget:
            print("\nDoctor found")
            print("Name:", d[1])
            print("Specialization:", d[2])
            print("Fee: Rs.", d[3])
            found = True

    if found == False:
        print("No suitable doctor found.")


def book_appointment():
    print("\nBOOK APPOINTMENT")

    patient = input("Enter patient name: ")
    age = input("Enter patient age: ")

    show_doctors()

    doctor_id = input("Enter doctor ID: ").upper()

    doctor_found = False

    for d in doctors:
        if d[0] == doctor_id:
            date = input("Enter appointment date: ")
            time = input("Enter appointment time: ")

            new_appointment = [
                patient,
                age,
                d[1],
                date,
                time
            ]

            appointments.append(new_appointment)

            print("\nAppointment booked successfully.")
            doctor_found = True
            break

    if doctor_found == False:
        print("Doctor ID is not valid.")


def show_appointments():
    print("\nAPPOINTMENTS")

    if len(appointments) == 0:
        print("No appointments booked.")

    else:
        for a in appointments:
            print("\nPatient:", a[0])
            print("Age:", a[1])
            print("Doctor:", a[2])
            print("Date:", a[3])
            print("Time:", a[4])


def cancel_appointment():
    print("\nCANCEL APPOINTMENT")

    patient = input("Enter patient name: ")

    for a in appointments:
        if a[0].lower() == patient.lower():
            appointments.remove(a)
            print("Appointment cancelled.")
            return

    print("Appointment not found.")


while True:

    print("\n**********")
    print("HOSPITAL APPOINTMENT SYSTEM")
    print("**********")
    print("1. Show Doctors")
    print("2. Find Doctor")
    print("3. Book Appointment")
    print("4. Show Appointments")
    print("5. Cancel Appointment")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_doctors()

    elif choice == "2":
        search_doctor()

    elif choice == "3":
        book_appointment()

    elif choice == "4":
        show_appointments()

    elif choice == "5":
        cancel_appointment()

    elif choice == "6":
        print("Thank you for Coming.")
        break

    else:
        print("Invalid Data.")
