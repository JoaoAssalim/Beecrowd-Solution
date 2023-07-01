import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] leds = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
        int x = sc.nextInt();
        sc.nextLine();
        for(int i = 0; i < x; i++){
            int total = 0;
            String ent = sc.nextLine();
            for(int j = 0; j < ent.length(); j++){
                int n = Integer.parseInt(ent.substring(j, j+1));
                total += leds[n];
            }
            System.out.println(total + " leds");
        }
        
    }
}
