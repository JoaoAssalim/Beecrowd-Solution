import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        sc.nextLine();
        for(int i = 0; i < n; i++){
            String[] s = sc.nextLine().split(" ");
            int x = Integer.parseInt(s[s.length-1]);
            if(x > m){
                System.out.printf(s[0]);
                for(int j = 1; j < s.length-1; j++){
                    System.out.printf(" " + s[j]);
                }
                System.out.println();
            }
        }

    }
}
