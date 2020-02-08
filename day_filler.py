# this function will read the new date and the old date
# and fill the gaps in dates between inputs

def day_filler(sheet, date, date_old, wbb):
    import datetime
    import xlrd
    from xlrd import open_workbook

    rows = sheet.nrows
    if rows < 2:
        return rows
    
    date_old = datetime.datetime.strptime(date_old, '%Y-%m-%d')
    date_old = date_old.date()
    date_new = datetime.date.today()
    days = abs((date_new - date_old).days)
    if days > 1:
        for i in range(0, (days-1)):
            rowsx = rows + i
            date = date_old + datetime.timedelta(days = i+1)

            # excel cells input based on retrieved variables
            s = wbb.get_sheet(0)
            # date column input
            s.write(rowsx, 0, str(date))
            # time column input
            s.write(rowsx ,1, 0)

        rowsx = rowsx + 1
        return rowsx
    else:
        rowsx = rows
        return rowsx
