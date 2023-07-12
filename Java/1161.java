import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int a = sc.nextInt(), b = sc.nextInt();
            long totalA = 1, totalB = 1, total = 0;

            for(int i = 1; i <= a; i++){
                totalA = totalA * i;
            }

            for(int i = 1; i <= b; i++){
                totalB = totalB * i;
            }

            total = totalA + totalB;
            System.out.println(total);

        }
    }
}
