from modelos.restaurante import Restaurante 

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_mexicano = Restaurante('El Mexico', 'Mexicana')
restaurante_lanche = Restaurante('Careca Lindo', 'Lanche')
 
restaurante_lanche.receber_avaliacao('Marcio', 9)
restaurante_lanche.receber_avaliacao('Vinicius', 10)
restaurante_lanche.receber_avaliacao('Breno', 6)

def main():
    Restaurante.lista_restaurantes()

if __name__ == '__main__':
    main() 

