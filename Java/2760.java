import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine(), b = sc.nextLine(), c = sc.nextLine();
        System.out.printf("%s%s%s\n", a,b,c);
        System.out.printf("%s%s%s\n", b,c,a);
        System.out.printf("%s%s%s\n", c,a,b);
        if(a.length() > 10)
            System.out.printf("%s", a.substring(0, 10));
        else 
            System.out.printf("%s", a);
        if(b.length() > 10)
            System.out.printf("%s", b.substring(0, 10));
        else 
            System.out.printf("%s", b);
        if(c.length() > 10)
            System.out.printf("%s\n", c.substring(0, 10));
        else 
            System.out.printf("%s\n", c);
    }
}
