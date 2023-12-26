class Elevador:
   
    
    def __init__(self, andares_totais):
        self.andares_totais = andares_totais
        self.andar_atual = 1

    def ir_para_andar(self, destino):
        
        if 1 <= destino <= self.andares_totais:
            self.andar_atual = destino
            print(f"Elevador agora está no andar {destino}.")
        else:
            print("Andar inválido. Por favor, escolha um andar dentro do intervalo permitido.")

# Exemplo de uso
elevador = Elevador(andares_totais=10)
elevador.ir_para_andar(destino=10)
