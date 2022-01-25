def time(seconds):
    minutes = 60
    hour = 3600
    if seconds <= minutes:
        mm = seconds / minutes
        print(f"00:{int(mm)}:{minutes-1}")
    elif seconds >= hour:
        hh = seconds / hour
        print(f"{int(hh)}:{minutes-1}:{minutes-1}")


seconds = 359999
time(seconds)
