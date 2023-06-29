import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int x = sc.nextInt(), y = sc.nextInt();
            int[][] m = new int[x][y];
            int px=0,py=0,ex=0,ey=0;

            for(int i = 0; i < x; i++){
                for(int j = 0; j < y; j++){
                    int n = sc.nextInt();
                    if(n == 2){
                        px = i;
                        py = j;
                    }else if(n == 1){
                        ex = i;
                        ey = j;
                    }
                }
            }
            int med = Math.abs(ex-px) + Math.abs(ey-py);
            System.out.println(med);
        }
    }
}
