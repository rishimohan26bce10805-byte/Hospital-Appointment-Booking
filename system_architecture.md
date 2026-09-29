# System Architecture

## Architecture Type

The application uses a simple single-process, console-based architecture.

```text
+----------------------+
|        User          |
+----------+-----------+
           |
           v
+----------------------+
| Console / Main Menu  |
|       app.py         |
+----------+-----------+
           |
     +-----+------+
     |            |
     v            v
+---------+   +----------------+
| Doctors |   | Appointment    |
|  List   |   | Management     |
+----+----+   +-------+--------+
     |                |
     +-------+--------+
             |
             v
       In-Memory Lists
```

## Components

### User Interface
Receives user input and displays results through the console.

### Main Controller
The `while True` loop displays the main menu and selects the requested operation.

### Doctor Data
The `doctors` nested list contains doctor ID, name, specialization and fee.

### Doctor Search
The `search_doctor()` function identifies a specialization using predefined keywords and applies the budget condition.

### Appointment Management
The booking, display and cancellation functions operate on the `appointments` list.

## Storage

No external database is used. All data remains in memory for the current program session.
