import java.util.Scanner;


public class Main {
    public static boolean isPrime(int n){
        if(n == 1) return false;
        if(n==2 || n == 3) return true;

        int cont = 0;
        for(int i = 2; i < Math.sqrt(n)+1; i++){
            if(n % i == 0)
                cont++;
        }
        if(cont == 0) return true;
        return false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            int num = sc.nextInt();
            if(isPrime(num)){
                System.out.println("Prime");
            }else{
                System.out.println("Not Prime");
            }
        }
    }
}
