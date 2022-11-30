package JavaQuestJuego.Juego;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;

public class NodoCombate extends Nodo {
    private Personaje enemigo;
    private List<Personaje> lista;

    public NodoCombate(Integer num, Integer id){
        this.id=id;
        lista = new ArrayList<>();
        crear_enemigos();
        this.enemigo = lista.get(num);
    }
    /*
    * interactuar(): Estructura en la que se procede en este tipo de nodo.
    *
    * jugador: tipo Jugador, el cual se le harán los cambios correspondientes del item.
    *
    * return: no retorna.
    */
    @Override
    public void interactuar(Jugador jugador){
        JOptionPane.showMessageDialog(null,"En este momento has entrado a una sala de combate, debes prepararte ya que te enfrentarás a: "+enemigo.getNombre()+"\n"+"Vida actual tuya: "+jugador.getHp_actual()+"/"+jugador.getHp_total()+"\n"+"Vida actual del enemigo: "+enemigo.getHp_actual()+"/"+enemigo.getHp_total());
        while((enemigo.getHp_actual()>0)&&(jugador.getHp_actual()>0)){
            String decision = JOptionPane.showInputDialog("Ingresa ATACAR si deseas realizar tu ataque. Ingresa ESTADISTICAS si deseas ver tus estadisticas");
            if(decision.equals("ATACAR") != false){
                if(0<(jugador.getDanio()-enemigo.getDefensa())){
                    enemigo.setHp_actual(enemigo.getHp_actual()-(jugador.getDanio()-enemigo.getDefensa()));
                }
                if(0<(enemigo.getDanio()-jugador.getDefensa())){
                    jugador.setHp_actual(jugador.getHp_actual()-(enemigo.getDanio()-jugador.getDefensa()));
                }
                JOptionPane.showMessageDialog(null, "Has atacado al enemigo | Le has hecho de daño: "+(jugador.getDanio()-enemigo.getDefensa())+"\n"+"El enemigo te ha atacado | Te ha hecho de daño: "+ (enemigo.getDanio()-jugador.getDefensa())+"\n\n"+"Vida actual del enemigo: "+enemigo.getHp_actual()+"/"+enemigo.getHp_total());
                if(jugador.getHp_actual()<=0){
                    JOptionPane.showMessageDialog(null, "Has sido derrotado por "+enemigo.getNombre());
                    JOptionPane.showMessageDialog(null, "Game Over");
                    System.exit(0);
                }
                else if(enemigo.getHp_actual()<=0){
                    JOptionPane.showMessageDialog(null, "FELICIDADES!! Has derrotado a "+enemigo.getNombre()+". Has conseguido una recompensa de: $"+enemigo.getDinero());
                    jugador.setDinero(jugador.getDinero()+enemigo.getDinero());
                }
            }
            else if(decision.equals("ESTADISTICAS") != false){
                jugador.verEstado();
            }
            else{
                JOptionPane.showMessageDialog(null, "Eleccion ingresada incorrecta, vuelva a ingresarla");
            }
        }
    }
    /*
    * crear_enemigos(): crea enemigos de tipo personaje, y luego se guardan en la lista.
    *
    * Sin parametros
    *
    * return: no retorna.
    */
    public void crear_enemigos(){
        Personaje en1 = new Personaje("El Traidor Cucho", 200, 20, 20, 3, 2);
        Personaje en2 = new Personaje("Perro Ivan", 150, 15, 15, 2, 2);
        Personaje en3 = new Personaje("Sansón Pata Grande", 250, 23, 23, 2, 3);
        Personaje en4 = new Personaje("Lilo Hocico Venenoso", 100, 10, 10, 2, 2);
        Personaje en5 = new Personaje("Rudy Barbanegra", 150, 13, 13, 3, 1);
        Personaje en6 = new Personaje("Titina", 100, 15, 15, 1, 1);
        Personaje en7 = new Personaje("Laica (Después del Edo Tensei)", 300, 23, 23, 3, 4);
        Personaje en8 = new Personaje("La Pulga Messi", 50, 8, 8, 1, 1);
        Personaje en9 = new Personaje("God Scooby", 100, 15, 15, 3, 2);
        Personaje en10 = new Personaje("Cancerbero", 400, 24, 24, 5, 4);
        Personaje en11 = new Personaje("Thor El Carnicero", 350, 35, 35, 3, 1);
        Personaje en12 = new Personaje("Perro con Rabia", 100, 10, 10, 4, 0);

        lista.add(en1);
        lista.add(en2);
        lista.add(en3);
        lista.add(en4);
        lista.add(en5);
        lista.add(en6);
        lista.add(en7);
        lista.add(en8);
        lista.add(en9);
        lista.add(en10);
        lista.add(en11);
        lista.add(en12);
    }
}
