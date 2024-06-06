public class PilaEnlazada<T> implements Pila<T> {
    private Nodo<T> tope;
    private int tamano;

    public PilaEnlazada() {
        this.tope = null;
        this.tamano = 0;
    }

    @Override
    public void apilar(T elemento) {
        Nodo<T> nuevoNodo = new Nodo<>(elemento);
        nuevoNodo.siguiente = tope;
        tope = nuevoNodo;
        tamano++;
    }

    @Override
    public T desapilar() {
        if (estaVacia()) {
            throw new RuntimeException("La pila está vacía");
        }
        T valor = tope.valor;
        tope = tope.siguiente;
        tamano--;
        return valor;
    }

    @Override
    public T cima() {
        if (estaVacia()) {
            throw new RuntimeException("La pila está vacía");
        }
        return tope.valor;
    }

    @Override
    public boolean estaVacia() {
        return tope == null;
    }

    @Override
    public int tamano() {
        return tamano;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Nodo<T> actual = tope;
        while (actual != null) {
            sb.append(actual.valor).append(" => ");
            actual = actual.siguiente;
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        PilaEnlazada<Integer> pila = new PilaEnlazada<>();

        // Apilar  elementos
        pila.apilar(10);
        pila.apilar(20);
        pila.apilar(30);
        pila.apilar(40);
        pila.apilar(50);

        System.out.println("Pila después de apilar 10, 20, 30, 40, 50:");
        System.out.println(pila);  

        // Ver elemento en la cima
        System.out.println("Elemento en la cima:");
        System.out.println(pila.cima());  

        // Desapilar elemento
        System.out.println("Elemento desapilado:");
        System.out.println(pila.desapilar());  

        System.out.println("Pila después de desapilar un elemento:");
        System.out.println(pila);  

        // Verificar tamaño de la pila
        System.out.println("Tamaño de la pila:");
        System.out.println(pila.tamano());  
    }
}
