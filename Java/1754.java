import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            double a = sc.nextDouble(), b = sc.nextDouble();
            long c = (long) Math.ceil(a/b);
            if(c <= 2)
                System.out.println(2);
            else
                System.out.println(c);

        }
        
    }
}
