import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int h = sc.nextInt(), m = sc.nextInt();
            int hora = h / 30, min = m / 6;
            if(hora < 10){
                System.out.printf("0" + hora + ":");
            }else{
                System.out.printf(hora + ":");
            }
            if(min < 10){
                System.out.println("0" + min);
            }else{
                System.out.println(min);
            }
        }

    }
}
