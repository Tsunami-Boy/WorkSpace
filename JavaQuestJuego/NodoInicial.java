package JavaQuestJuego;

import javax.swing.JOptionPane;

public class NodoInicial extends Nodo{
    public NodoInicial(Integer id){
        this.id = id;
    }
    /*
    * interactuar(): Estructura en la que se procede en este tipo de nodo.
    *
    * Sin parametros.
    *
    * return: no retorna.
    */
    @Override
    public void interactuar(Jugador jugador){
        JOptionPane.showMessageDialog(null, "Hola michi aventurero, necesitamos de tu ayuda!! Nuestro pueblo ha sido esclavizado por los bandidos caninos y...lamentablemente \npor Don Cucho, El Traidor. El futuro de este michi pueblo queda en tus manos. Deberás avanzar en un arduo mapa hasta lograr derrotar al jefe.\nBuena suerte.");
    }
}
