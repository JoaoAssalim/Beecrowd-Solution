import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int atual = 0, cont = 0;

        for(int i = 0; i < n; i++){
            int num = sc.nextInt();
            if(i == 0){
                atual = num;
                cont++;
            }else if(atual != num){
                atual = num;
                cont++;
            }
        }
        System.out.println(cont);
    }
}
