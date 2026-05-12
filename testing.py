def times_ten(start_index:int, end_index:int):
    times = {}
    for key in range(start_index,end_index+1):
        value = key*10
        times[key] = value
    return times

if __name__ == "__main__":
    print(times_ten(3,6))








