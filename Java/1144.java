import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i = 1; i <= n; i++){
            int b = i*i, c = i*i*i;
            int d = b+1, e = c+1;
            System.out.println(i + " " + b + " " + c);
            System.out.println(i + " " + d + " " + e);
        }
    }
}
