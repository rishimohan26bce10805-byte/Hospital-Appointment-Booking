# Component Diagram

```text
+------------------------------------------------+
|          Hospital Appointment System           |
+------------------------------------------------+
|                                                |
|  +------------------+                          |
|  |    Main Menu     |                          |
|  +--------+---------+                          |
|           |                                    |
|     +-----+------------------------------+     |
|     |            |            |           |     |
|     v            v            v           v     |
| +--------+  +---------+  +----------+ +------+ |
| | Doctor |  | Search  |  | Booking  | |Cancel| |
| | Listing|  | Doctor  |  |  Module  | | App. | |
| +---+----+  +----+----+  +----+-----+ +--+---+ |
|     |            |            |           |     |
|     +------------+------------+-----------+     |
|                       |                         |
|                       v                         |
|             +--------------------+              |
|             | In-Memory Data     |              |
|             | doctors            |              |
|             | appointments      |              |
|             +--------------------+              |
+------------------------------------------------+
```

## Main Components

- Main Menu
- Doctor Listing
- Doctor Search
- Appointment Booking
- Appointment Display
- Appointment Cancellation
- In-memory doctor and appointment data
