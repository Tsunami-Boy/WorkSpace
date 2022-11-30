package JavaQuestJuego.Juego;

public class Item {
    private String nombre;
    private Integer precio;
    private Integer recuperar_hp;
    private Integer aumentar_hp_total;
    private Integer aumentar_danio;
    private Integer aumentar_defensa;
    
    public Item(String nombre, Integer precio, Integer recuperar_hp, Integer aumentar_hp_total, Integer aumentar_danio, Integer aumentar_defensa){
        this.nombre = nombre;
        this.precio = precio;
        this.recuperar_hp = recuperar_hp;
        this.aumentar_hp_total = aumentar_hp_total;
        this.aumentar_danio = aumentar_danio;
        this.aumentar_defensa = aumentar_defensa;
    }
    /*
    * aplicar(): aplica los items comprados en el jugador
    *
    * jugador: tipo Jugador, el cual se le harán los cambios correspondientes del item.
    *
    * return: no retorna.
    */
    public void aplicar(Jugador jugador){
        Integer dinero = jugador.getDinero();
        Integer hp = jugador.getHp_actual();
        Integer hp_total = jugador.getHp_total();
        Integer danio = jugador.getDanio();
        Integer defensa = jugador.getDefensa();

        dinero = dinero - getPrecio();
        hp_total = hp_total + getAumentar_hp_total();
        hp = hp + getRecuperar_hp();
        if (hp > hp_total){
            hp = hp_total;
        }
        danio = danio + getAumentar_danio();
        defensa = defensa + getAumentar_defensa();

        jugador.setDinero(dinero);
        jugador.setHp_total(hp_total);
        jugador.setHp_actual(hp);
        jugador.setDanio(danio);
        jugador.setDefensa(defensa);
    }
    //Getter 
    public String getNombre(){
        return nombre;
    }
    public Integer getPrecio(){
        return precio;
    }
    public Integer getRecuperar_hp(){
        return recuperar_hp;
    }
    public Integer getAumentar_hp_total(){
        return aumentar_hp_total;
    }
    public Integer getAumentar_danio(){
        return aumentar_danio;
    }
    public Integer getAumentar_defensa(){
        return aumentar_defensa;
    }

}
