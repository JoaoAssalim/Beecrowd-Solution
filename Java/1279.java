import java.math.BigInteger;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = 1;
        while(sc.hasNextBigInteger()){
            BigInteger ano = sc.nextBigInteger();
            if(c > 1){
                System.out.println();
            }
            int ver = 0;
            if((ano.mod(BigInteger.valueOf(4)) == BigInteger.valueOf(0) && ano.mod(BigInteger.valueOf(100)) != BigInteger.valueOf(0)) || (ano.mod(BigInteger.valueOf(400)) == BigInteger.valueOf(0))){
                System.out.println("This is leap year.");
                ver = 1;
            }
            if(ano.mod(BigInteger.valueOf(15)) == BigInteger.valueOf(0)){
                System.out.println("This is huluculu festival year.");
                ver = 1;
            }
            if((ano.mod(BigInteger.valueOf(55)) == BigInteger.valueOf(0)) && ((ano.mod(BigInteger.valueOf(4)) == BigInteger.valueOf(0) && ano.mod(BigInteger.valueOf(100)) != BigInteger.valueOf(0)) || (ano.mod(BigInteger.valueOf(400)) == BigInteger.valueOf(0)))){
                System.out.println("This is bulukulu festival year.");
                ver = 1;
            }
            if(ver == 0){
                System.out.println("This is an ordinary year.");
            }
            c++;
        }

    }
}
