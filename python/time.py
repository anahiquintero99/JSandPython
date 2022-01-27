def twoDigits(number):
    return (f"0:{number}")


def time(seconds):
    minutes = 60
    hour = 3600

    hh = int(seconds / hour)
    secondsM = (seconds - (hh * hour))
    mm = int(secondsM / 60)
    ss = secondsM - (mm * minutes)

    if hh < 10:
        hh = twoDigits(hh)
    if mm < 10:
        mm = twoDigits(mm)
    if ss < 10:
        ss = twoDigits(mm)

    print(f"{hh}:{mm}:{ss}")


seconds = 86399
time(seconds)
