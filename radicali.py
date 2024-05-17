class MiaClasse:
    def __init__(self, nome):
        self.nome = nome

    def radicali(self):
        for i in range(317, 999):
            quadrato = i*i
            prime = quadrato // 1000
            seconde = quadrato % 1000
            somma = prime + seconde
            corretto = somma == i
            if corretto:
                print(f"n={i} \t quadrato={quadrato} \t prime={prime} \t seconde={seconde} \t somma={somma} \t corretto={corretto}")


if __name__ == "__main__":
    # Crea un'istanza della classe
    istanza = MiaClasse("Giulia")

    # Chiama il metodo saluta
    istanza.radicali()
