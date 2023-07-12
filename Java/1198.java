import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLong()){
            long a = sc.nextLong(), b = sc.nextLong();
            long c = Math.abs(a-b);
            System.out.println(c);
        }
    }
}
