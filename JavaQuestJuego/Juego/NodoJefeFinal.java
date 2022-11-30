package JavaQuestJuego.Juego;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;


public class NodoJefeFinal extends Nodo{
    private Personaje jefe;
    private List<Personaje> lista;

    public NodoJefeFinal(Integer num, Integer id){
        this.id = id;
        lista = new ArrayList<>();
        crear_jefes();
        jefe = lista.get(num);
    }
    /*
    * interactuar(): estructura en la que se procede en este nodo.
    *
    * jugador: tipo Jugador, el cual se le harán los cambios correspondientes del item.
    *
    * return: no retorna.
    */
    @Override
    public void interactuar(Jugador jugador){
        JOptionPane.showMessageDialog(null, "Luego de un arduo trabajo, logras llegar hasta el jefe encargado de la mafia perruna, el gran y espeluznante "+jefe.getNombre()+".\nTras descubrir que desea exterminar a todos los gatos esta noche, decides hacer tu ultimo plan... Atacarlo.\nPrepárate para el combate.");
        JOptionPane.showMessageDialog(null, "Vida actual tuya: "+jugador.getHp_actual()+"/"+jugador.getHp_total() + "\n" + "Vida actual tuya: "+jefe.getHp_actual()+"/"+jefe.getHp_total());

        while((jefe.getHp_actual()>0)&&(jugador.getHp_actual()>0)){
            String decision = JOptionPane.showInputDialog("Ingresa ATACAR si deseas realizar tu ataque. Ingresa ESTADISTICAS si deseas ver tus estadisticas");
            if(decision.equals("ATACAR") != false){
                jefe.setHp_actual(jefe.getHp_actual()-(jugador.getDanio()-jefe.getDefensa()));
                jugador.setHp_actual(jugador.getHp_actual()-(jefe.getDanio()-jugador.getDefensa()));
                JOptionPane.showMessageDialog(null, "Has atacado al enemigo | Le has hecho de daño: "+(jugador.getDanio()-jefe.getDefensa()) +"\n"+"El enemigo te ha atacado | Te ha hecho de daño: "+ (jefe.getDanio()-jugador.getDefensa())+"\n\n"+"Vida actual del enemigo: "+jefe.getHp_actual()+"/"+jefe.getHp_total());
                if(jugador.getHp_actual()<=0){
                    JOptionPane.showMessageDialog(null, "Has sido derrotado por el temible "+jefe.getNombre());
                    JOptionPane.showMessageDialog(null, "Game Over");
                    System.exit(0);
                }
                else if(jefe.getHp_actual()<=0){
                    JOptionPane.showMessageDialog(null, "FELICIDADES!! Has logrado aniquilar al jefe "+jefe.getNombre()+". Los perros subordinaos de este sienten temor ante tu poder.\nLos gatitos que han sido esclavizados logran huir y se acercan al lugar del combate.\n");
                    JOptionPane.showMessageDialog(null, "A lo lejos empiezas a escuchar los cuernos de la victoria y el retumbar de los tambores, el ambiente es de alegría y agradecimiento.\nTodos los gatitos te agradecen por ser el héroe y empieza una celebración de 7 días.\n Fin");
                    System.exit(0);
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
    * crear_jefes(): se crea una lista de jefes de tipo personaje.
    *
    * Sin parametros.
    *
    * return: no retorna.
    */
    public void crear_jefes(){
        Personaje en1 = new Personaje("Dark Dog", 0,55, 55, 6, 4);
        Personaje en2 = new Personaje("Kaidog", 0, 45, 45, 4, 6);
        lista.add(en1);
        lista.add(en2);
    }
}
