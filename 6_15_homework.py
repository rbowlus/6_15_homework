#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.display import clear_output as co

def show_instructions():
    print("""Type 'add' to add new product to your cart.
Type 'quit' to exit the program.
Type 'show' to list all products in your cart.
Type 'delete' if you want to remove item from cart.""")

def shopping_cart():
    input('Welcome to Shopping Cart! Press any key to continue ')
    
    done = False
    info = []
    
    while not done:
        co()
        
        show_instructions()
        choice = input('What is your choice? ')
        
        if choice == 'add':
            product = input("Type in the product name.\n ").lower()
            
            product_dict = {
                'product': product
            }
            
            info.append(product_dict)
            
        elif choice == 'show':
            for stuff in info:
                print(stuff)
            input('Press any key continue')
            
        elif choice == 'delete':
            for stuff in info:
                print(stuff)
            prod_delete = input('Type in product you wish to delete:\n').lower()
            del product_dict['product']
            
        elif choice == 'quit':
            confirm = input('Are are you sure you want to quit? Y/N? ').lower()
            if confirm == 'y':
                for stuff in info:
                    print(stuff)
                done = True
            elif confirm == 'n':
                continue
    
shopping_cart()


# In[ ]:


from IPython.display import clear_output as co

def show_instructions():
    print("""Type 'add' to add new product to your cart.
Type 'quit' to exit the program.
Type 'show' to list all products in your cart.
Type 'delete' if you want to remove item from cart.""")

