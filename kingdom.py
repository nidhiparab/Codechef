for ti in range(int(input())):
    inp = input()
    l = inp[len(inp)-1]
    alice = 0
    bob = 0
    vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if l in vowel:
        print("Case #{}: {} is ruled by Alice.".format(ti+1, inp))
    elif l == 'y' or l == 'Y':
        print("Case #{}: {} is ruled by nobody.".format(ti+1, inp))
    else:
        print("Case #{}: {} is ruled by Bob.".format(ti+1, inp))