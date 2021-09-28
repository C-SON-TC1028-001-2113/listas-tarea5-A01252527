def main():
    #escribe tu código abajo de esta línea 
    y = int(input())
    nombres = []
    x = 0
    if y>0 :
        while x<y :
            valor = input()
            nombres.append(valor)
            x = x+1
        print(nombres)
        noduplicados = []
        for x in nombres :
            if x not in noduplicados:
                noduplicados.append(x)
        print(noduplicados)
    else:
        print('Error')
    
    pass


if __name__=='__main__':
    main()
