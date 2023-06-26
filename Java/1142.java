import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int aux = 1;
        for(int i = 0; i < n; i++){
            int b = aux+1, c = aux+2;
            System.out.println(aux + " " + b + " " + c + " PUM");
            aux += 4;
        }
    }
}
