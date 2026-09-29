# Design Decisions

## 1. Console Interface

A console interface is used because the project is intended to demonstrate basic Python programming concepts without requiring external GUI frameworks.

## 2. List-Based Data Storage

The supplied implementation uses nested lists for doctors and a list for appointments. This matches the simple data requirements of the project.

## 3. Functions

Separate functions are used for the major operations:

- `show_doctors()`
- `search_doctor()`
- `book_appointment()`
- `show_appointments()`
- `cancel_appointment()`

This makes the code easier to understand and maintain.

## 4. Keyword-Based Doctor Search

The current project uses simple predefined keywords to map a problem to a specialization. This is intentionally simple and appropriate for a basic Python project.

## 5. In-Memory Storage

The current implementation does not use a database. Appointment information is stored in the `appointments` list while the program is running.

## 6. Doctor ID Validation

The booking process checks the entered doctor ID against the predefined doctor list before storing the appointment.

## 7. No External Libraries

The application uses only Python language features, making it easy to run in a standard Python 3.x environment.
