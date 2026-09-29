# Non-Functional Requirements

## 1. Usability
The system should provide a simple numbered console menu and clear prompts.

## 2. Performance
Operations should execute immediately for the small in-memory dataset used by the application.

## 3. Maintainability
Major operations are separated into functions such as `show_doctors()`, `search_doctor()`, `book_appointment()`, `show_appointments()` and `cancel_appointment()`.

## 4. Portability
The application should run on systems supporting Python 3.x without third-party packages.

## 5. Reliability
The system checks doctor IDs before booking and checks for an appointment before cancellation.

## 6. Resource Efficiency
The application uses simple Python lists and does not require external services.

## 7. Error Handling
The current implementation handles invalid menu choices, invalid doctor IDs and missing appointments through messages. Comprehensive exception handling for invalid numeric input is not implemented.
