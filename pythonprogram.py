def newbeginning(i):
    while i != 0:
        if i > 0:
            print(i);
            i = i - 1
        elif i < 0:
            print(i);
            i = i + 1
        else:
            break
    print("This is the new beginning..");

print(newbeginning(15));