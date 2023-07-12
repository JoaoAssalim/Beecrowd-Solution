import java.util.Scanner;


public class Main {
    public static int mdc(int a, int b){
        while(b != 0){
            double resto = a % b;
            a = b;
            b = (int) resto;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> s = new ArrayList<String>();

        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            int a = sc.nextInt(), b = sc.nextInt();
            System.out.println(mdc(a, b));
        }
    }
}
