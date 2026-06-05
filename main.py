import time
name = input("Please enter your name: ")
timestamp = time.strftime("%H", time.localtime())
match timestamp:
    case _ if timestamp >= "20" or "00" <= timestamp < "04":
        print(f"Good Night, {name}!")
    case _ if "04" <= timestamp <= "10":
        print(f"Good Morning, {name}!")
    case _ if "10" < timestamp <= "18":
        print(f"Good Afternoon, {name}!")
    case _:
        print(f"Good Evening, {name}!")
print("Current timestamp:", timestamp)


