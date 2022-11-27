package JavaQuestJuego;
import java.util.SortedSet;
import javax.swing.JOptionPane;

public class javaQuest {
    public static void main(String[] args){
        String nom = JOptionPane.showInputDialog("Bienvenido honorable gaturr@, ingresa tu michi_nombre y empieza tu aventura");
        Integer nodos_totales = Integer.parseInt(JOptionPane.showInputDialog(nom+" a continuación deberás ingresar la profundidad que deseas generar en el mapa"));
        //Se inicializa
        Jugador jugador = new Jugador(nom,500,20,20,5,1);
        SortedSet<Edge> edges = GraphGenerator.Generar(nodos_totales);
        NodoInicial inicio = new NodoInicial(0);
        NodoJefeFinal jefe = new NodoJefeFinal(0,0);
        Mapa mapa = new Mapa(nodos_totales,inicio,edges);
        //Inicia el juego
        inicio.interactuar(jugador);
        while(jugador.getHp_actual()>0){
            String decision = JOptionPane.showInputDialog("\n"+jugador.getNombre()+" deberás elegir alguna de estas instrucciones solamente ingresando su numero indicado:\n\n(1) Ver mapa\n(2) Ver estadísticas\n(3) Ver items\n(4) Avanzar");
            if(decision.equals("1") != false){
                mapa.verMapa(edges);
            }
            else if(decision.equals("2") != false){
                jugador.verEstado();
            }
            else if(decision.equals("3") != false){
                jugador.verItems();
            }
            else if(decision.equals("4") != false){
                mapa.avanzar(edges,jugador);
            }
            else{System.out.println("Opcion ingresada no válida, intentalo nuevamente");}
        }
        if(jugador.getHp_actual()<1){
            System.out.println("Game Over");
        }
        else{jefe.interactuar(jugador);}
        
    }
}