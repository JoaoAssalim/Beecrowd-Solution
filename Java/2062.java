import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] pal = sc.nextLine().split(" ");

        for(int i = 0; i < pal.length; i++){
            if(pal[i].contains("OB") && pal[i].length() <= 3){
                pal[i] = "OBI";
            }if(pal[i].contains("UR") && pal[i].length() <= 3){
                pal[i] = "URI";
            }
        }

        for(int i = 0; i < pal.length; i++){
            if(i == pal.length-1){
                System.out.println(pal[i]);
            }else{
                System.out.printf("%s ", pal[i]);
            }
        }
    }
}
