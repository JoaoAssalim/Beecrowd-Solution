import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt(), E = sc.nextInt(), A = sc.nextInt(), O = sc.nextInt(), W = sc.nextInt(), X = sc.nextInt();
        if((H+E+A+X) >= O+W)
            System.out.println("Middle-earth is safe.");
        else
            System.out.println("Sauron has returned.");
    }
}
