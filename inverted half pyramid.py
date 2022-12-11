print("Inverted Half Pyramid of Stars (*):")
n=int(input(' Enter = '))
for i in range(n):
    for j in range(i, n):
        print("* ", end="")
    print()
