def make_readable(seconds):
    hours = seconds // 3600
    remainder = seconds - hours * 3600
    min = remainder // 60
    remainder = remainder - min * 60
    sec = remainder
    
    readable_time = "{:02d}:{:02d}:{:02d}".format(hours,min,sec)
    return readable_time

#first solution:

def make_readable(seconds):
    hours = seconds // 3600
    remainder = seconds - hours * 3600
    min = remainder // 60
    remainder = remainder - min * 60
    if remainder <= 59:
        sec = remainder
    else:
        sec = 59
        
    readable_time = "{:02d}:{:02d}:{:02d}".format(hours,min,sec)
    return readable_time

