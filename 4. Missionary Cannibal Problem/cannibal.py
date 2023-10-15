n = 3

left = (n, n)
right = lambda: (n-left[0], n-left[1])
boat = [0, 0]
direction = True
items = {
    0: "missionaries",
    1: "cannibals",
}

def show_state(dir: bool):
    print("M "*left[0] + "C "*left[1], end="")
    print("| --> |", end=" ") if dir else print("| <-- |", end=" ")
    print("M "*right()[0] + "C "*right()[1])

def check_state():
    show_state(direction)
    if left[1]>left[0] or right()[1]>right()[0]:
        if left[0]==0 or right()[0]==0:
             return True
        print("Game over...")
        return False
    if right()[0] == 3 and right()[1] == 3:
        print("You won.")
        return False
    return True

def get_input():
    while True:
        for i in range(2):
            while True:
                try:
                    boat[i] = int(input(f"Enter the number of {items[i]} > "))
                except ValueError:
                    boat[i] = 0
                finally:
                    if direction:
                        if boat[i]<=left[i]:
                            break
                    else:
                        if boat[i]<=right()[i]:
                            break
                    print("Invalid input.")
        if boat[0] + boat [1] > 0 and boat[0] + boat [1] <= 2:
            break
        else:
            print("Invalid input.")

while check_state():
    get_input()
    
    if direction:
        left = (left[0]-boat[0], left[1]-boat[1])
        direction=False
    else:
        left = (left[0]+boat[0], left[1]+boat[1])
        direction=True