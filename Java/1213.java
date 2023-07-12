import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int n = sc.nextInt();
            int i = 1, aux = 1;
            while(i % n > 0){
                i = (i*10+1) % n;
                aux++;
            }
            System.out.println(aux);
        }
    }
}
