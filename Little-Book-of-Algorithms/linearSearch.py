def linear_search(target):
    names = ["Rocky", "Connor", "Jawwad",
"Yacoub", "Cara", "Jess",
"Jake", "Suki", "Zi", "Q"]
    found = False
    for count in range(len(names)):
        if target.lower() == (names[count]).lower():
            print(target, "found at position", count)
            found = True
    if found == False:
        print(target, "was not found")
name = input("Who are you looking for? ")
linear_search(name)