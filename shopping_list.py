import os

menu = """

=========== SHOPPING LIST ===========
[i] Insert an item
[d] Delete an item
[l] List items
====================================

=> Select an option: """

shopping_list = []

while True:
    option = input(menu)
  
    if option == "i":
        # command to clear the terminal
        os.system('cls' if os.name == 'nt' else 'clear')  
        
        product = input("Product: ")
        shopping_list.append(product)

    elif option == "l":
        os.system('cls' if os.name == 'nt' else 'clear')

        if len(shopping_list) == 0:
            print("The shopping list is empty!")

        for index, product in enumerate(shopping_list):
            print(index, product)

    elif option == "d":

        try:
            delete_index = int(input("Choose the item you want to delete: "))
            del shopping_list[delete_index]    
            print("Item successfully removed!!")
        except ValueError:
            print("Please enter an integer.")
        except IndexError:
            print("The item does not exist in the list. Please try again.")
        except Exception:
            print("Unknown error.")

    else:
        print("Invalid option!! Please choose i, d, or l.")
