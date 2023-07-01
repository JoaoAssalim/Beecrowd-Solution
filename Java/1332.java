import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.nextLine();
        for(int i = 0; i < x; i++){
            String pal = sc.nextLine();
            if(pal.length() == 3){
                if(pal.substring(0, 1).equals("o") && pal.substring(1, 2).equals("n")){
                    System.out.println(1);
                }else if(pal.substring(0, 1).equals("o") && pal.substring(2, 3).equals("e")){
                    System.out.println(1);
                }else if(pal.substring(1, 2).equals("n") && pal.substring(2, 3).equals("e")){
                    System.out.println(1);
                }else{
                    System.out.println(2);
                }
            }else{
                System.out.println(3);
            }
        }
        
    }
}
