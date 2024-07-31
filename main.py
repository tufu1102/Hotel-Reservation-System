from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime, tkinter.font
from tkinter.messagebox import askyesno, showinfo, showerror
from PIL import Image, ImageTk
from hash_class import HashTable
from Table import ReservationLinkedList, BookTable
import csv

root = Tk()
root.title('MEAT & EAT')
window_width = root.winfo_screenwidth() - 300
window_height = root.winfo_screenheight() - 100
root.geometry(f"{window_width}x{window_height}")

reservations_list = ReservationLinkedList()
table_objects = []

def delete_entries(frame):
    if frame==f2:
        F2_e1.delete(0, END)
        F2_e2.delete(0, END)
        F2_e3.delete(0, END)
        F2_e4.delete(0, END)
        TableVar1.set('')
        TableVar2.set('')
        TableVar3.set('')
        TableVar4.set('')
        TableVar5.set('')
        TableVar6.set('')
        TableVar7.set('')
        TableVar8.set('')
        TableVar9.set('')
        TableVar10.set('')
        TableVar11.set('')
        TableVar12.set('')
        TableVar13.set('')
        cal.selection_set(cur_date)
        hour_var.set(hours[0])
        minute_var.set(minutes[0])
        F2_b2.configure(command=lambda:confirm(False))
    if frame==f3:
        F3_e1.delete(0,END)
        F3_e2.delete(0,END)
    if frame==f4:
        F4_e1.delete(0, END)
        F4_e2.delete(0,END)
        F4_e3.delete(0,END)
    

def change_frame(cur, arg):
    if cur == f1 and arg == f4:
        delete_entries(f4)
        clear_labels_in_frame(f4)
    if cur == f4 and arg == f2:
        #Configure the command of confirm button to confirm(True)
        F2_b2['command'] = lambda: confirm(True)
    else:
        F2_b2['command'] == confirm
    arg.pack(side="top", fill="both", expand=True)
    cur.pack_forget()
    
    

def confirm(edit=False):
    if edit == False:
        answer = askyesno(title='CONFIRMATION', message='Would you like to select the chosen table/s?')
        if answer:
            get_details()
            change_frame(f2, f1)
            message = showinfo(title="TABLE RESERVED!", message="The table/s you have chosen have been successfully reserved. Thank you!")
            delete_entries(f2)
    else:
        answer = askyesno(title='CONFIRMATION', message='Would you like to edit the chosen reservation/s?')
        if answer:
            get_details()
            change_frame(f2, f1)
            message = showinfo(title="TABLE RESERVED!", message="The table/s you have chosen have been successfully reserved. Thank you!")
            delete_entries(f2)


def get_details():
    selected_date = cal.selection_get()
    num_people = F2_e1.get()

    selected_tables=[]
    if TableVar1.get():
        selected_tables.append(TableVar1.get())
    if TableVar2.get():
        selected_tables.append(TableVar2.get())
    if TableVar3.get():
        selected_tables.append(TableVar3.get())
    if TableVar4.get():
        selected_tables.append(TableVar4.get())
    if TableVar5.get():
        selected_tables.append(TableVar5.get())
    if TableVar6.get():
        selected_tables.append(TableVar6.get())
    if TableVar7.get():
        selected_tables.append(TableVar7.get())
    if TableVar8.get():
        selected_tables.append(TableVar8.get())
    if TableVar9.get():
        selected_tables.append(TableVar9.get())
    if TableVar10.get():
        selected_tables.append(TableVar10.get())
    if TableVar11.get():
        selected_tables.append(TableVar11.get())
    if TableVar12.get():
        selected_tables.append(TableVar12.get())
    if TableVar13.get():
        selected_tables.append(TableVar13.get())

    #getting the time
    selected_hour = hour_var.get()
    selected_minute = minute_var.get()
    selected_time = f"{selected_hour}:{selected_minute}"

    #getting special request
    special_request = F2_e2.get()

    #getting name
    name = F2_e3.get()

    #getting phone number
    phone_number = F2_e4.get()

    #linked list addition
    for table_no in selected_tables:
        table = BookTable(
            table_no= int(table_no),
            chairs=int(num_people),
            date=selected_date.strftime("%Y-%m-%d"),
            time=selected_time,
            people=int(num_people),
            sp_request=special_request,
            customer_name=name,
            phone_number=phone_number
        )
        table.select_table(reservations_list)


