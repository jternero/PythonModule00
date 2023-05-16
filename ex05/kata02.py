kata = (2019, 9, 25, 3, 30)

import sys



def kata_do():
    date =  "{:02d}/{:02d}/{:04d}".format(kata[1], kata[2], kata[0])
    time = "{:02d}:{:02d}".format(kata[3], kata[4])
    print(f"{date} {time}")
    return
if __name__ == "__main__":
    if len(sys.argv) == 1:
        kata_do()
    elif len(sys.argv) > 1 and sys.argv[1] == "new_data":
        print(f"Enter year (1990-2023)")
        year = int(input())
        while year < 1990 or year > 2023:
            year = int(input("Invalid input. Enter Year (1990-2023): "))
        print(f"Enter Month (1-12):   ")
        month = int(input())
        while month < 1 or month > 12:
            month = int(input("Invalid input. Enter Month (1-12): "))
        print(f"Enter Day (1-31):     ")
        day = int(input())
        while day < 1 or day > 31:
            day = int(input("Invalid input. Enter Day (1-31): "))
        print(f"Enter Time - Hour (0-23):    ")
        hour = int(input())
        while hour < 0 or hour > 23:
            hour = int(input("Invalid input. Enter Time - Hour (0-23): "))
        print(f"Enter Time - Minute (0-59):     ")
        minute = int(input())
        while minute < 0 or minute > 59:
            minute = int(input("Invalid input. Enter Time - Minute (0-59): "))
        kata = (year, month, day, hour, minute)
        kata_do()
    else:
        print("Error: Too many arguments")