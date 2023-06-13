import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        float b = scanner.nextFloat();
        float c = scanner.nextFloat();
        float d = (b*c);
        System.out.println("NUMBER = " + a);
        System.out.printf("SALARY = U$ %.2f\n", d);
    }
}
