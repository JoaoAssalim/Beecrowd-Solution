import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double count = 0;
        int n = scanner.nextInt();
        for(int i = 0; i < n; i++){
            double a = scanner.nextDouble(), b = scanner.nextDouble();
            count += a/b;
        }
        if(count <= 1){
            System.out.println("OK");
        }else{
            System.out.println("FAIL");
        }
    }
}
