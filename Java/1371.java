import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int n = sc.nextInt();
            if(n == 0)
                break;
            int ant = 1;
            int i = 1;
            System.out.print("1");
            while(i*i <= n){
                if(ant != 1){
                    System.out.print(" " + ant);
                }
                ant = i*i;
                i++;
            }
            if(ant != 1){
                System.out.println(" " + ant);
            }else{
                System.out.println();
            }
            
        }
        
    }
}
