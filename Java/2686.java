import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNextFloat()){
            float n = sc.nextFloat();
            if(n >= 0 && n < 90){
                n = n*240;
                int nw = (int) n;
                int h = 6 + (nw/3600);
                nw = nw%3600;
                int m = nw/60;
                nw = nw%60;
                int s = nw;
                System.out.printf("Bom Dia!!\n");
                if(h < 10) {
                    System.out.printf("0%d:", h);
                }else{
                    System.out.printf("%d:", h);
                }if(m < 10) {
                    System.out.printf("0%d:", m);
                }else{
                    System.out.printf("%d:", m);
                }if(s < 10) {
                    System.out.printf("0%d\n", s);
                }else{
                    System.out.printf("%d\n", s);
                }
            }else if(n >= 90 && n < 180){
                n -= 90;
                n = n*240;
                int nw = (int) n;
                int h = 12 + (nw/3600);
                nw = nw%3600;
                int m = nw/60;
                nw = nw%60;
                int s = nw;
                System.out.printf("Boa Tarde!!\n");
                if(h < 10) {
                    System.out.printf("0%d:", h);
                }else{
                    System.out.printf("%d:", h);
                }if(m < 10) {
                    System.out.printf("0%d:", m);
                }else{
                    System.out.printf("%d:", m);
                }if(s < 10) {
                    System.out.printf("0%d\n", s);
                }else{
                    System.out.printf("%d\n", s);
                }
            }else if(n >= 180 && n < 270){
                n -= 180;
                n = n*240;
                int nw = (int) n;
                int h = 18 + (nw/3600);
                nw = nw%3600;
                int m = nw/60;
                nw = nw%60;
                int s = nw;
                System.out.printf("Boa Noite!!\n");
                if(h < 10) {
                    System.out.printf("0%d:", h);
                }else{
                    System.out.printf("%d:", h);
                }if(m < 10) {
                    System.out.printf("0%d:", m);
                }else{
                    System.out.printf("%d:", m);
                }if(s < 10) {
                    System.out.printf("0%d\n", s);
                }else{
                    System.out.printf("%d\n", s);
                }
            }else{
                n -= 270;
                n = n*240;
                int nw = (int) n;
                int h = (nw/3600);
                nw = nw%3600;
                int m = nw/60;
                nw = nw%60;
                int s = nw;
                System.out.printf("De Madrugada!!\n");
                if(h < 10) {
                    System.out.printf("0%d:", h);
                }else{
                    System.out.printf("%d:", h);
                }if(m < 10) {
                    System.out.printf("0%d:", m);
                }else{
                    System.out.printf("%d:", m);
                }if(s < 10) {
                    System.out.printf("0%d\n", s);
                }else{
                    System.out.printf("%d\n", s);
                }
        }
        }
    }
}
