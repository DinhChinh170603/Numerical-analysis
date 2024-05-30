package HePTViPhan;

import java.util.Scanner;

public class EulerMethodSystem {
    private static double h;
    public static double differentialY1 (double x, double y1, double y2) {
        return y2;
    }
    public static double differentialY2 (double x, double y1, double y2) {
        return 2 - 2*y2 - 8*y1;
    }
    public static double yCorrect(double x) {
        return x + 1/3*Math.pow(x, 3) - 16/3;
    }
    public static double y1(double x, double y1, double y2) {
        return y1 + h*differentialY1(x, y1, y2);
    }
    public static double y2(double x, double y1, double y2) {
        return y2 + h*differentialY2(x, y1, y2);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap h: ");
        h = sc.nextDouble();
        System.out.print("Nhap x: ");
        double x = sc.nextDouble();
        System.out.print("Nhap y1: ");
        double y1 = sc.nextDouble();
        System.out.print("Nhap y2: ");
        double y2 = sc.nextDouble();
        double saiSo = 0;
        for (int i = 1; i <= 10; i ++) {
            System.out.println("y1(" + (x + h) + ")=" + y1(x, y1, y2));
            System.out.println("y2(" + (x + h) + ")=" + y2(x, y1, y2));
            double y1Pre = y1;
            y1 = y1(x, y1, y2);
            y2 = y2(x, y1Pre, y2);
            x += h;
//            saiSo = Math.abs(yCorrect(x) - y);
//            System.out.println("Sai so: " + saiSo);
            System.out.println();
        }
    }
}
