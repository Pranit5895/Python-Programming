def convert_seconds(seconds):
    hours = seconds // 3600
    mintues = (seconds - hours *3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
