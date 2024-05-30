package PTViPhan;

import java.util.Scanner;

public class MidpointMethod {
    private static double h;
    public static double differential (double x, double y) {
        return 2*x*y;
    }
    public static double y(double x, double y, double yMid) {
        return y + h*differential(x, yMid);
    }
    public static double yCorrect(double x) {
        return Math.exp(Math.pow(x,2)-1);
    }
    public static double yMidpont(double x, double y) {
        return y + h/2*differential(x, y);
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
            System.out.println("y" + (i - 0.5) + "=" + yMidpont(x, y));
            double yMid = yMidpont(x, y);
            x += h/2;
            System.out.println("y" + i + "=" + y(x, y, yMid));
            y = y(x, y, yMid);
            x += h/2;
            saiSo = Math.abs(yCorrect(x) - y);
            System.out.println("Sai so: " + saiSo);
            System.out.println();
        }
    }
}
