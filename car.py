print("CAR LOOP BY ** ELLIOT BAZUAYE **")
print("")
count = ""
started = False
while count != "EXIT":
    car = input(">   ").upper()
    if car == "HELP":
        print("""
start = To start car
stop = to stop car
quit = to exit
          """)

    elif car == "START":
        if started:
            print("already Started")
        else:
            started = True
            print(" Car started...")

    elif car == "STOP":
        if not started:
            print("car already stopped")
        else:
            started = False
            print(" Car stopped.")

    elif car == "EXIT":
        print("exited, Good bye")
        break
    else:
        print("i don't understand")
