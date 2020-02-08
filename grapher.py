# graphing function that visualizes data

# shuffle through the created habbits

def grapher(habit):
    import xlwt
    import xlrd
    from xlwt import Workbook
    from xlrd import open_workbook
    from xlutils.copy import copy
    import datetime
    from day_filler import day_filler
    import matplotlib.pyplot as plt

    # path to chosen excel sheet
    loc = ("/Users/dominikcydzik/Desktop/Coding/habbit_tracker/habit_stats/" + habit + ".xls")
    # open workbook in xlrd and xlwt
    wb = open_workbook(loc)
    wbb = copy(wb)
    sheet = wb.sheet_by_index(0 )
    # saving the value of rows used
    rows = sheet.nrows

    # fill out the empty dates with zero values to complete week
    date_old = str(sheet.cell_value(rows-1, 0))
    date = datetime.date.today()

    if date_old != date:
        day_filler(sheet, date, date_old, wbb)

    save_name = loc
    wbb.save(save_name)

    # create graphing function that graphs the last 7 days recorded
    ##print('You have ' rows ' recorded.')
    ##x = input('')
    x = []
    y = []
    for i in range(1, rows):
        x.append('Day ' + str(i))
        y.append(sheet.cell_value(i,1))


    # consider an automated weekly e-mail that sends
    # you an update on all the habits you engaged in
    #
    # consider all habits grapher

    # set figure parameters
    fig = plt.figure(figsize=(12,8))

    # subplot of chart
    #plt.subplot(2,1,1)
    # plotting the points
    plt.bar(x, y)

    # naming the x axis
    plt.xlabel('Dates')
    plt.xticks(rotation=90)
    # naming the y axis
    plt.ylabel('Time (min)')

    # giving a title to my graph
    plt.title('Summary: ' + habit)

    # subplot of statistical summary
    #plt.subplot(2,1,2)
    #plt.text(0.5, 0.1, 'Summary')

    # function to show the plot
    plt.show()


    return
