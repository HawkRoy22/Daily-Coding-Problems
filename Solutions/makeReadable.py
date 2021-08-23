def make_readable(seconds):
    hour = seconds // 3600
    tempOne = seconds - (3600 * hour)
    minutes = tempOne // 60
    sec = seconds - ((60 * minutes) + (3600 * hour))
    if(seconds % 60 == 0):
        print()
    elif(seconds < 10):
        print(f'00:00:0{seconds}')
    elif(seconds < 60 and seconds > 9):
        print(f'00:00:{seconds}')
    elif(seconds >= 60 and seconds < 3600):
        if(minutes < 10):
            print(f'00:0{minutes}:{sec}')
        else:
            print(f'00:{minutes}:{sec}')
    elif(seconds/3600):
        print(f'{hour}:{minutes}:{sec}')