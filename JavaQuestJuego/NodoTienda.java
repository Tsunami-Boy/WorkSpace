package JavaQuestJuego;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

import javax.swing.JOptionPane;


public class NodoTienda extends Nodo{
    private List<Item> inventario;

    public NodoTienda(Integer id){
        this.id = id;
        inventario = new ArrayList<>();
        crear_inventario();
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
        String salida = "Woow, impresionante!! Has llegado a la Tienda\n"+jugador.getNombre()+" podrás comprar algunos de los siguientes items como gustes";
        Random num_items = new Random();
        Scanner entrada4 = new Scanner(System.in);
        Scanner entrada5 = new Scanner(System.in);
        int numero = (num_items.nextInt(8-5+1)+5);
        int arreglo[] = new int[numero];
        arreglo[0] = (int) (Math.random() *8);

        for(int i = 1; i < numero; i++){
            arreglo[i]= (int) (Math.random() *8);
            for (int j = 0; j<i; j++){
                if(arreglo[i] == arreglo[j]){
                    i--;
                }
            }
        }
        for(int i = 0; i < numero-1; i++){
            for(int j = 0; j < numero-1; j++){
                if(arreglo[j] > arreglo [j+1]){
                    int aux = arreglo[j];
                    arreglo[j] = arreglo[j+1];
                    arreglo[j+1] = aux;
                }
            }
        }
        boolean flag = true;
        salida = salida + "\nEl dinero actual que tiene es de: $"+jugador.getDinero() + "\nLos items dispoibles son los siguientes:\n";
            for(int i=0;i<numero;i++){
                salida = salida + "(" + arreglo[i]+")  " + inventario.get(arreglo[i]).getNombre() + "  $" + inventario.get(arreglo[i]).getPrecio()+"\n";
            }
            salida = salida + "Si no desea comprar ingrese NO COMPRAR";
        while(flag == true){
            String decision = JOptionPane.showInputDialog(salida);
            boolean flag2 = false;
            if(decision.equals("NO COMPRAR") == false){
                for(int i=0;i<numero;i++){
                    if(arreglo[i] == Integer.parseInt(decision)){
                        flag2 = true;
                    }
                }
            }
            if(decision.equals("NO COMPRAR") == false && flag == true && flag2 == true){
                if(jugador.getDinero() >= inventario.get(Integer.parseInt(decision)).getPrecio()){
                    String confirmar = JOptionPane.showInputDialog("Ingresa CONFIRMAR si estás seguro de tu compra");
                    if(confirmar.equals("CONFIRMAR")){
                        comprar(Integer.parseInt(decision), jugador);
                        flag = false;
                    String seguir = JOptionPane.showInputDialog("¿Desea seguir comprando? Ingrese SI o NO");
                    if(seguir.equals("SI") != false){
                        flag = true;
                    }
                    else{
                        flag = false;
                    }
                    }
                    else{JOptionPane.showMessageDialog(null, "No ha confirmado la compra, volverá a la tienda");}
                }
                else{JOptionPane.showMessageDialog(null, "Dinero insuficiente"); flag = true;}
            }
            else if (decision.equals("NO COMPRAR") != false){
                flag = false;
            }
            else{
                JOptionPane.showMessageDialog(null, "Decision ingresada no valida, vuelva a intentarlo");
                flag = true;
            }
            entrada4.close();
            entrada5.close();
        }
    }
    /*
    * crear_inventario(): se crea el inventario de la tienda, agregando cada item de tipo Item a una lista.
    *
    * Sin parametros.
    *
    * return: no retorna.
    */
    public void crear_inventario(){
        //Item 1
        Item item1 = new Item("Garras de hierro",350,0,0,3,1);
        Item item2 = new Item("Collar protector",450,2,3,0,2);
        Item item3 = new Item("Lentes facheros",350,0,1,1,1);
        Item item4 = new Item("Chaleco anti-mordidas",800,3,7,0,4);
        Item item5 = new Item("Atún",250,5,0,0,0);
        Item item6 = new Item("Sombrero de paja facherito (Otorga facha)",1000,4,4,4,4);
        Item item7 = new Item("Vacuna anti-rabia",600,2,3,1,3);
        Item item8 = new Item("Vacuna de la rabia",600,2,3,3,1);
        inventario.add(item1);
        inventario.add(item2);
        inventario.add(item3);
        inventario.add(item4);
        inventario.add(item5);
        inventario.add(item6);
        inventario.add(item7);
        inventario.add(item8);
    }
    /*
    * comprar(): aplica en el personaje el item y lo guarda en la lista de items que se aplicó el personaje.
    *
    * item: item de tipo Item que se desea aplicar y guardar en el jugador.
    * jugador: tipo Jugador, el cual se le harán los cambios correspondientes del item.
    *
    * return: no retorna.
    */
    public void comprar(Integer item, Jugador jugador){
        inventario.get(item).aplicar(jugador);
        jugador.setItem(inventario.get(item));
    }

}
