import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), l = sc.nextInt(), d = sc.nextInt();
        int qt = l*1000, cafe = 1;

        while(qt/d < n){
            qt += l*1000;
            cafe++;
        }
        System.out.println(cafe*l);

    }
}
