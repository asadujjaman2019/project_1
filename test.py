number=int(input("how_many_number="))

for i in range(1,number+1):
    number_of_space = number - i
    for j in range(1,i+1):
        if j==1:
            print(" "*number_of_space,end="")
        print(j,end="")
    print()