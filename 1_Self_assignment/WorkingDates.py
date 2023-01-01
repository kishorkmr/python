from datetime import date, datetime, timedelta

def get_WorkingDates(StartDate, EndDate):
    start_date = datetime.strptime(StartDate,"%d-%b-%y") .date()
    end_date = datetime.strptime(EndDate,"%d-%b-%y") .date()

    print('Start date:', start_date)
    print('End date:', end_date)

    Working_DayDates = []

    delta = end_date - start_date   # returns timedelta
    #Print week days only
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        week_day = day.weekday()
        if week_day < 5:
            #print(day)
            Working_DayDates.append({'Working_Day':week_day, 'Working_Date':day})

    return Working_DayDates
    

def main():    
    #Enter dates in DD-MMM-YY format
    StartDate = '01-DEC-22'
    EndDate = '10-DEC-22'
    print(get_WorkingDates(StartDate, EndDate))

#main()