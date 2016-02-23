def power_seq():
    x = input("Please write some sequences of numbers, and separate them with ',': ")
    d = int(input("Please write the degree you want your first number to be put in:"))
    args = x.split(",")
    print(args)
    args.insert(0, d)
    i = 0
    for l in args:
        s = int(args[i-1])
        k = int(l)
        i += 1
        print(k**s)
print(power_seq())
