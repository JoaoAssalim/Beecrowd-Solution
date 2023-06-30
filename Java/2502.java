import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int a = sc.nextInt(), b = sc.nextInt();
            HashMap<String, String> s = new HashMap<>();
            sc.nextLine();
            String s1 = sc.nextLine(), s2 = sc.nextLine();
            String aux1 = s1.toLowerCase(), aux2 = s2.toLowerCase();

            for(int i = 0; i < a; i++){
                s.put(s1.substring(i, i+1), s2.substring(i, i+1));
                s.put(aux1.substring(i, i+1), aux2.substring(i, i+1));
                s.put(s2.substring(i, i+1), s1.substring(i, i+1));
                s.put(aux2.substring(i, i+1), aux1.substring(i, i+1));
            }
            for(int i = 0; i < b; i++){
                String n = sc.nextLine();
                for(int j = 0; j < n.length(); j++){
                    if(s.get(n.substring(j, j+1)) != null){
                        System.out.print(s.get(n.substring(j, j+1)));
                    }else{
                        System.out.printf(n.substring(j, j+1));
                    }
                }
                System.out.println();
            }
            System.out.println();
        }

    }
}
