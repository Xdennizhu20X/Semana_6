from abc import ABC, abstractmethod

class Cola(ABC):

    @abstractmethod
    def encolar(self, elemento):
        pass

    @abstractmethod
    def desencolar(self):
        pass

    @abstractmethod
    def ver_frente(self):
        pass

    @abstractmethod
    def esta_vacia(self):
        pass

    @abstractmethod
    def tamano(self):
        pass

class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None

class ColaListaEnlazada(Cola):
    def __init__(self):
        self.frente = None
        self.final = None
        self._tamano = 0

    def encolar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self._tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        elemento = self.frente.elemento
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self._tamano -= 1
        return elemento

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.frente.elemento

    def esta_vacia(self):
        return self.frente is None

    def tamano(self):
        return self._tamano

def mostrar_menu():
    print("\nOperaciones de Cola:")
    print("1. Encolar")
    print("2. Desencolar")
    print("3. Ver Frente")
    print("4. Verificar si está vacía")
    print("5. Ver tamaño de la cola")
    print("6. Salir")

# Ejemplo de uso con interacción del usuario
cola = ColaListaEnlazada()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        elemento = input("Ingresa el elemento a encolar: ")
        cola.encolar(elemento)
        print(f"Elemento '{elemento}' encolado.")
        
    elif opcion == '2':
        elemento = cola.desencolar()
        if elemento is None:
            print("La cola está vacía, no se puede desencolar.")
        else:
            print(f"Elemento '{elemento}' desencolado.")
    
    elif opcion == '3':
        elemento = cola.ver_frente()
        if elemento is None:
            print("La cola está vacía.")
        else:
            print(f"El elemento en el frente es: '{elemento}'")
    
    elif opcion == '4':
        if cola.esta_vacia():
            print("La cola está vacía.")
        else:
            print("La cola no está vacía.")
    
    elif opcion == '5':
        print(f"El tamaño de la cola es: {cola.tamano()}")
    
    elif opcion == '6':
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
