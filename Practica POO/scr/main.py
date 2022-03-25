from scr.clases.Land import Land


if __name__=="__main__":
    Movil1 = Land("Trek",1200,False)
    Movil2 = Land("Lamborgini",120000,True)
    movilList = [Movil1, Movil2]

    for Movil in movilList:
        Movil.tipo()