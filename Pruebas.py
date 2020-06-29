prueba = input()
stringlength = len(prueba)
slicedString = prueba[stringlength::-1]


if prueba == slicedString:
    print("Palindrome")
else:
    print("Not palindrome")