def edit_reservation():
    flag = False
    # Retrieve the date, name, and phone number entered by the user
    date_str = F4_e1.get()
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    name = F4_e2.get()
    phone_number = F4_e3.get()

    # Iterate over the existing reservations for the provided details
    for reservation_node in reservations_list.EVfind(date.strftime("%Y-%m-%d"), name, phone_number):
        flag = True
        
        cal.selection_set(date)
    # Set the values from the existing reservation in Frame 2
        F2_e1.delete(0, END)
        F2_e1.insert(0, reservation_node.chairs)

        # Set the selected tables based on the existing reservation
        # ...
        selected_tables = str(reservation_node.table_no)

# Set the values of the TableVar variables based on the selected tables
        if '1' == selected_tables:
            TableVar1.set('1')
        if '2' == selected_tables:
            TableVar2.set('2')
        if '3' == selected_tables:
            TableVar3.set('3')
        if '4' == selected_tables:
            TableVar4.set('4')
        if '5' == selected_tables:
            TableVar5.set('5')
        if '6' == selected_tables:
            TableVar6.set('6')
        if '7' == selected_tables:
            TableVar7.set('7')
        if '8' == selected_tables:
            TableVar8.set('8')
        if '9' == selected_tables:
            TableVar9.set('9')
        if '10' == selected_tables:
            TableVar10.set('10')
        if '11' == selected_tables:
            TableVar11.set('11')
        if '12' == selected_tables:
            TableVar12.set('12')
        if '13' == selected_tables:
            TableVar13.set('13')



        # Split the time into hour and minute and set in Frame 2
        hour, minute = reservation_node.time.split(":")
        hour_var.set(hour)
        minute_var.set(minute)

        # Set the special request, name, and phone number
        F2_e2.delete(0, END)
        F2_e2.insert(0, reservation_node.request)
        F2_e3.delete(0, END)
        F2_e3.insert(0, reservation_node.customer_name)
        F2_e4.delete(0, END)
        F2_e4.insert(0, reservation_node.phone_number)
        # Switch to Frame 2

        reservations_list.delete_reservations(date_str, name, phone_number)
        delete_reservations_from_csv(date, name, phone_number)
        change_frame(f4, f2)
        
    
    if not flag:
    # If no reservation found, show an error message
        showerror("Reservation Not Found", "Error: Reservation not found.")

