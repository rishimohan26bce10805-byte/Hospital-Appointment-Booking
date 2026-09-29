# Implementation Details

## Programming Language

Python 3.x

## Main Data Structures

### Doctors

```python
doctors = [
    ["D01", "Dr. Sharma", "General Physician", 400],
    ["D02", "Dr. Mehta", "Cardiologist", 800],
    ["D03", "Dr. Singh", "Dermatologist", 600],
    ["D04", "Dr. Verma", "Pediatrician", 500]
]
```

Each doctor record contains:

1. Doctor ID
2. Doctor name
3. Specialization
4. Consultation fee

### Appointments

```python
appointments = []
```

Each appointment contains:

1. Patient name
2. Patient age
3. Doctor name
4. Date
5. Time

## Functions

### `show_doctors()`
Loops through the doctor list and prints doctor information.

### `search_doctor()`
Reads the problem and budget, determines specialization from supported keywords and checks the doctor's fee.

### `book_appointment()`
Reads patient details, displays doctors, validates the doctor ID and appends a new appointment.

### `show_appointments()`
Checks whether appointments exist and prints each appointment.

### `cancel_appointment()`
Searches for a patient name without case sensitivity and removes the first matching appointment.

## Main Loop

The application uses:

```python
while True:
```

The loop continues until the user selects option 6.

## Current Input Handling

The code uses `input()` for all user interaction.

The budget is converted using:

```python
int(input("Enter your budget: "))
```

The current implementation does not catch non-numeric budget input or other runtime input errors.
