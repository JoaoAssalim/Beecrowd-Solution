import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i = 1; i <= n; i++){
            int b = i*i, c = i*i*i;
            System.out.println(i + " " + b + " " + c);
        }
    }
}
