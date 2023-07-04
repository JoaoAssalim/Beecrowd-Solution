import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int n = sc.nextInt();
            int a = 0, b = 0;
            if(n == 0){
                break;
            }
            for(int i = 0; i < n; i++){
                int x = sc.nextInt();
                if(x == 0)
                    a++;
                else
                    b++;
            }
            System.out.println("Mary won " + a + " times and John won " + b + " times");
        }

    }
}
