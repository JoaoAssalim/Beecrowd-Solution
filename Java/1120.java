import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){
            String a = sc.nextLine();
            String[] n = a.split(" ");
            if(n[0].equals("0") && n[1].equals("0")){
                break;
            }
            String nova = "";

            for(int i = 0; i < n[1].length(); i++){
                if(!n[1].substring(i, i+1).equals(n[0])){
                    nova += n[1].substring(i, i+1);
                }
            }

            if(nova.equals("")){
                System.out.println(0);
            }else{
                BigInteger x = new BigInteger(nova);
                System.out.println(x);
            }

        }
    }
}
