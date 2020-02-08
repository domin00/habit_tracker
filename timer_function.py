# this function will do all the
# time manipulation for this app

def timer_function():
    import datetime

    # implement if_cond to decide for manual or automated input of time

    choice = input("'auto' or 'manual'? ")

    if choice == 'auto':
        x = input("Type 'start' to start: ")

        if x == 'start':
            a = datetime.datetime.now()
            #a = a.total_seconds()

        x = input("Type 'stop' to stop: ")

        if x == 'stop':
            b = datetime.datetime.now()
            #b = b.total_seconds()

        time = (b - a)
        time = (time.seconds)/60
        timer = round(time, 2)

        return timer
    elif choice == 'manual':
        timer = int(input('Duration of focus: '))

        return timer
