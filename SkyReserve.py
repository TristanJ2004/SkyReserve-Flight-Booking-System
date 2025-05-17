import sys

flights = [
    {"flight_no": "FL001", "destination": "New York", "seats": ["1A", "1B", "1C"]},
    {"flight_no": "FL002", "destination": "London", "seats": ["2A", "2B", "2C"]},
    {"flight_no": "FL003", "destination": "Tokyo", "seats": ["3A", "3B", "3C"]}
]

bookings = []

def display_flights():
    print("\nAvailable Flights:")
    for i, flight in enumerate(flights, 1):
        print(f"{i}. Flight No: {flight['flight_no']} to {flight['destination']}")

def search_flight():
    destination = input("Enter destination to search: ")
    print("\nMatching Flights:")
    found = False
    for flight in flights:
        if destination.lower() in flight["destination"].lower():
            print(f"Flight No: {flight['flight_no']} to {flight['destination']}")
            found = True
    if not found:
        print("No flights found for that destination.")

def book_flight():
    while True:
        display_flights()
        try:
            choice = int(input("Select flight number to book: ")) - 1
            if choice < 0 or choice >= len(flights):
                print("\nInvalid flight selection.\n")
                continue
        except ValueError:
            print("\nInvalid input.\n")
            continue

        flight = flights[choice]

        # Check if flight is fully booked
        if not flight["seats"]:
            print(f"\nSorry, the flight to {flight['destination']} is fully booked.\n")
            continue

        break  # Valid flight selected

    name = input("Enter passenger name: ")
    contact = input("Enter contact information: ")

    print(f"Available seats: {', '.join(flight['seats'])}")

    while True:
        seat = input("Select seat number: ")
        if seat not in flight["seats"]:
            print("\nSeat not available. Please choose again.")
        else:
            break

    flight["seats"].remove(seat)
    bookings.append({
        "name": name,
        "contact": contact,
        "flight_no": flight["flight_no"],
        "destination": flight["destination"],
        "seat": seat
    })

    print("\nBooking successful!")
    print(f"{name}, you booked flight {flight['flight_no']} to {flight['destination']} at seat {seat}")

    return post_action_prompt()

def view_booking():
    name = input("Enter passenger name: ")
    contact = input("Enter contact info: ")

    found = None
    for booking in bookings:
        if booking["name"] == name and booking["contact"] == contact:
            found = booking
            break

    if found:
        print("\nYour Booking:")
        print(f"Flight: {found['flight_no']} to {found['destination']}")
        print(f"Seat: {found['seat']}")
        option = input("Do you want to cancel this booking? (Y/N): ").upper()
        if option == "Y":
            for flight in flights:
                if flight["flight_no"] == found["flight_no"]:
                    flight["seats"].append(found["seat"])
                    break
            bookings.remove(found)
            print("\nBooking cancelled successfully.")
    else:
        print("\nNo booking found.")

    return post_action_prompt()

def post_action_prompt():
    print("\n1. Return to Main Menu")
    print("2. Exit")
    choice = input("Select an option: ")
    if choice == "1":
        return
    else:
        print("Exiting system. Goodbye!")
        exit()

def main_menu():
    while True:
        print("\n--- Flight Booking System ---")
        print("1. Search Flights")
        print("2. Book a Flight")
        print("3. View Booking")
        print("4. Exit")

        option = input("Select an option (1-4): ")

        if option == "1":
            search_flight()
        elif option == "2":
            book_flight()
        elif option == "3":
            view_booking()
        elif option == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def skyreserve_start():
    print("===================================")
    print("     Welcome to SkyReserve ✈️")
    print("===================================")
    print("1. Enter SkyReserve")
    print("2. Exit")
    
    while True:
        choice = input("Select an option (1-2): ")
        if choice == "1":
            main_menu()
            break
        elif choice == "2":
            print("\nThank you for visiting SkyReserve. Goodbye!")
            break
        else:
            print("\nInvalid input. Please enter 1 or 2.")

skyreserve_start()
