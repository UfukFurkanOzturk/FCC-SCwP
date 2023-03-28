def add_time(start, duration, day=None):
    # separate starting time to pieces
    arr = start.split(":")
    hour = int(arr[0])
    minutes = int(arr[1][:-3])
    ampm = arr[1][3:]

    # separate duration
    arr2 = duration.split(":")
    dhour = int(arr2[0])
    dminutes = int(arr2[1])

    # total hour and total minutes as integer
    thour = hour + dhour
    tminutes = minutes + dminutes

    # converting midday to integer to make get day cycle easier
    if ampm == "AM":
        ampm = 0
    elif ampm == "PM":
        ampm = 1

    if tminutes >= 60:
        tminutes = tminutes - 60
        thour = thour + 1

    # check length of total minutes less than 2
    if len(str(tminutes)) < 2:
        tminutes = str(tminutes).rjust(2, "0")

    # calculate how many middays passed
    for i in range(int(thour/12)):
        ampm += 1

    # make total hour something we actually can return as time
    thour = thour - (24 * int(thour/24))
    if thour > 12:
        thour = thour - 12

    # calculate how many days passed
    if ampm % 2 == 0:
        daynum = int(ampm / 2)
        ampm = "AM"
    elif ampm % 2 == 1:
        daynum = int((ampm - 1) / 2)
        ampm = "PM"

    if day is not None:
        day = day.lower()
        day = day.capitalize()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        rday = days[(days.index(day) + daynum) % 7]
        rday = ", " + rday
    else:
        rday = ''

    if daynum == 0:
        new_time = str(thour) + ":" + str(tminutes) + " " + ampm + rday
    elif daynum == 1:
        new_time = str(thour) + ":" + str(tminutes) + " " + ampm + rday + " " + "(next day)"
    elif daynum >= 2:
        new_time = str(thour) + ":" + str(tminutes) + " " + ampm + rday + " " + f"({daynum} days later)"

    return new_time
