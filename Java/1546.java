public import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        for(int i = 0; i < x; i++){
            int n = scanner.nextInt();
            for(int j = 0; j < n; j++){
                int y = scanner.nextInt();
                if(y == 1){
                    System.out.println("Rolien");
                }else if(y == 2){
                    System.out.println("Naej");
                }else if(y == 3){
                    System.out.println("Elehcim");
                }else{
                    System.out.println("Odranoel");
                }
            }
        }

    }
} 1546 {
    
}
