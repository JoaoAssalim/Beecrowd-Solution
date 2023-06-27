import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        float count = 0;
        int n = scanner.nextInt();
        for(int i = 0; i < n; i++){
            float a = scanner.nextFloat(), b = scanner.nextFloat();
            count += a/b;
        }
        if(count <= 1){
            System.out.println("OK");
        }else{
            System.out.println("FAIL");
        }
    }
}
