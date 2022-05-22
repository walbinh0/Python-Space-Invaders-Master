class Colisao:

    @staticmethod
    def colisaoX(posicaoX, tamanhoX, posicaoX2, tamanhoX2):
        return posicaoX + tamanhoX >= posicaoX2 and posicaoX <= posicaoX2 + tamanhoX2
    
    @staticmethod
    def colisaoY(posicaoY, tamanhoY, posicaoY2, tamanhoY2):
        return posicaoY + tamanhoY >= posicaoY2 and posicaoY <= posicaoY2 + tamanhoY2
    
    @staticmethod
    def checa_colisao(entidade1, entidade2):
        return Colisao.colisaoX(entidade1.rect.x, entidade1.tamanho['x'], entidade2.rect.x, entidade2.tamanho['x']) and Colisao.colisaoY(entidade1.rect.y, entidade1.tamanho['y'], entidade2.rect.y, entidade2.tamanho['y'])
    

