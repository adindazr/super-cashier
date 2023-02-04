from tabulate import tabulate

class Transaction:
  '''
  A self service check-out program which allows customers
  to enter their own purchases, including quantity and price.
  Customers able to edit their input and print their shopping cart.
  Calculating payment and discount is also included.
  '''

  def __init__(self):
    '''
    To initiate list

    name     : containing item's name [list]
    quantity : containing item's quantity [list]
    price    : containing item's price [list]
    total    : containing item's total price (quantity * price) [list]
    '''
    self.name = list ()
    self.quantity = list()
    self.price = list()
    self.total = list()

  def add_item(self):
    '''
    To allow user input the item's name, quantity, and price.
    User's input will be added to list mentioned above.
    Function will go on loop which allow user to input item one by one.
    Looping will stop if user choose to exit/finish shopping.

    Output:
    Success message for input.
    '''
    while True:
      try:
        # user will get two option: (1) to add item or (2) to finish shopping
        choice = int(input("Welcome to Adinda's Store!\nWhat do you want to buy today?\n(1)Add item\n(2)Finish\n(3)Exit app\nEnter your choice (input only number):"))
        if choice not in [1,2,3]:
          # message will be raised if user input out of given option
          raise ValueError("\nERROR: Choose only digits from the given option")
      except ValueError as error:
        print(f"\n{error}")
        continue

      else:
        if choice == 1 : # if user choose to add item, including quantity & price; total will be auto-calculated
          input_name = input("Enter product name: ")
          while True:
            try:
              input_qty = int(input("Enter quantity: "))
              input_price = int(input("Enter price of the product: "))
              break
            except ValueError:
              print("\nERROR: Quantity and price should be a number")
          total_count = input_qty * input_price
          self.name.append(input_name) # to add item into name list
          self.quantity.append(input_qty) # to add item into quantity list
          self.price.append(input_price) # to add item into price list
          self.total.append(total_count) # to add item into total list
          print('\nItem added to the shooping chart!')

        elif choice == 2: # if user choose to finish shopping, looping will stop
          #break
          print("\nYeay! You're good to go!\nPlease go to check_order to print your shopping cart!")
          self.check_order()
        elif choice == 3:
          print("Exittt")
          break 

  def check_order(self):
    '''
    To allow user check their order by printing the shopping cart.
    User will be given option to edit their item (name, quantity, & price), remove/clear item or finish shopping.
    Function will go on loop until user choose to finish shopping.

    Output:
    Printed shopping cart.
    '''

    def show_items():
      headers = ['No', 'Item name', 'Item quantity', 'Item price', 'Total'] # list containing headers title
      no_item = range(1, len(self.name)+1) # variable to create item's number as many as user's input
      
      table = zip(no_item, self.name, self.quantity, self.price, self.total) 
      print("Here your shopping cart!")
      print(tabulate(table, headers=headers))
      print("")

    while True:
      try:
        # to print the shopping cart in table format
        show_items()

        # user will be asked to input digit out of thing they want to do
        choice = int(input("Are there anything else you want to do?\n(1)Add item\n(2)Edit item name\n(3)Edit item quantity\n(4)Edit item price\n(5)Remove item\n(6)Clear shopping cart\n(7)Finish shopping\nEnter your choice (input only number):"))
      
      except ValueError:
        # message will be raised if user input out of given option
        print("\nERROR: Choose only digits from the given option")
        continue
      
      if choice not in [1, 2, 3, 4, 5, 6, 7]:
        print("\nERROR: Choose a number from the given option")
        continue

      if choice == 1: # if user chooses to add item, including quantity & price; total will be auto-calculated
        input_name = input("Enter product name: ")
        while True:
          try:
            input_qty = int(input("Enter quantity: "))
            input_price = int(input("Enter price of the product: "))
            break
          except ValueError:
            print("\nERROR: Quantity and price should be a number")
        total_count = input_qty * input_price
        self.name.append(input_name) # to add item into name list
        self.quantity.append(input_qty) # to add item into quantity list
        self.price.append(input_price) # to add item into price list
        self.total.append(total_count) # to add item into total list
        print('\nItem added to the shooping chart!')
      
      elif choice == 2: # if user chooses to edit item's name
        show_items()
        input_product_numb = int(input("Enter product number: "))
        try:
          self.name[input_product_numb-1]
        except (IndexError, ValueError):
          print("\nERROR: Product number not found")
          continue
        input_new_name = input("Enter new product name: ")
        
        self.name[input_product_numb-1] = input_new_name # update list using indexing

      elif choice == 3: # if user chooses to edit item's quantity
        show_items()
        input_product_numb = int(input("Enter product number: "))
        try:
          self.name[input_product_numb-1]
        except (IndexError, ValueError):
          print("\nERROR: Product number not found")
          continue
        input_new_quantity = int(input("Enter new product quantity: "))
        
        self.quantity[input_product_numb-1] = input_new_quantity # update list using indexing
        self.total[input_product_numb-1] = input_new_quantity * self.price[input_product_numb-1] # to update total list
      
      elif choice == 4: # if user chooses to edit item's price
        show_items()
        input_product_numb = int(input("Enter product number: "))
        try:
          self.name[input_product_numb-1]
        except (IndexError, ValueError):
          print("\nERROR: Product number not found")
          continue
        input_new_price = int(input("Enter new product price: "))
        
        self.price[input_product_numb-1] = input_new_price # update list using indexing
        self.total[input_product_numb-1] = input_new_price * self.quantity[input_product_numb-1] # to update total list

      elif choice == 5: # if user chooses to remove an item
        show_items()
        input_product_numb = int(input("Enter product number: "))
        try:
          self.name[input_product_numb-1]
        except (IndexError, ValueError):
          print("\nERROR: Product number not found")
          continue

        self.name.pop(input_product_numb-1) # remove name list using indexing
        self.quantity.pop(input_product_numb-1) # remove quantity list using indexing
        self.price.pop(input_product_numb-1) # remove price list using indexing
        self.total.pop(input_product_numb-1) # remove total list using indexing
      
      elif choice == 6: # if user chooses to clear all item(s)
        self.name.clear()
        self.quantity.clear()
        self.price.clear()
        self.total.clear()
        print("\nYour cart is empty now. Do you want to pick some items over again or finish shopping?")

      elif choice == 7: # if user chooses to finish shopping
        if len(self.name) == 0: # for user who clears their shopping cart aka cancels shopping 
          print("\nThank you for your time. Let's shopping another time!")
          break
        else: # for user who is ready to pay
          print("\nYour cart is ready! Let's move to payments!")
          self.payment()
          break

  def payment (self):
    '''
    To calculate payment and discount.

    total_bill = total payment before discount
    total_payment = total payment after discount

    Output:
    Printed final shopping cart.
    Calculated total bill, discount (if any), and final payment.
    '''
    total_bill = sum(self.total) # to calculated total payment before discount
    headers = ['No', 'Item name', 'Item quantity', 'Item price', 'Total']
    no_item = range(1, len(self.name)+1)
    table = zip(no_item, self.name, self.quantity, self.price, self.total)
    print("Your Shopping Summary")
    print(tabulate(table, headers=headers)) # to print final shopping cart

    if total_bill > 500_000: # to calculated 10% discount for bill above Rp500.000
      total_payment = total_bill * 0.9
      print(f"\nThank you for your shopping.\nYour shopping total payment is Rp{total_bill}.\nCongrats! You got 10% percent discount.\nYour final payment is Rp{total_payment}. ")
    
    elif total_bill > 300_000: # to calculated 8% discount for bill above Rp300.000
      total_payment = total_bill * 0.92
      print(f"\nThank you for your shopping.\nYour shopping total payment is Rp{total_bill}.\nCongrats! You got 8% percent discount.\nYour final payment is Rp{total_payment}. ")
    
    elif total_bill > 200_000: # to calculated 5% discount for bill above Rp200.000
      total_payment = total_bill * 0.95
      print(f"\nThank you for your shopping.\nYour shopping total payment is Rp{total_bill}.\nCongrats! You got 5% discount.\nYour final payment is Rp{total_payment}. ")
    
    else: # no discount
      total_payment = total_bill * 1
      print(f"\nThank you for your shopping. Your final payment is Rp{total_payment}.")
    
