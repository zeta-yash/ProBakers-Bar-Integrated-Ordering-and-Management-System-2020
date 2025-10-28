[![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev)
# ProBakers' Bar - Integrated Ordering and Management System

Welcome to **ProBakers' Bar**, a simple command-line restaurant management system. This system allows customers to book seats, place orders, and view the restaurant menu, while staff can manage seating availability and customer interactions.

---

## Features

### Customer Features:

* **Book a Seat**: Check availability and book seats in the restaurant.
* **Place Orders**: Choose food items from the menu and place orders.
* **View Menu**: Display a list of available food items and their prices.
* **Generate Bill**: View and calculate the bill for the food ordered.
* **Give Rating**: Provide feedback on the restaurant experience.

### Staff Features:

* **Seat Management**: Monitor and manage seat availability.
* **Menu Management**: Update the food menu and manage prices.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ProBakers-Bar.git
```

### 2. Navigate to the project directory

```bash
cd ProBakers-Bar
```

### 3. Run the application

```bash
python src/ordering_management.py
```

---

## Usage

Upon running the system, you'll be prompted to log in as either a **Customer** or **Staff**.

### Customer Workflow:

1. **Login**: Enter your name (new customers are registered automatically).
2. **Choose an Action**:

   * **Book Seat**: Reserve available seats.
   * **Give Order**: Select food items to order.
   * **View Menu**: See a list of available food items and prices.
   * **Generate Bill**: View your order summary and calculate the total.
   * **Give Rating**: Provide feedback on the restaurant experience.
3. **Exit**: Log out from the system.

### Staff Workflow:

* Manage seat availability and update the restaurant menu.
* The system will automatically prompt the staff to manage these features based on the customer interactions.

---

## Example Interaction:

**Login as Customer**:

```
Login as:
    1.Customer
    2.Staff
    0.Exit
Choose from the options given above: 1
Please enter your name: John
Welcome Back, John! How can I help you?

1.Book Seat
2.Give Order
3.MENU
4.Generate Bill
5.Give Rating
0.Exit

Enter the choice: 1
Available Seats: 12
Enter no. of Seats you want: 2
Your Booking Confirmed

Enter the choice: 2
Enter the food codes here (in '[]' brackets): [1, 2]
Your order has been placed!
Order Summary:
BlackForest
Pastries

Enter the choice: 4
Items              Price
================================
BlackForest        200
Pastries           50
================================
Total              250
```

---

## Menu Example:

```
Item                Price (in Rs.)
--------------------------------
1.BlackForest       200
2.Pastries          50
3.CocoFudge         40
4.Muffins           20
5.Toast             10
6.Sandwiches        30
7.Pizza             90
8.Biscuits          25
9.SoftDrink         20
10.Coffee           35
```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

### Sample ASCII Art:

```
                             )  (  )  (
                            (^)(^)(^)(^)
                            _i__i__i__i_
                           (____________)
                           |####|>o<|###| 
                           (____________)
                           ProBakers' Bar
Welcome to the Integrated Ordering and Management System of ProBakers' Bar.
```

---

## Notes

* This system is designed for a simple restaurant scenario.
* It assumes a fixed number of seats in the restaurant and basic stock for food items.
* Staff is not explicitly managed within the code but could be expanded to include features like password management, employee tracking, and more.
