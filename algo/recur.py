def countdown(x):
    if x ==0:
        print("Done!")
    else:
        print(x,"... ", end='')
        countdown(x-1)

countdown(4)
