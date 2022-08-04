while True:

    myString = input("Editor")
    editor = myString.lower()

    if editor == "word" or editor == "notepad":
        print("awful")
    elif editor == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")