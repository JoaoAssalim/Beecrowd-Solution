import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble(), b = sc.nextDouble();
        System.out.printf("%.6f\n", ((((1.0 + a/100.00) * (1.0 + b/100.00)) - 1.0) * 100.0));

    }
}
