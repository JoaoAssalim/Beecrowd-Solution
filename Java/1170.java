import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            float sup = sc.nextFloat();
            int dias = 0, parar = 1;
            while(parar == 1){
                sup = sup/2;
                dias++;
                if(sup <= 1)
                    parar = 0;
            }
            System.out.println(dias + " dias");
        }
    }
}
