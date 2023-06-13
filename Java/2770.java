import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextInt()) {
            String line = scanner.nextLine();
            List<Integer> lista = new ArrayList<>();
            String[] linex = line.split(" ");
            for (String numero : linex) {
                int valor = Integer.parseInt(numero);
                lista.add(valor);
            }

            for(int i = 0; i < lista.get(2); i++){
                String xy = scanner.nextLine();
                List<Integer> listax = new ArrayList<>();
                String[] linexy = xy.split(" ");
                for (String numero : linexy) {
                    int valor = Integer.parseInt(numero);
                    listax.add(valor);
                }

                if(listax.get(0) <= lista.get(0) && listax.get(1) <= lista.get(1) || listax.get(0) <= lista.get(1) && listax.get(1) <= lista.get(0)){
                    System.out.println("Sim");
                }else{
                    System.out.println("Nao");
                }




            }
        }
    }   
}