class Blackjack:
    def registrar_jugador(self, nombre: str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass

    def comparar_manos(self):
        pass

class Carta:
    def __init__(self, valor: str, pinta: str):
        self.valor: str = valor
        self.pinta: str = pinta

class Baraja:
    def revolver(self):
        pass

    def repartir_carta(self, tapada: bool) -> Carta:
        pass

    def pedir_carta(self) -> bool:
        pass

class Mano:
    def __init__(self, carta):
        pass

    def es_blackjack(self) -> bool:
        pass

    def plantarse(self) -> bool:
        pass

class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas

    def inicializar_mano(self, cartas):
        pass

    def hacer_jugada(self):
        pass

    def fichas_disponibles(self) -> bool:
        pass

class Casa:
    def inicializar_mano(self, carta):
        pass

    def hacer_jugada(self):
        pass



