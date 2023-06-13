import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        double d = ((a*2) + (b*3) + (c*5))/10;
        System.out.printf("MEDIA = %.1f\n", d);
    }
}
