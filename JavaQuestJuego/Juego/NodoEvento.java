package JavaQuestJuego.Juego;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;

public class NodoEvento extends Nodo{
    private String descripcion;
    private String alternativa1;
    private String alternativa2;
    private Item resultado1;
    private Item resultado2;

    public NodoEvento(Integer num, Integer id){
        this.id = id;
        this.descripcion = lista_descripcion(num);
        this.alternativa1 = lista_alternativa1(num);
        this.alternativa2 = lista_alternativa2(num);
        this.resultado1 = lista_resultado1(num);
        this.resultado2 = lista_resultado2(num);
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
        String salida = descripcion + "\nEn este momento debes elegir una de estas dos alternativas introduciendo su numero: \n\n" + alternativa1 + "\n" + alternativa2;
        String decision = JOptionPane.showInputDialog(null, salida);
        if(decision.equals("1")){
            JOptionPane.showMessageDialog(null, "Acabas de obtener: "+resultado1.getNombre()+"\nVida recuperada: "+resultado1.getRecuperar_hp()+"\nVida total aumentada: "+resultado1.getAumentar_hp_total()+"\nDaño aumentado: "+resultado1.getAumentar_danio()+"\nDefensa aumentada: "+resultado1.getAumentar_defensa());
            resultado1.aplicar(jugador);
            jugador.setItem(resultado1);
        }
        else{
            JOptionPane.showMessageDialog(null, "Acabas de obtener: "+resultado2.getNombre()+"\nVida recuperada: "+resultado2.getRecuperar_hp()+"\nVida total aumentada: "+resultado2.getAumentar_hp_total()+"\nDaño aumentado: "+resultado2.getAumentar_danio()+"\nDefensa aumentada: "+resultado2.getAumentar_defensa());
            resultado2.aplicar(jugador);
            jugador.setItem(resultado2);
        }
    }
    /*
    * lista_descripcion(): se crean las descripciones en orden y se guardan en una lista.
    *
    * num: numero el cual se usará para la posicion en la lista.
    *
    * return: retorna una descripcion de la lista.
    */
    public String lista_descripcion(Integer num){
        List<String> lista;
        lista = new ArrayList<>();
        
        String event1="Acabas de llegar a un pueblo desierto. Por lo visto, los perros han arrasado con todo. Decides revisar todas las casas y en la penultima casa puedes ver como dos perros tienen de esclavo a un pequeño gatito.\n";
        lista.add(event1);
        String event2="Acabas de encontrar un gato misterioso con un manto. El gato con un maullido profundo te comenta que todo esto es una simulación y te da a ofrecer dos tipos de comida distinta. \n";
        lista.add(event2);
        String event3="Acabas de pasar de infiltrado por un pueblo poblado de perros con la mision de adquirir información del jefe final. Al pasar por un callejón te topas con un perro ladrón. \n";
        lista.add(event3);
        String event4="Acabas de llegar a un lago con abundantes peces, decides armar tu caña de pescar ya que tienes mucha hambre. Con el pasar del tiempo llenas tu cubetita de peces, pero de la nada salta un merluzo gigante desde el agua y se impone frente a ti. \n";
        lista.add(event4);

        return lista.get(num);

    }
    /*
    * lista_alternativa1(): se crean las alternativas 1 en orden y se guardan en una lista.
    *
    * num: numero el cual se usará para la posicion en la lista.
    *
    * return: retorna una alternativa 1 de la lista.
    */
    public String lista_alternativa1(Integer num){
        List<String> lista;
        lista = new ArrayList<>();
        
        String alt1="(1)  Ayudar al pequeño gatito, pero puedes tener daños colaterales";
        lista.add(alt1);
        String alt2="(1)  Pelet Azul";
        lista.add(alt2);
        String alt3="(1)  Atacar al ladrón, pero puedes tener daños colaterales";
        lista.add(alt3);
        String alt4="(1)  Intentar comprender que quiere el merluzo de forma pacífica";
        lista.add(alt4);

        return lista.get(num);
    }
    /*
    * lista_alternativa2(): se crean las alternativas 2 en orden y se guardan en una lista.
    *
    * num: numero el cual se usará para la posicion en la lista.
    *
    * return: retorna una alternativa 2 de la lista.
    */
    public String lista_alternativa2(Integer num){
        List<String> lista;
        lista = new ArrayList<>();

        String alt1= "(2)  Revisar la siguiente casa e irse del pueblo";
        lista.add(alt1);
        String alt2= "(2)  Pelet Rojo";
        lista.add(alt2);
        String alt3= "(2)  Negociar con el ladrón para adquirir información (Sospechoso)";
        lista.add(alt3);
        String alt4= "(2)  Atacar al merluzo ya que se ve apetitoso";
        lista.add(alt4);

        return lista.get(num);
    }
    /*
    * lista_resultado1(): se crean los resultados 1 en orden y se guardan en una lista.
    *
    * num: numero el cual se usará para la posicion en la lista.
    *
    * return: retorna un resultado 1 de la lista.
    */
    public Item lista_resultado1(Integer num){
        List<Item> lista;
        lista = new ArrayList<>();

        Item item1 = new Item("Bolita de lana",0,-2,2,1,1);
        lista.add(item1);
        Item item2 = new Item("Pelet Azul (Empiezas a sentir mas energía)",0,1,1,0,1);
        lista.add(item2);
        Item item3 = new Item("Daga O Wazamono",0,-1,0,4,1);
        lista.add(item3);
        Item item4 = new Item("Papel diplomático de paz entre peces y gatos",0,0,3,0,2);
        lista.add(item4);

        return lista.get(num);
    }
    /*
    * lista_resultado2(): se crean los resultados 2 en orden y se guardan en una lista.
    *
    * num: numero el cual se usará para la posicion en la lista.
    *
    * return: retorna un resultado 2 de la lista.
    */
    public Item lista_resultado2(Integer num){
        List<Item> lista;
        lista = new ArrayList<>();

        Item item1 = new Item("Lentes rotos",0,1,1,0,1);
        lista.add(item1);
        Item item2 = new Item("Pelet Rojo (Entras en un sueño y en este ves el futuro)",0,1,0,2,0);
        lista.add(item2);
        Item item3 = new Item("Pergamino de defensa (Falso)",0,0,0,0,1);
        lista.add(item3);
        Item item4 = new Item("Merluzo gigante frito con puré de papas",0,3,4,0,0);
        lista.add(item4);
    
        return lista.get(num);
    }
}
