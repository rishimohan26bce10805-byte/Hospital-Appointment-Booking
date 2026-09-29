# Workflow

## Main Workflow

```text
START
  |
  v
Initialize doctors and appointments
  |
  v
Display Main Menu
  |
  +--> 1. Show Doctors
  |
  +--> 2. Find Doctor
  |
  +--> 3. Book Appointment
  |
  +--> 4. Show Appointments
  |
  +--> 5. Cancel Appointment
  |
  +--> 6. Exit --> END
  |
  +--> Invalid Choice
          |
          v
     Display Message
          |
          v
     Return to Menu
```

## Find Doctor Workflow

```text
Enter problem
      |
      v
Convert problem to lowercase
      |
      v
Check supported keywords
      |
      v
Determine specialization
      |
      v
Enter budget
      |
      v
Check specialization AND fee <= budget
      |
   +--+--+
   |     |
 Found  Not Found
   |     |
Display  Display
Doctor   "No suitable doctor found"
```

## Booking Workflow

```text
Enter patient name
       |
       v
Enter patient age
       |
       v
Display doctors
       |
       v
Enter doctor ID
       |
       v
Validate ID
   +---+---+
   |       |
 Valid   Invalid
   |       |
Enter     Error
date/time
   |
Store appointment
   |
Confirmation
```

## Cancellation Workflow

```text
Enter patient name
       |
       v
Search appointments
       |
   +---+---+
   |       |
 Found   Not Found
   |       |
Remove    Message
record
   |
Confirmation
```
