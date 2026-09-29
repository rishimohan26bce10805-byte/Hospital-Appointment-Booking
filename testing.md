# Testing

## Test Environment

- Python 3.x
- Command-line terminal
- No external packages

## Functional Test Cases

| ID | Test Case | Input / Action | Expected Result |
|---|---|---|---|
| T01 | Show doctors | Select `1` | Four doctors are displayed |
| T02 | Find cardiologist | Problem `heart`, budget `800` | Dr. Mehta is displayed |
| T03 | Find cardiologist below budget | Problem `heart`, budget `500` | No suitable doctor |
| T04 | Find dermatologist | Problem `skin`, budget `600` | Dr. Singh is displayed |
| T05 | Find pediatrician | Problem `child`, budget `500` | Dr. Verma is displayed |
| T06 | Find general physician | Problem `fever`, budget `400` | Dr. Sharma is displayed |
| T07 | Find general physician using cold | Problem `cold`, budget `400` | Dr. Sharma is displayed |
| T08 | Book valid appointment | Doctor ID `D01` | Appointment booked |
| T09 | Book invalid appointment | Doctor ID `D99` | Invalid doctor ID message |
| T10 | Show empty appointments | Select `4` before booking | No appointments booked |
| T11 | Show booked appointments | Select `4` after booking | Appointment details displayed |
| T12 | Cancel existing appointment | Enter matching patient name | Appointment cancelled |
| T13 | Cancel missing appointment | Enter unknown patient | Appointment not found |
| T14 | Invalid menu choice | Enter `9` | Invalid Data message |
| T15 | Exit | Select `6` | Application terminates |

## Edge Cases

- Problem does not contain a supported keyword.
- Budget is lower than all matching doctors.
- Invalid doctor ID.
- No appointments exist.
- Patient name is entered with different capitalization.
- Invalid menu option.
- Non-numeric budget input.

## Current Limitations Identified by Testing

The supplied code does not explicitly handle non-numeric budget input. Such input can raise a Python `ValueError`.

The system also does not validate appointment date/time formats or patient age.
