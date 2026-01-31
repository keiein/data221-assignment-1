#assignment_question_7.py
#convert seconds into hours, mins, seconds, AM/PM

def convert_seconds_to_clock(seconds_since_midnight:int) -> str: #Define function taking in seconds
    if seconds_since_midnight < 0 or seconds_since_midnight > 86400: #has to be within 24 hours
        return 'Seconds since midnight must be between 0 and 86399.'

    #time conversion
    hours = seconds_since_midnight // 3600
    minutes = (seconds_since_midnight % 3600) // 60
    seconds = (seconds_since_midnight % 3600) % 60

    midday_system = 'AM'
    if hours >= 12:
        midday_system = 'PM'

    clock_hours = hours
    if hours == 0:
        clock_hours = 12
    elif hours > 12:
        clock_hours = hours - 12

    return f"{clock_hours} {minutes:02} {seconds:02} {midday_system}" #formatted string

#print(convert_seconds_to_clock(4942))