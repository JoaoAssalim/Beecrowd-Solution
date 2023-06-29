import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            long x = sc.nextLong();
            String bx = Long.toBinaryString(x);
            int cont = 0, aux = 0;
            for(int j = 0; j < bx.length(); j++){
                String charAtIndex = String.valueOf(bx.charAt(j));
                boolean isEqualToZero = charAtIndex.equals("0");

                if(isEqualToZero){
                    if(aux > cont)
                        cont = aux;
                        aux = 0;
                }else{
                    aux += 1;
                }
            }
            if(aux > cont)
                cont = aux;
            System.out.println(cont);
        }

    }
}
