import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for(int i = 0; i < n; i++){
            int a = scanner.nextInt(), b = scanner.nextInt();
            BigInteger res = BigInteger.valueOf(a).pow(BigInteger.valueOf(b).intValue());
            System.out.println(res.toString().length());
        }
    }
}
