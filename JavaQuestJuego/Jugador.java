package JavaQuestJuego;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;

public class Jugador extends Personaje{
    private List<Item> items_aplicados;
    public Jugador(String nombre, Integer dinero, Integer hp_actual, Integer hp_total, Integer danio, Integer defensa){
        super(nombre,dinero,hp_actual,hp_total,danio,defensa);
        items_aplicados = new ArrayList<>();
    }
    /*
    * verEstado(): Muestra en pantalla las caracteristicas actuales del jugador.
    *
    * Sin parametros
    *
    * return: no retorna.
    */
    public void verEstado(){
        JOptionPane.showMessageDialog(null, "A continuacion se mostrará su información \nNombre: "+getNombre()+"\nDinero: "+getDinero()+"\nVida actual: "+getHp_actual()+"\nVida total: "+getHp_total()+"\nDaño: "+getDanio()+"\nDefensa: "+getDefensa());
    }
    /*
    * verItems(): Hace un recorrido por la lista de items que fueron equipados en el jugador.
    *
    * Sin parametros
    *
    * return: no retorna.
    */
    public void verItems(){
        String salida = "Tus items son los siguientes:\n";
        int largo = items_aplicados.size();
        int i = 0;
        if(largo != 0){
            while (i<largo){
                salida = salida + items_aplicados.get(i).getNombre() + "\n";
                i++;
            }
            JOptionPane.showMessageDialog(null, salida);
        }
        else{JOptionPane.showMessageDialog(null, "Aún no tienes items en tu inventario");}
    }
    //Getter y Setter Items
    public void setItem(Item item){
        items_aplicados.add(item);
    }
}
