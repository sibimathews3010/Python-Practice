def timeConversion(s):
    # Extract hours, minutes, and seconds
    hh, mm, ss_ampm = map(int, s[:-2].split(":"))
    ampm = s[-2:]

    # Convert to military time
    if ampm == 'PM' and hh != 12:
        hh += 12
    elif ampm == 'AM' and hh == 12:
        hh = 0

    # Format the result
    military_time = "{:02d}:{:02d}:{:02d}".format(hh, mm, ss_ampm)

    return military_time

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
