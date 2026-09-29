# Sequence Diagram

## Doctor Search

```text
User -> System: Select Find Doctor
User -> System: Enter problem
User -> System: Enter budget
System -> System: Identify specialization
System -> Doctors: Check specialization and fee
Doctors --> System: Matching result
System --> User: Display doctor / no suitable doctor
```

## Appointment Booking

```text
User -> System: Select Book Appointment
User -> System: Enter patient name and age
System --> User: Display doctors
User -> System: Enter doctor ID
System -> Doctors: Validate doctor ID
Doctors --> System: Valid / Invalid
System -> User: Request date and time
User -> System: Enter date and time
System -> Appointments: Store appointment
System --> User: Appointment booked successfully
```

## Appointment Cancellation

```text
User -> System: Select Cancel Appointment
User -> System: Enter patient name
System -> Appointments: Search patient
Appointments --> System: Match / No match
System -> Appointments: Remove matching record
System --> User: Cancellation result
