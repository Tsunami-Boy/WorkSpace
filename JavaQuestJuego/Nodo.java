package JavaQuestJuego;

import java.util.List;

public abstract class Nodo {
    Integer id;
    private List<Nodo> siguientesnodos;
    
    public abstract void interactuar(Jugador juagdor);
    
    public void agregarNodo(Nodo sig){
        List<Nodo> NodoS = getSiguientesnodos();
        NodoS.add(sig);
        setSiguientesnodos(NodoS);

    };

    //Setter y Getter
    public Integer getId(){
        return id;
    }
    public void setId(Integer id){
        this.id = id;
    }
    public List<Nodo> getSiguientesnodos(){
        return siguientesnodos;
    }
    public void setSiguientesnodos(List<Nodo> siguientesnodos){
        this.siguientesnodos = siguientesnodos;
    }
}
