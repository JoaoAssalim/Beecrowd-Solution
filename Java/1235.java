import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.nextLine();
        for(int i = 0; i < x; i++){
            String pal = sc.nextLine();
            int len_pal = pal.length()/2;

            String p1 = pal.substring(0, len_pal);
            String p2 = pal.substring(len_pal, pal.length());
            String nova = "";

            for(int j = p1.length(); j > 0; j--){
                nova += p1.substring(j-1, j);
            }
            for(int j = p2.length(); j > 0; j--){
                nova += p2.substring(j-1, j);
            }

            System.out.println(nova);
        }
        
    }
}
