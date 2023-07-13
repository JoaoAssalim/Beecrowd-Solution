import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int total = 0;
            int n = sc.nextInt();
            sc.nextLine();
            for(int y = 0; y < n; y++){
                if(y > 0){
                    sc.nextLine();
                }
                String especie = sc.nextLine();
                String[] raca = sc.nextLine().split(" ");
                String[] nome = sc.nextLine().split(" ");

                boolean ver = false;
                if(especie.equals("cachorro")){
                    if(nome.length > 1){
                        for(int j = 0; j < nome.length; j++){
                            if(raca[0].substring(0, 1).equals(nome[j].substring(0, 1))){
                                ver = true;
                                break;
                            }
                        }
                    }
                }if(ver){
                    total++;
                }
            }
            System.out.println(total);
        }

    }
}
