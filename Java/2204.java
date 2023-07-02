import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for(int i = 0; i < n; i++){
            String x = sc.nextLine();
            String[] s = x.split(" ");

            if(s[0].equals(s[1])){
                System.out.println(s[0]);
            }else{
                System.out.println(1);
            }
        }

    }
}
