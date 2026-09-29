# Use Case Specification

## Primary Actor

**Patient / User**

## Use Cases

| ID | Use Case | Description |
|---|---|---|
| UC-01 | Show Doctors | View available doctors and fees. |
| UC-02 | Find Doctor | Find a suitable doctor based on problem and budget. |
| UC-03 | Book Appointment | Create an appointment with a valid doctor. |
| UC-04 | Show Appointments | View appointments stored during the session. |
| UC-05 | Cancel Appointment | Remove an appointment using patient name. |
| UC-06 | Exit | Terminate the application. |

## UC-02 Find Doctor

1. User selects Find Doctor.
2. System asks for problem.
3. User enters problem.
4. System asks for budget.
5. User enters budget.
6. System identifies specialization using supported keywords.
7. System checks doctors.
8. Matching doctor information is displayed, or no suitable doctor message is displayed.

## UC-03 Book Appointment

1. User selects Book Appointment.
2. System asks for patient name and age.
3. System displays doctors.
4. User enters doctor ID.
5. System validates the ID.
6. User enters appointment date and time.
7. System stores the appointment.
8. System displays confirmation.

## UC-05 Cancel Appointment

1. User selects Cancel Appointment.
2. User enters patient name.
3. System searches stored appointments.
4. Matching appointment is removed.
5. If no match exists, the system displays an appointment-not-found message.
