
def new_habit(habit):
    import xlwt
    import xlrd
    from xlrd import open_workbook
    from xlwt import Workbook

    wb = Workbook()
    sheet1 = wb.add_sheet(habit)

    sheet1.write(0,0, habit.upper())
    sheet1.write(0,1, 'TIME')
    save_name = '/habit_stats/' + habit + '.xls'
    
    wb.save(save_name)
