print("Full Pyramid Pattern of Stars (*): ")


n=int(input('enter = '))
q=n+1
for i in range(n):
    for s in range(-q, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()
