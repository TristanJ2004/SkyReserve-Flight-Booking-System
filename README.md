✈️ SkyReserve Flight Booking System - Code Explanation
This Python script simulates a simple command-line flight booking system. It allows users to:

1. Search for available flights

2. Book a seat on a flight

3. View or cancel their bookings

📁 Data Structures
• flights: A list of dictionaries. Each dictionary contains:

• flight_no: Flight number (e.g., "FL001")

• destination: Destination of the flight (e.g., "New York")

• seats: A list of available seats (e.g., ["1A", "1B", "1C"])

• bookings: An initially empty list where each new booking (passenger info, flight, seat) will be stored.

🔍 Functions
display_flights()
• Displays all available flights with their numbers and destinations.

search_flight()
• Asks the user for a destination and displays matching flights.

book_flight()
• Allows the user to:

1. Choose a flight from the list.

2. Enter their name and contact.

3. Pick an available seat.

4. Confirm the booking (which removes the seat from availability and stores the booking in the bookings list).

• If a flight has no available seats, it informs the user.

view_booking()
• Lets the user enter their name and contact to retrieve a previous booking.

• If found, they can choose to cancel it, which will return the seat to the flight and remove the booking from the list.

post_action_prompt()
• After completing a task (booking, viewing, or cancelling), the user can:

• Return to the main menu

• Exit the program

main_menu()
• The central menu that offers users the following options:

1. Search Flights

2. Book a Flight

3. View Booking

4. Exit

skyreserve_start()
• The entry point of the system.

• Displays a welcome message and lets the user choose to enter the system or exit.

▶️ Program Flow
1. Program starts → skyreserve_start() is called.

2. User chooses to enter → main_menu() is launched.

3. From there, users can:

• Search for flights

• Book a flight

• View or cancel a booking

• Exit the system

🧠 Key Features
• Simple and user-friendly CLI interface

• Booking includes validation (e.g., valid flight and seat selection)

• Handles full bookings and invalid inputs

• Stores booking information until the program ends


