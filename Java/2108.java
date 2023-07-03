import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String maior = "";
        while(sc.hasNextLine()){
            String cc = "";
            String[] pal = sc.nextLine().split(" ");
            if(pal[0].contains("0")){
                break;
            }
            for(int i = 0; i < pal.length; i++){
                if(i == pal.length-1)
                    System.out.println(pal[i].length());
                else
                    System.out.printf("%d-", pal[i].length());
                if(pal[i].length() >= maior.length())
                    maior = pal[i];
            }
        }
        System.out.println();
        System.out.println("The biggest word: " + maior);
        
    }
}
