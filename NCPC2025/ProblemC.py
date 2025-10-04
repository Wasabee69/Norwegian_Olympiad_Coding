###


def solve(start_time, end_time):
    if start_time == end_time:
        return f"7 days"

    days = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}
    ms = int(start_time[7:])
    me = int(end_time[7:])
    hs = int(start_time[4:6]) * 60
    he = int(end_time[4:6]) * 60
    ds = days[start_time[:3]] * 24 * 60
    de = days[end_time[:3]] * 24 * 60

    minutes_one_week = 60 * 24 * 7

    minutes_start = ms + hs + ds
    minutes_end = me + he + de


    if minutes_end < minutes_start:
        minutes = minutes_one_week - minutes_start + minutes_end

    else:
        minutes = minutes_end - minutes_start

    days, minutes = divmod(minutes, 60 * 24)
    hours, minutes = divmod(minutes, 60)

    res = []
    plural = lambda x, y: x + "s" if y > 1 else x
    days_string = plural("day", days)
    hours_string = plural("hour", hours)
    minutes_string = plural("minute", minutes)

    if days:
        if hours:
            if minutes:
                return f"{days} {days_string}, {hours} {hours_string}, {minutes} {minutes_string}"
            return f"{days} {days_string} and {hours} {hours_string}"
        elif minutes:
            return f"{days} {days_string} and {minutes} {minutes_string}"
        else:
            return f"{days} {days_string}"
    if hours:
        if minutes:
            return f"{hours} {hours_string} and {minutes} {minutes_string}"
        return f"{hours} {hours_string}"
    return f"{minutes} {minutes_string}"




start_time = input()
end_time = input()
print(solve(start_time, end_time))
