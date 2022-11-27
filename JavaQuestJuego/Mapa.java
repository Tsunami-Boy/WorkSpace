package JavaQuestJuego;
import java.util.ArrayList;
import java.util.List;
import java.util.SortedSet;

import javax.swing.JOptionPane;

public class Mapa {
    private Integer profundidad;
    private NodoInicial nodoinicial;
    private Nodo nodo_actual;
    private List<Nodo> lista_nodos;

    public Mapa(Integer profundidad, NodoInicial nodoinicial,SortedSet<Edge> edges){
        this.profundidad = profundidad;
        this.nodoinicial = nodoinicial;
        this.nodo_actual = this.nodoinicial;
        lista_nodos = new ArrayList<>();
        crear_nodos(edges);
    }
    /*
    * verMapa(): Muestra la direccion de cada nodo en el mapa
    *
    * edges: arcos generados a partir de nos nodos en el mapa.
    *
    * return: no retorna.
    */
    public void verMapa(SortedSet<Edge> edges){
        String salida = "El mapa tiene una profundidad de: "+profundidad+"\n"+"Actualmente estás en el nodo: "+nodo_actual.getId()+"\n\n";
        for (Edge e : edges) {
            salida= salida + "(" + e.x + ") -> (" + e.y + ")\n";
        } 
        JOptionPane.showMessageDialog(null, salida);
    }
    /*
    * avanzar(): avanza en el camino que escoja el jugador, siempre y cuando este tenga conexión con el nodo actual.
    *
    * edges: arcos generados a partir de nodos en el mapa.
    * jugador: de tipo Jugador, guarda las caracteristicas del personaje.
    *
    * return: no retorna.
    */
    public void avanzar(SortedSet<Edge> edges, Jugador jugador){
        String salida = "Debes elegir uno de los siguientes caminos disponinles (solo ingresa el numero): \n";
        Integer id = nodo_actual.getId();
        for (Edge e: edges) {
            if(id == e.x){
                salida = salida + "camino " + e.y + "\n";
            }
        }
        boolean flag2 = true;
        while(flag2 == true){
            String decision = JOptionPane.showInputDialog(salida);
            boolean isNumeric = (decision != null && decision.matches("[0-9]+"));
            if(isNumeric == true){
                boolean flag = false;
                for(Edge e: edges){
                    if(id == e.x && Integer.parseInt(decision) == e.y){
                        flag = true;
                    }
                }
                if(flag == true){
                    for(int i=0;i<lista_nodos.size();i++){
                        if(lista_nodos.get(i).getId() == Integer.parseInt(decision)){
                            lista_nodos.get(i).interactuar(jugador);
                            this.nodo_actual = lista_nodos.get(i);
                            flag2 = false;
                        }
                    }
                }
                else{JOptionPane.showMessageDialog(null, "Camino ingresado no válido");flag2=true;}
            }
            else{JOptionPane.showMessageDialog(null, "Dato ingresado no valido");flag2=true;}
        }
    }
    /*
    * crear_nodos(): crea el tipo de nodo a partir del porcentaje señalado en las instrucciones. Crea un nodo por cada arista del mapa.
    *
    * edges: arcos generados a partir de nodos en el mapa.
    *
    * return: no retorna.
    */
    public void crear_nodos(SortedSet<Edge> edges){
        List<Integer> cant_aristas;
        cant_aristas = new ArrayList<>();
        for (Edge e : edges) {
            int largo = cant_aristas.size();
            boolean flag = true;
            for(int i=0;i<largo;i++){
                if(cant_aristas.get(i) == e.x){
                    flag = false;
                }
            }
            if(flag == true){
                cant_aristas.add(e.x);
            }
            flag = true;
            for(int i=0; i<largo; i++){
                if(cant_aristas.get(i) == e.y){
                    flag = false;
                }
            }
            if(flag == true){
                cant_aristas.add(e.y);
            }
        }
        for(int i=1; i<cant_aristas.size()-1;i++){
            double Random = Math.random();
            if(Random <=0.6){
                Integer rand1 = (int) (Math.random()*11);
                NodoCombate combat = new NodoCombate(rand1, i);
                lista_nodos.add(combat);
            }
            else if(Random > 0.6 && Random <=0.9){
                Integer rand2 = (int) (Math.random()*3);
                NodoEvento event = new NodoEvento(rand2, i);
                lista_nodos.add(event);
            }
            else if(Random >0.9 && Random <= 1){
                NodoTienda tiend = new NodoTienda(i);
                lista_nodos.add(tiend);
            }
        }
        Integer rand3 = (int) (Math.random()*1);
        NodoJefeFinal jefe = new NodoJefeFinal(rand3, (cant_aristas.size()-1));
        lista_nodos.add(jefe);
    }
}
