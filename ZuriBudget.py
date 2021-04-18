class Budget:

    def __init__(self):
        self.category_list = []
        self.category_balance = {}

    # To start the application
    def app_main(self):
        if not (self.category_list and self.category_balance):
            print("Your Categories are empty. Please add Categories")
            self.create_categories()
        else:
            self.operation()

    # New Category
    def create_categories(self):
        number_of_categories = int(input("You can create Food, Clothing, Entertainment... \n How many categories do you want to create?: "))
        for num in range(1, number_of_categories + 1):
            supply_category = input(f"Supply Category Name {num}: ")
            self.category_list.append(supply_category)

        for category in self.category_list:
            self.category_balance[category] = 0
        print("**** **** **** **** **** **** **** **** **** ****")
        print("Categories have been successfully created")
        print(f"Category and Balance: {self.category_balance}\n")
        self.operation()

    # Budget operations function
    def operation(self):
        print(""" *** You can perform the following ***:\n
 [1] - DEPOSIT
 [2] - WITHDRAW
 [3] - BALANCE
 [4] - TRANSFER BETWEEN CATEGORIES
 [5] - CREATE NEW CATEGORY
 [6] - TOTAL BALANCE
 [7] - EXIT
        """)
        try:
            action = int(input("Which operation do you want to perform? Type 1,2,3,4,5,6 or 7: "))
            if action == 1:
                self.deposit_funds()

            elif action == 2:
                self.withdraw_funds()

            elif action == 3:
                self.get_balance()

            elif action == 4:
                self.transfer_funds()

            elif action == 5:
                self.add_new_category()

            elif action == 6:
                self.get_total_balance()

            elif action == 7:
                quit()

            else:
                print("You have supplied an invalid input. Please try again \n")
                self.operation()
        except ValueError:
            print("Number is expected")
            self.operation()

    def deposit_funds(self):
        print("Below are the categories available for deposit:")
        for category in self.category_list:
            print(self.category_list.index(category) + 1, category)
        try:
            select_category = int(input("Select a category to deposit funds to: "))
            selected_category = select_category - 1  
            category = self.category_list[selected_category]  
            print(f"You have chosen to deposit funds to  {category}".capitalize())
            deposit_amount = int(input(f"How much do you want to deposit to {category}: "))
            self.category_balance[category] += deposit_amount
            print(f"You have deposited {deposit_amount} to {category}")
            print(f"Your New Balance:  {self.category_balance}")
            try:
                reply = int(input('Would you like to carry out another operation? Enter 1 for "Yes" and 2 for "No" \n'))
                if reply == 1:
                    self.operation()
                elif reply == 2:
                    print("Thank you for using this app")
                    exit()
                else:
                    print("Invalid input")
                    self.operation()
            except ValueError:
                print("Please try again")
                self.operation()
        except:
            print("Number Expected")
            self.operation()

    def withdraw_funds(self):
        print("These are the available categories?")
        for category in self.category_list:
            print(self.category_list.index(category) + 1, category)
        try:
            select_category = int(input("Select a category to withdraw funds from: "))
            selected_category = select_category - 1  
            category = self.category_list[selected_category]
            print(f"You have chosen to withdraw funds from  {category}")
            withdrawal_amount = int(input(f"How much do you want to withdraw from {category}: "))
            if withdrawal_amount >= self.category_balance[category] or self.category_balance[category] <= 0:
                print(f"Insufficient funds. Your current balance is {self.category_balance[category]}")
                try:
                    response = int(input('Would you like to make a deposit? Enter 1 for "Yes" and 2 for "No" \n'))
                    if response == 1:
                        self.deposit_funds()
                    elif response == 2:
                        try:
                            reply = int(input('Would you like to perform another operation? Enter 1 for "Yes" and 2 for "No" \n'))
                            if reply == 1:
                                self.operation()
                            elif reply == 2:
                                print("Thank you")
                                exit()
                            else:
                                print("Invalid value supplied")
                                self.operation()
                        except ValueError:
                            print("Number is Expected")
                            self.operation()

                    else:
                        print("Invalid parameter supplied")
                        self.operation()
                except ValueError:
                    print("Number is Expected")
                    self.operation()
            else:
                self.category_balance[category] -= withdrawal_amount
                print(f"{withdrawal_amount} successfully withdrawn from {category}")
                print(f"Updated Balance:  {self.category_balance}")
                try:
                    reply = int(input('Would you like to perform another operation? Select (1) for "Yes" and (2) for "No" \n'))
                    if reply == 1:
                        self.operation()
                    elif reply == 2:
                        print("Thank you")
                        exit()
                    else:
                        print("Invalid value supplied")
                        self.operation()
                except ValueError:
                    print("Number is Expected")
                    self.operation()
        except ValueError:
            print("Number is expected")
            self.operation()

    # Transfering funds function
    def transfer_funds(self):
        try:
            # Transfering funds
            print("The below are the categories available?")
            for category in self.category_list:
                print(self.category_list.index(category) + 1, category.upper())
            selected_category1 = int(input("Select a category to transfer funds from: "))
            sending_category = selected_category1 - 1
            category1 = self.category_list[sending_category]

            # Receiving funds
            selected_category2 = int(input("Select category to transfer funds to:"))
            for category in self.category_list:
                print(self.category_list.index(category) + 1, category)
            receiving_category = selected_category2 - 1
            category2 = self.category_list[receiving_category]

            print(f"You have chosen to transfer funds from  {category1} to {category2}")
            withdrawal_amount = int(input(f"How much do you want to transfer from {category1} to {category2}: "))
            if withdrawal_amount >= self.category_balance[category1] or self.category_balance[category1] <= 0:
                print(f"Insufficient funds. Your current balance is {self.category_balance[category1]}")
                try:
                    response = int(input('Would you like to make a deposit? Type 1 for "Yes" and 2 for "No" \n'))
                    if response == 1:
                        self.deposit_funds()
                    elif response == 2:
                        try:
                            reply = int(input('Would you like to perform another operation? Type 1 for "Yes" and 2 for "No" \n'))
                            if reply == 1:
                                self.operation()
                            elif reply == 2:
                                print("Thanks for using this app")
                                exit()
                            else:
                                print("Invalid value supplied")
                                self.operation()
                        except ValueError:
                            print("Number is Expected")
                            self.operation()
                    else:
                        print("Invalid parameter supplied")
                        self.deposit_funds()
                except ValueError:
                    print("Number is Expected")
                    self.deposit_funds()
            else:
                self.category_balance[category1] -= withdrawal_amount
                self.category_balance[category2] += withdrawal_amount
                print(f"{withdrawal_amount} Successfully transfered from {category1} to {category2}")
                print(f"Updated List and Balance:  {self.category_balance}")
                try:
                    response = int(input('Would you like to make another transfer? Type 1 for "Yes" and 2 for "No" \n'))
                    if response == 1:
                        self.transfer_funds()
                    elif response == 2:
                        try:
                            reply = int(input('Would you like to perform another operation? Type 1 for "Yes" and 2 for "No" \n'))
                            if reply == 1:
                                self.operation()
                            elif reply == 2:
                                print("Thank you")
                                self.operation()
                            else:
                                print("Invalid value supplied")
                                self.operation()
                        except ValueError:
                            print("Number is Expected")
                            self.operation()
                    else:
                        print("Invalid parameter supplied")
                        self.operation()
                except ValueError:
                    print("Number is Expected")
                    self.operation()
        except ValueError:
            print("Number is Expected")
            self.transfer_funds()

    # Get category balance function
    def get_balance(self):
        for category in self.category_balance:
            balance = self.category_balance[category]
            print(f"{category} balance: {balance}")
        try:
            response = int(input('Would you like to perform another operation? Type 1 for "Yes" and 2 for "No" \n'))
            if response == 1:
                self.operation()
            elif response == 2:
                print("Thank you for using this app")
                exit()
            else:
                print("Input not found, please try again")
                self.get_balance()
        except ValueError:
            print("Number is Expected")
            self.operation()

    # Get total balance of the categories all-together
    def get_total_balance(self):
        total_balance = 0
        for category in self.category_balance:
            balance = self.category_balance[category]
            total_balance += balance
        print(f"Total Balance: {total_balance}")
        try:
            response = int(input('Would you like to perform another operation? Select (1) for "Yes" and (2) for "No" \n'))
            if response == 1:
                self.operation()
            elif response == 2:
                print("Thank you for using this app")
                exit()
            else:
                print("Input not found, please try again")
                self.get_total_balance()
        except ValueError:
                print("Number is Expected")
                self.operation()

    # Adding new categories
    def add_new_category(self):
        supply_category = input("Supply Category Name: ")
        self.category_list.append(supply_category)
        self.category_balance[supply_category] = 0
        print("New Category successfully added")
        print(f"New Category List: {self.category_list} \nNew Category and Balance:  {self.category_balance}\n")
        try:
            response = int(input('Would you like add another category? Select (1) for "Yes" and (2) for "No" \n'))
            if response == 1:
                self.add_new_category()
            elif response == 2:
                try:
                    reply = int(input('Would you like to perform other operations? Select (1) for "Yes" and (2) for "No" \n'))
                    if reply == 1:
                        self.operation()
                    elif reply == 2:
                        print("Thank you")
                        exit()
                    else:
                        print("Not found. Operation complete")
                        self.operation()
                except ValueError:
                    print("Number is expected")
                    self.operation()
            else:
                print("Invalid value supplied")
                self.operation()
        except ValueError:
            print("Number is expected")
            self.operation()

Budget().app_main()
