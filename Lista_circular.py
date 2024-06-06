
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head
        if head is not None:
            self.head.next = head

    def is_empty(self):
        return self.head is None

    def size(self):
        if self.is_empty():
            return 0
        current = self.head
        count = 1
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def search(self, position, prev=False):
        # Busca el elemento en la posición dada. Si position es negativo busca el último elemento
        # El argumento prev sirve para devolver en una lista tanto el nodo buscado como el anterior.
        if position == 0:
            if prev is False:
                return self.head
            else:
                return [self.search(-1), self.head]
        elif position < 0:
            current = self.head
            while current.next != self.head:
                previous = current
                current = current.next
            return current if prev is False else [previous, current]
        else:
            k = 1
            current = self.head
            while k < position and current.next != self.head:
                k += 1
                previous = current
                current = current.next
            return current if prev is False else [previous, current]

    def insert(self, node, position):
        # Inserta el nodo después de la posición indicada. Si se indica una posición negativa, o mayor que
        # el tamaño de la lista, se inserta al final
        if self.is_empty():
            self.head = node
            self.head.next = self.head
            return
        if position == 0:
            last_element = self.search(-1)
            last_element.next = node
            node.next = self.head
            self.head = node
        elif position < 0:
            last_element = self.search(-1)
            last_element.next = node
            node.next = self.head
        else:
            element = self.search(position)
            node.next = element.next
            element.next = node

    def delete(self, position):
        # Para posiciones con valor negativo, borra el último nodo
        if self.is_empty():
            return
        if position == 0:
            last_element = self.search(-1)
            if self.head.next == self.head:  # Only one element
                self.head = None
            else:
                self.head = self.head.next
                last_element.next = self.head
        elif position < 0:
            previous = self.search(-1, True)[0]
            if previous.next == self.head:  # Only one element
                self.head = None
            else:
                previous.next = previous.next.next
        else:
            previous = self.search(position - 1, True)[0]
            previous.next = previous.next.next

def print_list(c_list):
    if c_list.is_empty():
        print("\nLa lista está vacía.")
        return
    print(c_list.head.data)
    current = c_list.head.next
    while current is not c_list.head:
        print(current.data)
        current = current.next

c_list = CircularLinkedList()
for i in range(1, 2):
    c_list.insert(Node(i), -1)

print("Lista inicial:")
print_list(c_list)

while True:
    command = input("Elija uno: \n1.Insertar \n2.Eliminar \n3.Mostrar \n4.Tamaño de Lista\n5.Salir ")
    
    if command == "1":
        data = int(input("\nIngrese el valor del nodo: "))
        position = int(input("\nIngrese la posición: "))
        c_list.insert(Node(data), position)
    elif command == "2":
        position = int(input("Ingrese la posición: "))
        c_list.delete(position)
    elif command == "3":
        print_list(c_list)
    elif command == "4":
        print(f"Tamaño de la lista: {c_list.size()}")
    elif command == "5":
        break
    else:
        print("Comando no reconocido. Intente de nuevo.")
