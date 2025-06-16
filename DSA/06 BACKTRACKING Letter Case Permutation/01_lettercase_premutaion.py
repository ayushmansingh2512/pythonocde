def letterCase(s):
    output = [""]
    for c in s:
        print("c:", c)
        tmp = []
        if c.isalpha():
            for o in output:
                print("___________________________________________________")
                tmp.append(o + c.lower())
                tmp.append(o + c.upper())
                print("-------------------------------------------------")
        else:
            print("_________________________Big")
            for o in output:
                tmp.append(o + c)  # fixed operator
            print("tmp after adding num:", tmp)
            print("_________________________Big")

        output = tmp  # fixed typo from tnp to tmp
        print("output after main iteration:", output)

    return output

print(letterCase("a1b2"))
