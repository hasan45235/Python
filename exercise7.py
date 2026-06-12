
timer = int(input("Enter Timer Seconds: "))

def createTimer(n):
    if n == 0 or n == 1:
        print(f"{n}\nBlast Off")
        
        return n 
    else:
        print(n)
        return createTimer(n-1)

createTimer(timer)