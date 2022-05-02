#have a help command 
def show_help():
    #print out instructions on how use app
    print("what show we pick up at the store")
    print("""
    Enter Done to stop adding items
    Enter Show to stop adding items
    Enter Help to stop adding items
    """)


def show_list():
    #print out the list
    print("Here's your list:")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    shopping_list.append(new_item) 
    print(f"Added {new_item}." +"List now has {} ".format(len(shopping_list)))



#make a list to hold onto our iyems
shopping_list = []

show_help()

while True :
    #ask for new items
    new_item=input("Entre new items:")
    #add new items to our list
    #be able to quit the app 
    if new_item == 'Done':
        show_list()
        break
    elif new_item =='Help':
        show_help()
        continue
    elif new_item == 'Show':
        show_list()
        continue

    add_to_list(new_item)
    


