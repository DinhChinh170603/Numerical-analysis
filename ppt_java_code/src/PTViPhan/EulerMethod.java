package PTViPhan;

import java.util.Scanner;

public class EulerMethod {
    private static double h;
    public static double differential (double x, double y) {
        return 1 + Math.pow(x, 2);
    }
    public static double yCorrect(double x) {
        return x + 1/3*Math.pow(x, 3) - 16/3;
    }
    public static double y(double x, double y) {
        return y + h*differential(x, y);
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
            System.out.println("y" + i + "=" + y(x, y));
            y = y(x, y);
            x += h;
            saiSo = Math.abs(yCorrect(x) - y);
            System.out.println("Sai so: " + saiSo);
            System.out.println();
        }
    }
}
