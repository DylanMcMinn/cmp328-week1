def read_int(prompt):
    while True:
        text= input(prompt)
        if text.strip().lstrip(".").isdigit():
            return int(text)
        print("Please enter a whhole number (e.g. 42)")

w = read_int("width: ")
h= read_int("height: ")
print("Area:", w*h)