import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int n = sc.nextInt();
            if(n == 0)
                break;
            if(n == 3){
                System.out.println(1);
            }else{
                long res = 1;
                for(long i = 4; i <= n; i++){
                    res = (res*i) % 1000000009;
                }
                System.out.println(res);
            }
            
        }
        
    }
}
