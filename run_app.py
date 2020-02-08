# file to initialize when running app

# import functions
from new_habit import new_habit
from habits import habits


print('\nHey Dom! Welcome to the HabbitTracker.')

loop = True
while loop == True:
    x = input('\nWhat do you want to do? \n\nOptions: \n~ Create new habit: *new* \n~ Track habit: *habit name* \n~ Close: *close* \n')

    if x == 'new' or x == 'New' or x == 'NEW':
        habit = input('What habit is that? ')
        new_habit(habit)
        # form new habbit
    elif x == 'close' or x == 'Close' or x == 'CLOSE':
        # end loop to close
        print('Ok, hope you had a good time. Bye!')
        loop = False

    else:
        # sort through habbits (main working space)
        [date, time] = habits(x)
        print(['The time of focus was: ' + str(time) + ' minutes.'])
        print(['The date of recording was: ' + str(date)])
