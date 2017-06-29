def resolveHanoi(discos, origem, destino,auxiliar):
    if (discos > 0):
        resolveHanoi(discos-1,origem,auxiliar,destino)
        print("Mover disco ", discos, " de ", origem, " para ", destino)
        resolveHanoi(discos-1,auxiliar,destino,origem)
resolveHanoi(4,"haste inicial","haste final","haste auxiliar")
    
