# Hospital Appointment System – Project Statement

## 1. Problem Statement

Patients may need to find a suitable doctor according to their problem and budget and then manage an appointment. Manual handling of this information can be inconvenient.

The Hospital Appointment System provides a simple console-based solution for viewing available doctors, finding a doctor based on a problem and budget, booking appointments, viewing appointments and cancelling appointments.

## 2. Scope of the Project

### Included in Scope

The project includes:

1. Displaying available doctors.
2. Searching for a doctor using supported problem keywords.
3. Checking the doctor's fee against the user's budget.
4. Booking an appointment.
5. Validating the entered doctor ID.
6. Displaying booked appointments.
7. Cancelling an appointment using patient name.
8. Exiting the application.

### Outside the Current Scope

The current version does not include:

- Permanent database storage.
- Patient medical records.
- Online payment.
- Doctor login.
- Patient login.
- Real-time doctor availability.
- Online/web interface.
- Appointment reminders.

## 3. Target Users

The intended users are:

- Patients/users needing basic doctor information.
- Users wanting to book a simple appointment.
- Students learning Python.
- Teachers/instructors demonstrating programming concepts.
- Academic project evaluators.

## 4. High-Level Features

### 4.1 Show Doctors

Displays:

- Doctor ID
- Doctor name
- Specialization
- Consultation fee

### 4.2 Find Doctor

The user provides a problem and budget.

The program maps the following keywords:

- `heart` → Cardiologist
- `skin` → Dermatologist
- `child` → Pediatrician
- `fever` → General Physician
- `cold` → General Physician

The doctor is shown when the specialization matches and the fee is within the budget.

### 4.3 Book Appointment

The user provides:

- Patient name
- Patient age
- Doctor ID
- Appointment date
- Appointment time

The appointment is stored in the `appointments` list.

### 4.4 Show Appointments

Displays the currently stored patient name, age, doctor, date and time.

### 4.5 Cancel Appointment

The user enters a patient name. The program searches the appointment list and removes the first matching appointment.

## 5. Project Objectives

- Apply Python concepts to a practical problem.
- Use lists to store doctor and appointment data.
- Use functions to organize program operations.
- Implement a menu-driven workflow.
- Provide basic doctor matching.
- Implement appointment booking and cancellation.
- Demonstrate input, processing and output.

## 6. Functional Modules

The major functional modules are:

1. Doctor Listing Module
2. Doctor Search Module
3. Appointment Booking Module
4. Appointment Display Module
5. Appointment Cancellation Module
6. Main Menu / Exit Module

## 7. Expected Outcome

The expected outcome is a working Python console application in which the user can:

- View available doctors.
- Search for a suitable doctor.
- Book an appointment.
- View appointments.
- Cancel an appointment.
- Exit the application.

## 8. Data Storage

The current application uses in-memory Python lists.

Doctor records are stored in:

```python
doctors = [...]
```

Appointments are stored in:

```python
appointments = []
```

Appointments are therefore not retained after the program terminates.

## 9. Future Scope

The system can later be expanded with:

- SQL/database storage.
- Patient accounts.
- Doctor accounts.
- Doctor availability.
- Appointment rescheduling.
- Appointment IDs.
- Online payment.
- Notifications.
- Web/GUI interface.
- Advanced search.
- Automated tests.

## 10. Conclusion

The Hospital Appointment System is a compact educational project that applies Python programming concepts to a practical appointment-management problem. It provides core functionality for viewing doctors, finding doctors, booking appointments, viewing appointments and cancelling appointments through a console interface.
