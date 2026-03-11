from random import randrange
def show_menu():
    while True:
        print("""\n \n Digital Time Capsule

1 - Create a time capsule
2 - View saved capsules
3 - Open a capsule
4 - Random message from the future
5 - Exit""")
        a=int(input('inset an option: '))

        if a == 1:
            create_capsule()
        elif a == 2:
            view_capsules()
        elif a == 3:
            open_capsule()
        elif a == 4:
            random_future_message()
        elif a == 5:
            print('Good bye time traveler ;)') 
            break
        else:
            print('\n You must insert an existent option',end='\n')
def create_capsule():
    b=input('Write a message for your future self: ')
    if b == '' :
        print('message can not be empty')
        return
    c=int(input('How many years in the future should it open?'))
    if c <= 0 :
        print('years must be a positive integer')
        return
    messages.append(b)
    years.append(c)
def view_capsules():
    if messages == [] or years == []:
        print('No capsules created yet.')
    else:
        for i, msg in enumerate(messages):
            print(i + 1, "-", msg, "(opens in", years[i], "years)")
def open_capsule():
    d=int(input('Enter capsule number: '))
    if d > 0 and d <= len(messages):
        print('''Opening capsule...

        Message from the past:'''
        , messages[d-1])
    else:
        print("Invalid capsule number.")
def random_future_message():
    future_messages = [
    "You made it further than you expected.",
    "Your hard work paid off.",
    "You survived the difficult times.",
    "Keep going, you're on the right path.",
    "Your future self is proud of you."]
    print(future_messages[randrange(len(future_messages))])
def run_time_capsule():
    show_menu()
messages = []
years = []
run_time_capsule()
