from datetime import datetime

def logger_time(func):
    def wrapped_func(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_date = datetime.now()
        duration = end_date - start_time
        print(f"Elapsed Time == {duration.seconds // 3600}h:{duration.seconds // 60}m:{duration.seconds % 60}s")
        return result

    return wrapped_func