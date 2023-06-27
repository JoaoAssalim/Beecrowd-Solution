import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        String[] ns = s.split(" ");
        int total = Integer.parseInt(ns[1]) - Integer.parseInt(ns[0]);

        if(total >= 3){
            System.out.println("Muito bem! Apresenta antes do Natal!");
        }else if(total > 0 && total <= 2){
            if(Integer.parseInt(ns[1]) < 23){
                System.out.println("Parece o trabalho do meu filho!");
                System.out.println("TCC Apresentado!");
            }else{
                System.out.println("Parece o trabalho do meu filho!");
                System.out.println("Fail! Entao eh nataaaaal!");
            }
        }else{
            System.out.println("Eu odeio a professora!");
        }
    }
}