def delete_reservations_from_csv(date, name, phone_number):
    # Read the existing reservations from the CSV file
    date_str = date.strftime("%Y-%m-%d")
    reservations = []
    with open("reservations.csv", "r") as file:
        reader = csv.reader(file)
        reservations = list(reader)

    # Remove the reservations with matching date, name, and phone number
    updated_reservations = [reservation for reservation in reservations if
                            reservation[3] != date_str or reservation[7] != name or int(reservation[8]) != int(phone_number)]

    # Write the updated reservations back to the CSV file
    with open("reservations.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_reservations)

def clear_labels_in_frame(frame):
    exclude_labels = ["Date:", "Name:", "Phone no.:", "*enter in yyyy-mm-dd format"]
    for widget in frame.winfo_children():
        if isinstance(widget, Label) and widget.cget("text") not in exclude_labels:
            widget.destroy()


def view_reservation(date, name, ph):
    flag =False
    
    
    # Display the reservation details in a table format
    row = 0
    for reservation in reservations_list.EVfind(date, name, ph):
        flag = True
        headers = ['Date', 'Time', 'Name', 'Table', 'People', 'Special Request', 'Phone Number']
        for i, header in enumerate(headers):
            label = Label(f4, text=header, font=('Trebuchet MS', 14, 'bold'))
            label.place(relx=0.1 + (i * 0.1), rely=0.2)

        # Display Date
        F4_l6 = Label(f4, text=reservation.date, font=('Trebuchet MS', 14))
        F4_l6.place(relx=0.1, rely=0.25 + (row * 0.1))
        
        # Display Time
        F4_l8 = Label(f4, text=reservation.time, font=('Trebuchet MS', 14))
        F4_l8.place(relx=0.2, rely=0.25 + (row * 0.1))
        
        # Display Name
        F4_l10 = Label(f4, text=reservation.customer_name, font=('Trebuchet MS', 14))
        F4_l10.place(relx=0.3, rely=0.25 + (row * 0.1))
        
        # Display Table
        F4_l12 = Label(f4, text=reservation.table_no, font=('Trebuchet MS', 14))
        F4_l12.place(relx=0.4, rely=0.25 + (row * 0.1))
        
        # Display People
        F4_l14 = Label(f4, text=reservation.people, font=('Trebuchet MS', 14))
        F4_l14.place(relx=0.5, rely=0.25 + (row * 0.1))
        
        # Display Special Request
        F4_l16 = Label(f4, text=reservation.request, font=('Trebuchet MS', 14))
        F4_l16.place(relx=0.6, rely=0.25 + (row * 0.1))
        
        # Display Phone Number
        F4_l18 = Label(f4, text=reservation.phone_number, font=('Trebuchet MS', 14))
        F4_l18.place(relx=0.7, rely=0.25 + (row * 0.1))
        
        row += 1

    if not flag:
        showerror("View Reervation","Reservation not found")
    
    

def check_valid(date, name, ph, choice= 'edit'):


    valid_d = valid_n = valid_p = True
    if date:
        try:
            datetime.date.fromisoformat(date)
        except ValueError:
            m = showerror(title='date incorrect', message='date must be in the yyyy-mm-dd format')
            valid_d = False
    else:
        m = showerror(title='date required', message='date column cannot be empty')
        valid_d = False
    if not name:
        m = showerror(title='name required', message='name column cannot be empty')
        valid_n = False
    if ph:
        if not (len(ph)==10 and ph.isdigit()):
            m = showerror(title='phone number invalid', message='enter a valid phone number')
            valid_p = False
    else:
        m = showerror(title='phone number required', message='phone no. column cannot be empty')
        valid_p = False

    if valid_p and valid_d and valid_n:
        if choice=='edit':
            edit_reservation()

        else:
            view_reservation(date, name, ph)


def treeview():
    # Create a new window for the treeview
    treeview_window = Toplevel(root)
    treeview_window.title('View Reservations')

    # Create the Treeview widget
    tree = ttk.Treeview(treeview_window)
    tree.pack(fill='both', expand=True)

    # Configure the columns
    tree["columns"] = ("Date", "Time", "Name", "Table", "People", "Special Request", "Phone Number")
    tree.column("#0", width=0, stretch="no")  # Hide the default first column
    tree.column("Date", width=100)
    tree.column("Time", width=100)
    tree.column("Name", width=150)
    tree.column("Table", width=100)
    tree.column("People", width=80)
    tree.column("Special Request", width=200)
    tree.column("Phone Number", width=120)

    #fetch reservations from a data source
    reservations = fetch_reservations()

    # Add column headings
    tree.heading("Date", text="Date")
    tree.heading("Time", text="Time")
    tree.heading("Name", text="Name")
    tree.heading("Table", text="Table")
    tree.heading("People", text="People")
    tree.heading("Special Request", text="Special Request")
    tree.heading("Phone Number", text="Phone Number")

    # Fetch reservations from a data source (e.g., a database)
    reservations = fetch_reservations()

    # Insert reservations into the treeview
    for reservation in reservations:
        tree.insert("", "end", values=reservation)

    # Add scrollbar
    scrollbar = ttk.Scrollbar(treeview_window, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    # Adjust column widths based on content
    for column in tree["columns"]:
        tree.heading(column, text=column, anchor='w')
        tree.column(column, width= tkinter.font.Font().measure(column))

    # Bind the "Destroy" event of the treeview window to update the main frame when closed
    treeview_window.protocol("WM_DELETE_WINDOW", lambda: change_frame(f4, f1))

def fetch_reservations():
    # Implement your code to fetch reservations from a data source (e.g., a database)
    # Return a list of reservation data in the format: (date, time, name, table, people, special_request, phone_number)
    reservations = [
        ("2023-07-07", "18:30", "John Doe", "Table 1", 4, "No special request", "1234567890"),
        ("2023-07-08", "19:00", "Jane Smith", "Table 3", 2, "Vegetarian meal", "9876543210")
    ]
    return reservations

def check_staff(name, pwd):
    """ checks whether staff name and passwd matches with that in the staff_dict"""
    staff_dict = staff_list()
    if pwd==staff_dict[name]:
        change_frame(f3,f5)
        F3_e1.delete(0, END)
        F3_e2.delete(0, END)
    else:
        message = showerror(title='error', message="name or password is incorrect")

def staff_list():
    staff_dict = HashTable()
    with open("staff.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        read_list = list(reader)
        for i in read_list[1:]:
            staff_dict[i[0]] = i[1]
    return staff_dict

f5 = Frame(root)  # treeview page for staff viewers
f4 = Frame(root)  # login page for customers to view reservation
f3 = Frame(root)  # staff login page
f2 = Frame(root)  # select table page
f1 = Frame(root, bg='blue')  # home page

f1.pack(side="top", fill="both", expand=True)

# Frame 1
label = Label(f1, text="MEAT & EAT", font=('Trebuchet MS', 30))
label.place(relx=0.5, rely=0.05, anchor='n')
F1_b1 = Button(f1, text='BOOK RESERVATION', width=25, height=5, command=lambda: change_frame(f1, f2))
F1_b1.place(relx=0.5, rely=0.35, anchor='n')
F1_b2 = Button(f1, text='STAFF LOGIN', width=25, height=5, command=lambda: change_frame(f1, f3))
F1_b2.place(relx=0.5, rely=0.5, anchor='n')
F1_b3 = Button(f1, text='VIEW RESERVATION', width=25, height=5, command=lambda: change_frame(f1, f4))
F1_b3.place(relx=0.5, rely=0.65, anchor='n')

# Frame 2
# Buttons
F2_b1 = Button(f2, text='BACK', command=lambda: change_frame(f2, f1))
F2_b1.place(relx=0.95,x=-40, rely=0.95, anchor='sw')
F2_b2 = Button(f2, text='CONFIRM RESERVATION', command=lambda:confirm(False))
F2_b2.place(relx=0.95, rely=0.9, y=-8, anchor='se')

# Calendar
F2_l1 = Label(f2, text='Date:', font=('Trebuchet MS', 14))
F2_l1.place(relx=0.1, x=-90, rely=0.1, y=-15, anchor='w')

cur_date = datetime.date.today()
cal = Calendar(f2, selectmode='day', year=cur_date.year, month=cur_date.month, day=cur_date.day)
cal.place(relx=0.1, x=-90, rely=0.25, y=-10, relwidth=0.25, relheight=0.25, anchor='w')

# Entry box for number of people
F2_l2 = Label(f2, text='Number of People:', font=('Trebuchet MS', 14))
F2_l2.place(relx=0.1, x=-90, rely=0.4, anchor='w')
F2_e1 = Entry(f2, width=14, font=('calibre', 16))
F2_e1.place(relx=0.1, x=-90, rely=0.45, anchor='w')

# Tables
F2_l3 = Label(f2, text='Tables:', font=('Trebuchet MS', 14))
F2_l3.place(relx=0.1, x=-90, rely=0.55, anchor='w')

TableVar1 = StringVar()
TableVar2 = StringVar()
TableVar3 = StringVar()
TableVar4 = StringVar()
TableVar5 = StringVar()
TableVar6 = StringVar()
TableVar7 = StringVar()
TableVar8 = StringVar()
TableVar9 = StringVar()
TableVar10 = StringVar()
TableVar11 = StringVar()
TableVar12 = StringVar()
TableVar13 = StringVar()
T1 = Checkbutton(f2, text = "Table 1", font=('Trebuchet MS', 11), variable = TableVar1, \
                 onvalue = '1', offvalue = '', height=5, \
                 width = 20)
T1.place(relx=0.1, x=-90, rely=0.7, y=-60, height=20, width=100, anchor='w')
T2 = Checkbutton(f2, text = "Table 2", font=('Trebuchet MS', 11), variable = TableVar2, \
                 onvalue = '2', offvalue = '', height=5, \
                 width = 20)
T2.place(relx=0.1, x=-90, rely=0.7, y=-40, height=20, width=100, anchor='w')
T3 = Checkbutton(f2, text = "Table 3", font=('Trebuchet MS', 11), variable = TableVar3, \
                 onvalue = '3', offvalue = '', height=5, \
                 width = 20)
T3.place(relx=0.1, x=-90, rely=0.7, y=-20, height=20, width=100, anchor='w')
T4 = Checkbutton(f2, text = "Table 4", font=('Trebuchet MS', 11), variable = TableVar4, \
                 onvalue = '4', offvalue = '', height=5, \
                 width = 20)
T4.place(relx=0.1, x=-90, rely=0.7, y=0, height=20, width=100, anchor='w')
T5 = Checkbutton(f2, text = "Table 5", font=('Trebuchet MS', 11), variable = TableVar5, \
                 onvalue = '5', offvalue = '', height=5, \
                 width = 20)
T5.place(relx=0.1, x=-90, rely=0.7, y=20, height=20, width=100, anchor='w')
T6 = Checkbutton(f2, text = "Table 6", font=('Trebuchet MS', 11), variable = TableVar6, \
                 onvalue = '6', offvalue = '', height=5, \
                 width = 20)
T6.place(relx=0.1, x=-90, rely=0.7, y=40, height=20, width=100, anchor='w')
T7 = Checkbutton(f2, text = "Table 7", font=('Trebuchet MS', 11), variable = TableVar7, \
                 onvalue = '7', offvalue = '', height=5, \
                 width = 20)
T7.place(relx=0.2, x=-60, rely=0.7, y=-60, height=20, width=100, anchor='w')
T8 = Checkbutton(f2, text = "Table 8", font=('Trebuchet MS', 11), variable = TableVar8, \
                 onvalue = '8', offvalue = '', height=5, \
                 width = 20)
T8.place(relx=0.2, x=-60, rely=0.7, y=-40, height=20, width=100, anchor='w')
T9 = Checkbutton(f2, text = "Table 9", font=('Trebuchet MS', 11), variable = TableVar9, \
                 onvalue = '9', offvalue = '', height=5, \
                 width = 20)
T9.place(relx=0.2, x=-60, rely=0.7, y=-20, height=20, width=100, anchor='w')
T10 = Checkbutton(f2, text = "Table 10", font=('Trebuchet MS', 11), variable = TableVar10, \
                 onvalue = '10', offvalue = '', height=5, \
                 width = 20)
T10.place(relx=0.2, x=-60, rely=0.7, y=0, height=20, width=100, anchor='w')
T11 = Checkbutton(f2, text = "Table 11", font=('Trebuchet MS', 11), variable = TableVar11, \
                 onvalue = '11', offvalue = '', height=5, \
                 width = 20)
T11.place(relx=0.2, x=-60, rely=0.7, y=20, height=20, width=100, anchor='w')
T12 = Checkbutton(f2, text = "Table 12", font=('Trebuchet MS', 11), variable = TableVar12, \
                 onvalue = '12', offvalue = '', height=5, \
                 width = 20)
T12.place(relx=0.2, x=-60, rely=0.7, y=40, height=20, width=100, anchor='w')
T13 = Checkbutton(f2, text = "Table 13", font=('Trebuchet MS', 11), variable = TableVar13, \
                 onvalue = '13', offvalue = '', height=5, \
                 width = 20)
T13.place(relx=0.2, x=-60, rely=0.7, y=60, height=20, width=100, anchor='w')


# Time picker
F2_l4 = Label(f2, text='Time:', font=('Trebuchet MS', 14))
F2_l4.place(relx=0.1, x=-90, rely=0.87, anchor='w')
F2_l9 = Label(f2, text=':', font=('Trebuchet MS', 14))
F2_l9.place(relx=0.22, x=25, rely=0.87, anchor='w')

# Creating a list of hours from 10 AM to 9 PM
hours = [str(i) for i in range(10, 22)]

# Creating a list of minutes with a 10-minute interval
minutes = [str(i).zfill(2) for i in range(0, 60, 10)]

# Creating hour and minute variables with default values
hour_var = StringVar(f2)
minute_var = StringVar(f2)
# Setting default values for hour and minute variables
hour_var.set(hours[0])
minute_var.set(minutes[0])

# Creating dropdown menus for hour and minute selection
hour_dropdown = OptionMenu(f2, hour_var, *hours)
hour_dropdown.place(relx=0.18, rely=0.87, anchor='w')  # Updated placement for hour dropdown

minute_dropdown = OptionMenu(f2, minute_var, *minutes)
minute_dropdown.place(relx=0.27, rely=0.87, anchor='w')  # Updated placement for minute dropdown


# Entry box for special request
F2_l5 = Label(f2, text='Special request:', font=('Trebuchet MS', 14))
F2_l5.place(relx=0.1, x=-90, rely=0.93, anchor='w')
F2_e2 = Entry(f2, width=15, font=('calibre', 14))
F2_e2.place(relx=0.1, x=70, rely=0.93, anchor='w')

#entry box for name
F2_l6 = Label(f2, text='Name:', font=('Trebuchet MS', 14))
F2_l6.place(relx=0.5, x=-40, rely=0.87, anchor='w')
F2_e3 = Entry(f2, width=18, font=('calibre', 14))
F2_e3.place(relx=0.5, x=30, rely=0.87, anchor='w')

#entry box for phone number
F2_l7 = Label(f2, text='Phone No.:', font=('Trebuchet MS', 14))
F2_l7.place(relx=0.5, x=-75, rely=0.93, anchor='w')
F2_e4 = Entry(f2, width=18, font=('calibre', 14))
F2_e4.place(relx=0.5, x=30, rely=0.93, anchor='w')


# Image
F2_l8 = Label(f2, text='Table Layout', font=('Trebuchet MS', 20))
F2_l8.place(relx=0.55, rely=0.6)

image_path = "table_image.jpeg"

# Resize the image
image = Image.open(image_path)
resized_image = image.resize((int(window_width/2), int(window_height/2)))
photo = ImageTk.PhotoImage(resized_image)

image_label = Label(f2, image=photo)
image_label.place(relx=0.65, rely=0.1, anchor='n')


#frame3
F3_l1 = Label(f3, text="Staff Login", font=('Trebuchet MS', 30))
F3_l1.place(relx=0.4, rely=0.3)

#entry box for staff name
F3_l2 = Label(f3, text='Name:', font=('Trebuchet MS', 14))
F3_l2.place(relx=0.4, x=-40, rely=0.5, anchor='w')
F3_e1 = Entry(f3, width=18, font=('calibre', 14))
F3_e1.place(relx=0.4, x=30, rely=0.5, anchor='w')

#entry box for password
F3_l3 = Label(f3, text='Password:', font=('Trebuchet MS', 14))
F3_l3.place(relx=0.4, x=-75, rely=0.6, anchor='w')
F3_e2 = Entry(f3, width=18, show='*', font=('calibre', 14))
F3_e2.place(relx=0.4, x=30, rely=0.6, anchor='w')

#buttons
F3_b1 = Button(f3, text='Login', font=('Calibri', 14), command=lambda:check_staff(F3_e1.get(), F3_e2.get()))
F3_b1.place(relx=0.4, x=60, rely=0.7)
F3_b2 = Button(f3, text='Back', font=('Calibri', 14), command=lambda: change_frame(f3, f1))
F3_b2.place(relx=0.92, rely=0.9)

#frame 4

#entry box for date, name and phone number
F4_l1 = Label(f4, text='Date:', font=('Trebuchet MS', 14))
F4_l1.place(relx=0.1, x=-60, rely=0.1, anchor='w')
F4_e1 = Entry(f4, width=18, font=('calibre', 14))
F4_e1.place(relx=0.1, rely=0.1, anchor='w')
F4_l4 = Label(f4, text='*enter in yyyy-mm-dd format', font=('Trebuchet MS', 10))
F4_l4.place(relx=0.1, x=-60, rely=0.1, y=30, anchor='w')

F4_l2 = Label(f4, text='Name:', font=('Trebuchet MS', 14))
F4_l2.place(relx=0.4, x=-60, rely=0.1, anchor='w')
F4_e2 = Entry(f4, width=18, font=('calibre', 14))
F4_e2.place(relx=0.4, rely=0.1, anchor='w')

F4_l3 = Label(f4, text='Phone no.:', font=('Trebuchet MS', 14))
F4_l3.place(relx=0.7, x=-50, rely=0.1, anchor='w')
F4_e3 = Entry(f4, width=18, font=('calibre', 14))
F4_e3.place(relx=0.75, rely=0.1, anchor='w')

#buttons
F4_b1 = Button(f4, text='Edit reservation', font=('Calibri', 14), command=lambda:check_valid(F4_e1.get(), F4_e2.get(), F4_e3.get()))
F4_b1.place(relx=0.15, rely=0.9)
F4_b1 = Button(f4, text='View reservation', font=('Calibri', 14), command=lambda:check_valid(F4_e1.get(), F4_e2.get(), F4_e3.get(), 'view'))
F4_b1.place(relx=0.3, rely=0.9)
F4_b3 = Button(f4, text='Back', font=('Calibri', 14), command=lambda: change_frame(f4, f1))
F4_b3.place(relx=0.92, rely=0.9)

root.mainloop()