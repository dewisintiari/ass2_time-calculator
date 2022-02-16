
# converting the day strings into day indexes
def get_day_id(day):
    if day == 'Sunday':
        day_id = 0
    elif day == 'Monday':
        day_id = 1
    elif day == 'Tuesday':
        day_id = 2
    elif day == 'Wednesday':
        day_id = 3
    elif day == 'Thursday':
        day_id = 4
    elif day == 'Friday':
        day_id = 5
    else: 
        day == 'Saturday'
        day_id = 6
    return day_id

# converting the day indexes into day strings
def get_day(day_id):
    if day_id == 0:
        day = 'Sunday'
    elif day_id == 1:
        day = 'Monday'
    elif day_id == 2:
        day = 'Tuesday'
    elif day_id == 3:
        day = 'Wednesday'
    elif day_id == 4:
        day = 'Thursday'
    elif day_id == 5:
        day = 'Friday'
    else: 
        day_id == 6
        day = 'Saturday'
    return day


# Converting daylight indicator to boolean value
# morning is a boolean value indicating the daylight (morning = True means that it is a AM time)

def get_daylight(morning):
    if morning == True:
        daylight = 'AM'
    else:
        daylight = 'PM'
    return daylight

def get_daylight_val(daylight):
    if daylight == 'AM':
        morning = True
    elif daylight == 'PM':
        morning = False
    return morning


def add_time(start, duration, day=None):

    # Extracting the hours, minutes, and daylight indicator from the input
    start_time = start.split()[0]
    start_hour = start_time.split(':')[0]
    start_min = start_time.split(':')[1]
    duration_hour = duration.split(':')[0]
    duration_min = duration.split(':')[1]
    daylight = start.split()[1]

    # Check if a typo in the input is found
    try:
        int(start_hour)
        int(start_min)
        int(duration_hour)
        int(duration_min)
    except:
        return "Check if there is a typo in the input"

    # Convert the input string into integer
    val_start_hour = int(start_hour)
    val_start_min = int(start_min)
    val_duration_hour = int(duration_hour)
    val_duration_min = int(duration_min)
    
    # Adding the current time with the duration
    morning = get_daylight_val(daylight)

    if morning == False:
        if val_start_hour == 12:
            if val_start_min == 0:
                pass
        else:
            val_start_hour += 12
    
    hour = val_start_hour + val_duration_hour
    minute = val_start_min + val_duration_min
    
    # Converting the excessive minutes into hour
    new_hour = hour
    new_minute = minute
    day_incr = 0               # indicator for today's time

    while new_minute > 60:
        new_hour += 1          # convert each 60 minutes into 1 hour
        new_minute -= 60
    
    if morning == False:
        if new_hour == 24:     # if the total hour exceeds 24, then we jump to the next day
            day_incr = 1

    while new_hour >= 24:
        new_hour -= 24
        day_incr += 1

    # Setting the daylight indicator
    if new_hour > 12:
        morning = False
        new_hour -= 12
    elif new_hour == 12:
        if val_duration_hour <= 12:
            morning = not morning
    else:
        morning = True
    daylight = get_daylight(morning)

    # Conversion of the day
    if day is None:
        pass
    else:
        day.casefold()          # the casefold() method returns a string where all the characters are in lower case
        day_id = get_day_id(day)
        new_day_id = (day_id + day_incr) % 7
        new_day = get_day(new_day_id)

    # Return the result
    if new_hour == 0:
        new_hour = 12
    if day is None:
        if day_incr == 0:
            return str(new_hour) + ':' + f"{new_minute:02}" + " " + daylight
        elif day_incr == 1:
            return str(new_hour) + ':' + f"{new_minute:02}" + " " + daylight + " (next day)"
        else:
            return str(new_hour) + ':' + f"{new_minute:02}" + " " + daylight + " (" + str(day_incr) + " days later)"
    else:
        if day_incr == 0:
            return str(new_hour) + ':' + f"{new_minute:02}" + " " + daylight + ', ' + new_day 
        elif day_incr == 1:
            return str(new_hour) + ':' + f"{new_minute:02}" + " " + daylight + ', ' + new_day + " (next day)"
        else:
            return str(new_hour) + ':' + f"{new_minute:02}" + " " + daylight + ', ' + new_day + " (" + str(day_incr) + " days later)"
        