def time(seconds):
    minutes = 60
    hour = 3600
    if seconds >= minutes:
        mm = seconds / minutes
        print(f"{mm}:{minutes-1}")


seconds = 60
time(seconds)
