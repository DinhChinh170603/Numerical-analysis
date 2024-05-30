package PTViPhan;

import java.util.Scanner;

public class HeunMethod {
    private static double h;
    public static double differential (double x, double y) {
        return 2*x*y;
    }
    public static double predictorY(double x, double y) {
        return y + h*differential(x, y);
    }
    public static double yCorrect(double x) {
        return Math.exp(Math.pow(x,2)-1);
    }
    public static double correctorY(double x, double y, double yPre) {
        return y + h/2*(differential(x, y) + differential(x+h, yPre));
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap h: ");
        h = sc.nextDouble();
        System.out.print("Nhap x: ");
        double x = sc.nextDouble();
        System.out.print("Nhap y: ");
        double y = sc.nextDouble();
        double saiSo = 0;
        for (int i = 1; i <= 10; i ++) {
            System.out.println("yPre" + i + "=" + predictorY(x, y));
            double yPre = predictorY(x, y);
            System.out.println("y" + i + "=" + correctorY(x, y, yPre));
            y = correctorY(x, y, yPre);
            x += h;
            saiSo = Math.abs(yCorrect(x) - y);
            System.out.println("Sai so: " + saiSo);
            System.out.println();
        }
    }
}
