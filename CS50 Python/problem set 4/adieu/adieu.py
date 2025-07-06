Name=[]

def get_name():
    while True:
        try:
            name=input()
            Name.append(name)
        except EOFError:
            break

def output_name():
    print("Adieu, adieu, to ",end='')
    num=len(Name)
    if num==1:
        print(Name[0])
    elif num==2:
        print(f"Adieu, adieu, to {Name[0]} and {Name[1]}")
    else:
        for keys in range(num-1):
            print(f"{Name[keys]}, ",end='')
        print(f"and {Name[num-1]}")



get_name()
output_name()
