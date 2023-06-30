import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int aux = 0;
        for(int i = 0; i <= n; i++){
            String s = sc.nextLine();
            if(s.contains("CD")){
                aux++;
            }
        }
        System.out.println(n-aux);

    }
}
