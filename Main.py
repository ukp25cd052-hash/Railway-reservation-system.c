seats = 50
bookings = {}
booking_id = 1

def check_availability():
    print("Available seats:", seats)

def book_ticket():
    global seats, booking_id
    if seats <= 0:
        print("No seats available")
        return
    
    name = input("Enter name: ")
    age = input("Enter age: ")

    bookings[booking_id] = {"name": name, "age": age}
    print("Booked successfully! Your ID:", booking_id)

    booking_id += 1
    seats -= 1

def view_ticket():
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        print("Details:", bookings[bid])
    else:
        print("Not found")

def cancel_ticket():
    global seats
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        del bookings[bid]
        seats += 1
        print("Cancelled successfully")
    else:
        print("Invalid ID")

while True:
    print("\n1.Check 2.Book 3.View 4.Cancel 5.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        check_availability()
    elif choice == '2':
        book_ticket()
    elif choice == '3':
        view_ticket()
    elif choice == '4':
        cancel_ticket()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
      
