import csv
from tkinter.messagebox import askyesno, showinfo, showerror

class ReservationNode:
    def __init__(self, table_no, chairs, reservation, date, time, people, sp_request='',
                 customer_name='', phone_number=''):
        self.table_no = table_no
        self.chairs = chairs
        self.reservation = reservation
        self.date = date
        self.time = time
        self.people = people
        self.request = sp_request
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.next = None

    def display(self):
            print(f"Table No: {self.table_no}")
            print(f"Chairs: {self.chairs}")
            print(f"Reservation: {self.reservation}")
            print(f"Date: {self.date}")
            print(f"Time: {self.time}")
            print(f"People: {self.people}")
            print(f"Special Request: {self.request}")
            print(f"Customer Name: {self.customer_name}")
            print(f"Phone Number: {self.phone_number}")
            print("----------------------")




class ReservationLinkedList:
    def __init__(self):
        self.head = None

    def append(self, reservation_node):
        if self.head is None:
            self.head = reservation_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = reservation_node

    def EVfind(self,date, name, phone_number):
        # Read reservations from the CSV file if the linked list is empty
        if self.head is None:
            try:
                self.read_reservations_from_csv('reservations.csv')
            except FileNotFoundError:
                self.write_reservations_to_csv('reservations.csv')

        current = self.head
        while current:
            if ( str(current.date) == str(date) and str(current.customer_name) == str(name)
                and str(current.phone_number) == str(phone_number)
            ):
                yield current
            current = current.next
        

    
    def find(self, table_no, date, time):
        # Read reservations from the CSV file if the linked list is empty
        if self.head is None:
            try:
                self.read_reservations_from_csv('reservations.csv')
            except FileNotFoundError:
                self.write_reservations_to_csv('reservations.csv')


        current = self.head
        while current:
            if (
                current.table_no == table_no
                and current.date == date
                and current.time == time
            ):
                return current
            current = current.next
        return None


    def delete_reservations(self, date, name, phone_number):
        current = self.head
        previous = None
        found = False
        while current:
            if current.date == date and current.customer_name == name and current.phone_number == phone_number:
                # Delete the reservation node
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                found = True
                break
            else:
                previous = current
                current = current.next

        if found:
            self.write_reservations_to_csv('reservations.csv')
        else:
            showerror("Reservation Not Found", "Error: Reservation not found.")



    def display(self):
        current = self.head
        while current is not None and current.reservation:
            print(f"Table No: {current.table_no}")
            print(f"Chairs: {current.chairs}")
            print(f"Reservation: {current.reservation}")
            print(f"Date: {current.date}")
            print(f"Time: {current.time}")
            print(f"People: {current.people}")
            print(f"Special Request: {current.request}")
            print(f"Customer Name: {current.customer_name}")
            print(f"Phone Number: {current.phone_number}")
            print("----------------------")
            current = current.next

    def write_reservations_to_csv(self, filename):
        reservations_data = []
        current = self.head
        while current:
            reservation_data = [
                current.table_no,
                current.chairs,
                str(current.reservation),
                current.date,
                current.time,
                current.people,
                current.request,
                current.customer_name,
                current.phone_number
            ]
            reservations_data.append(reservation_data)
            current = current.next

        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Table No', 'Chairs', 'Reservation', 'Date', 'Time', 'People',
                                 'Special Request', 'Customer Name', 'Phone Number'])
                writer.writerows(reservations_data)
        except IOError:
            showerror("Error", "Failed to write reservations to CSV file.")

    def read_reservations_from_csv(self, filename):
        self.head = None

        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    table_no, chairs, reservation, date, time, people, request, customer_name, phone_number = row
                    reservation_data = ReservationNode(int(table_no), int(chairs), reservation.lower() == 'true', date,
                                                       time, int(people), request, customer_name, phone_number)
                    self.append(reservation_data)
        except IOError:
            showerror("Error", "Failed to read reservations from CSV file.")

    def __iter__(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            yield current_item
            current_item = current_item.next

    


class BookTable:
    def __init__(self, table_no, chairs, date, time, people, sp_request = '', customer_name = '', phone_number = ''):
        self.table_no = int(table_no)
        self.chairs = chairs
        self.date = date
        self.time = time
        self.people = people
        self.request = sp_request
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.reservation = False


    def select_table(self, reservations_list):
        reservation_node = reservations_list.find(self.table_no, self.date, self.time)

        if reservation_node and reservation_node.reservation:
            # Reservation with the same details already exists
            showerror("Error", "Another reservation already exists with the same table number, date, and time.")
        else:
            self.reservation = True
            if reservation_node:
                # Reactivating a previously canceled reservation
                reservation_node.reservation = True
                reservation_node.customer_name = self.customer_name
                reservation_node.phone_number = self.phone_number
                showinfo("Reservation", "Reservation reactivated successfully.")

            else:
                reservation_data = ReservationNode(self.table_no, self.chairs, True, self.date,
                                                self.time, self.people, self.request,
                                                self.customer_name, self.phone_number)
                reservations_list.append(reservation_data)
                showinfo("Reservation", "Reservation made successfully.")

                reservations_list.write_reservations_to_csv('reservations.csv')

    



    def cancel_selection(self, reservations_list, username, phone_number):
        reservation_node = reservations_list.find(self.table_no, self.date, self.time)
        if reservation_node:
            if reservation_node.reservation:
                if reservation_node.table_no == self.table_no and reservation_node.date == self.date and reservation_node.time == self.time and reservation_node.customer_name == username and self.phone_number == phone_number:
                    self.reservation = False
                    reservation_node.reservation = False
                    reservation_node.customer_name = ''
                    reservation_node.phone_number = ''
                    showinfo("Cancel Reservation", "Reservation canceled successfully.")

                    reservations_list.write_reservations_to_csv('reservations.csv')
                else:
                    showerror("Unauthorized Access", "Error: Unauthorized access. Please provide correct username and phone number.")
            else:
                showerror("Reservation Not Found", "Error: Reservation not found.")
        else:
            showerror("Reservation Not Found", "Error: Reservation not found.")



    def display_reservations(self, reservations_list):
        reservations_list.display()







    




    
