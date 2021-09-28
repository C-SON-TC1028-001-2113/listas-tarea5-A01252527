
def main():
    a = int(input(''))
    aa = int(input(''))
    aaa = a*aa
    lista=[]
    i=1
    while i<=aaa:
        i=i+1
        aaaa = int(input(''))
        if aaaa<10:
            lista.append(aaaa)
    print(lista)

if __name__=='__main__':
    main()
