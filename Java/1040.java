import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float n1 = sc.nextFloat(), n2 = sc.nextFloat(), n3 = sc.nextFloat(), n4 = sc.nextFloat();
        float media = (n1*2 + n2*3 + n3*4 +n4*1)/10;

        if (media >= 7.0){
            System.out.printf("Media: %.1f\n", media);
            System.out.println("Aluno aprovado.");
        }else if (media < 5.0){
            System.out.printf("Media: %.1f\n", media);
            System.out.println("Aluno reprovado.");
        }else{
            System.out.printf("Media: %.1f\n", media);
            System.out.println("Aluno em exame.");
            float exame = sc.nextFloat();
            System.out.printf("Nota do exame: %.1f\n", exame);
            float media_final = (media + exame) / 2;
            if (media_final >= 5){
                System.out.printf("Aluno aprovado.\n");
                System.out.printf("Media final: %.1f\n", media_final);
            }else{
                System.out.printf("Aluno reprovado.\n");
                System.out.printf("Media final: %.1f\n", media_final);
            }
        }
    }
}
