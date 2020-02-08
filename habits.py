# shuffle through the created habbits

def habits(habit):
    import xlwt
    import xlrd
    from xlwt import Workbook
    from xlrd import open_workbook
    from xlutils.copy import copy
    import datetime
    from timer_function import timer_function
    from day_filler import day_filler
    from grapher import grapher

    # new log or continuation of last log conditional
    xx = str(input('Options:\n1. Log\n2. Graph\n'))
    # path to chosen excel sheet
    loc = ("/Users/dominikcydzik/Desktop/Coding/habbit_tracker/habit_stats/" + habit + ".xls")
    # open workbook in xlrd and xlwt
    wb = open_workbook(loc)
    wbb = copy(wb)
    sheet = wb.sheet_by_index(0 )
    # saving the value of rows used
    rows = (sheet.nrows)
    rowsx = rows - 1
    # conditional based on input
    if xx == '1':
        # progress to new row of sheet
        date_old = str(sheet.cell_value(rows-1, 0))

        date = str(datetime.date.today())
        time = 0
        if date_old != date:
            rowsx = day_filler(sheet, date, date_old, wbb)
        else:
            rowsx = rows - 1
            date = sheet.cell_value(rowsx, 0)
            time = sheet.cell_value(rowsx, 1)

        # timer function
        timer = timer_function()
        time = time + timer
        # excel cells input based on retrieved variables
        s = wbb.get_sheet(0)
        # date column input
        s.write(rowsx, 0, str(date))
        # time column input
        s.write(rowsx ,1, time)
        save_name = loc
        wbb.save(save_name)
        return [date, time]

    elif xx == '2':
        # graph data for specific skill tracker
        grapher(habit)
        date = sheet.cell_value(rowsx, 0)
        time = sheet.cell_value(rowsx, 1)
        return [date, time]
