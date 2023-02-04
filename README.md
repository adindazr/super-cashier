# Python Project : Super Cashier

## 1. Introduction
As final assignment for Python Learning in Pacmann Academy, we are required to create features for a self-service checkout counter at a supermarket. Customers can enter their own purchases using this cashier system. The customers can enter the goods, quantities, and pricing of their purchases, and also able to edit their previous input. Discount and payment calculation are also included. 

## 2. Objectives
The following is a list of requirements to accomplish the project:
1. Customers are able enter their purchases, including the quantities and price.
2. Customers are able to edit their previous input.
3. Customers have option either to delete their purchases one by one or all at once.
4. Discount calculation for each transaction.
5. Final payment calculation for each transaction. 

The following flowchart captures the work flow of the project based on the preceding requirements.
![Super Cashier Flow Chart](https://user-images.githubusercontent.com/121531633/216751979-db42a73b-9d41-40fd-99cb-9f449dfd64e4.jpg)

## 3. Function Explanation
```def add_item(self)``` : To allow user input the item's name, quantity, and price. User's input will be added to shopping cart. Function will go on loop which allow user to input item one by one. Looping will stop if user choose to exit/finish shopping. Output will be success message for input.

```def check_order(self)``` : To allow user check their order by printing the shopping cart. User will be given option to edit their item (name, quantity, & price), remove/clear item or finish shopping. Function will go on loop until user choose to finish shopping. Output will be printed shopping cart.

```def show_items()``` : To print shopping cart.

```def payment (self)```: To calculate payment and discount.


## 4. Test Case
### Test 1: add shopping item
<img width="417" alt="Super Cashier - Test Case 1" src="https://user-images.githubusercontent.com/121531633/216752988-0f849e97-8c0f-4e98-9bc8-fbadaeac931e.png">

### Test 2: remove one shopping item
<img width="420" alt="Super Cashier - Test Case 2" src="https://user-images.githubusercontent.com/121531633/216753022-ebf151c5-61a3-4e29-b2d1-5e00fe87574b.png">

### Test 3: clear shopping cart
<img width="613" alt="Super Cashier - Test Case 3" src="https://user-images.githubusercontent.com/121531633/216753030-c6476d1f-a0ae-4d80-ba9e-6e99e9ca1969.png">

### Test 4: discount and payment calculation
<img width="425" alt="Super Cashier - Test Case 4" src="https://user-images.githubusercontent.com/121531633/216753039-0ea0932c-05c4-40ef-aad9-36cd3432a6ae.png">


## 5. Conclusion
- Super Cashier is simple programming for a self-service checkout counter.
- Features including input good's data (item's name, quantity, & price), edit, remove and clear shopping cart. Discount and payment calculation are also included.
