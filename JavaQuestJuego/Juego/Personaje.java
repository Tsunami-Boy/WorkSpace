package JavaQuestJuego.Juego;

public class Personaje {
    //Atributos
    private String nombre;
    private Integer dinero;
    private  Integer hp_actual;
    private Integer hp_total;
    private Integer danio;
    private Integer defensa;

    //Metodos
    public Personaje(String nombre, Integer dinero, Integer hp_actual, Integer hp_total, Integer danio, Integer defensa){
        this.nombre = nombre;
        this.dinero = dinero;
        this.hp_actual = hp_actual;
        this.hp_total = hp_total;
        this.danio = danio;
        this.defensa = defensa;
    }
    //Getter y Setter
    public String getNombre(){
        return nombre;
    }
    public void setDinero(int dinero){
        this.dinero = dinero;
    }
    public int getDinero(){
        return dinero;
    }
    public void setHp_actual(int hp_actual){
        this.hp_actual = hp_actual;
    }
    public int getHp_actual(){
        return hp_actual;
    }
    public void setHp_total(int hp_total){
        this.hp_total = hp_total;
    }
    public int getHp_total(){
        return hp_total;
    }
    public void setDanio(int danio){
        this.danio = danio;
    }
    public int getDanio(){
        return danio;
    }
    public void setDefensa(int defensa){
        this.defensa = defensa;
    }
    public int getDefensa(){
        return defensa;
    }
}
