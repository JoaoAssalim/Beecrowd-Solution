import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double n = 0, count = 0;

        while(sc.hasNextLine()){
            String nome = sc.nextLine();
            double dist = sc.nextDouble();
            n += dist;
            count++;
            sc.nextLine();
        }
        double total = n/count;
        System.out.printf("%.1f\n", total);
        
    }
}
