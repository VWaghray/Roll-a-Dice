import random
response=str(input("Do you want to roll the dice. y or n: "))
while response == "y":
    no=random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  1  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[     ]")
        print("[  2  ]")
        print("[     ]")
        print("[-----]")
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  3  ]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[     ]")
        print("[  4  ]")
        print("[     ]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[     ]")
        print("[  5  ]")
        print("[     ]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[     ]")
        print("[  6  ]")
        print("[     ]")
        print("[-----]")
    response=str(input("Do you want to roll the dice again. y or n: "))