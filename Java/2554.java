import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int n = sc.nextInt(), n1 = sc.nextInt();
            String total = "0";
            sc.nextLine();
            for(int i = 0; i < n1; i++){
                String s = sc.nextLine();
                String[] dados = s.split(" ");
                boolean ver = true;

                for(int j = 1; j <= n; j++){
                    if(!dados[j].equals("1"))
                        ver = false;
                }

                if(ver && total.equals("0")){
                        total = dados[0];
                }
            }

            if(!total.equals("0")){
                System.out.println(total);
            }else{
                System.out.println("Pizza antes de FdI");
            }
        }
    }
}
