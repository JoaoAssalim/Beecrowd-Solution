import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<Double> la = new ArrayList<>();
        List<Double> lb = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        
        String a = scanner.nextLine();
        String[] na = a.split(" ");
        for (String numero : na) {
            double valor = Double.parseDouble(numero);
            la.add(valor);
        }

        String b = scanner.nextLine();
        String[] nb = b.split(" ");
        for (String numero : nb) {
            double valor = Double.parseDouble(numero);
            lb.add(valor);
        }

        double x = la.get(1) * la.get(2) + lb.get(1) * lb.get(2);
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", x);
    }
}