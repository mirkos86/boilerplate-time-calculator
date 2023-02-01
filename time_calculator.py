def add_time(start,duration,startDay=None):
    """Write a function named add_time that takes in two required parameters and one optional parameter:
    1. a start time in the 12-hour clock format (ending in AM or PM)
    2. a duration time that indicates the number of hours and minutes (optional) a starting day of the week, 
    case insensitive

    The function should add the duration time to the start time and return the result.
    If the result will be the next day, it should show (next day) after the time. 
    If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
    If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. 
    The day of the week in the output should appear after the time and before the number of days later.
    Do not import any Python libraries. Assume that the start times are valid times. 
    The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
    """
    weekdays=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    if startDay !=None:
        start_day = weekdays.index(startDay.lower())
    
    start_time = start.split(" ")
    start_half = start_time[1]
    
    if start_half == "AM":
        day_half = 0
    else:
        day_half = 1
    
    start = start_time[0].split(":")
    start_hours = int(start[0]) + day_half*12
    start_minutes = int(start[1])
    
    duration_time = duration.split(" ")
    durationHM = duration_time[0].split(":")
    duration_hours = int(durationHM[0])
    duration_minutes = int(durationHM[1])
    
    final_minutes = str((start_minutes+duration_minutes)%60)
    
    if len(final_minutes) < 2: 
        final_minutes = "0"+final_minutes

    extra_hours = int((start_minutes+duration_minutes)/60)
    final_hours = (start_hours+duration_hours+extra_hours)%24
    
    if final_hours == 0:
      final_hours = str(12)
      final_half="AM"
                
    elif final_hours==12:
        final_hours=str(12)
        final_half="PM"
    
    elif final_hours > 12:
        final_hours=str(final_hours-12)
        final_half="PM"

    else:
        final_hours=str(final_hours)
        final_half="AM"

    
    extra_days = int((start_hours+duration_hours+extra_hours)/24)
    
    new_time_hm = str(final_hours) +":" +str(final_minutes) +" " +final_half
    
    if startDay==None:
            if extra_days==0:
                new_time = new_time_hm
            elif extra_days==1:
                new_time = new_time_hm +" (next day)"
            else:
                new_time = new_time_hm +" ("+str(extra_days)+" days later)"
    else:
        
        final_day = weekdays[(start_day+extra_days%7)%7].capitalize()
        
        if extra_days==0:
            new_time = new_time_hm +", " + final_day 
        elif extra_days==1:
            new_time = new_time_hm +", " +final_day + " (next day)"
        else:
            new_time = new_time_hm +", " +final_day +" (" +str(extra_days) +" days later)"
        

    return new_time
    