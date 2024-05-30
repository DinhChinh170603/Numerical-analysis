package PTViPhan;

import java.util.Scanner;

public class RungeKuttaMethod3 {
    private static double h;

    public static double differential(double x, double y) {
        return 2*x*y;
    }

    public static double K1(double x, double y) {
        return differential(x, y);
    }

    public static double K2(double x, double y, double K1) {
        return differential(x + h / 2, y + h / 2 * K1);
    }

    public static double K3(double x, double y, double K1, double K2) {
        return differential(x + h, y - K1 * h + h * 2 * K2);
    }


    public static double yCorrect(double x) {
        return Math.exp(Math.pow(x, 2) - 1);
    }

    public static double y(double y, double K1, double K2, double K3) {
        return y + h / 6 * (K1 + 4 * K2 + K3);
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
        for (int i = 1; i <= 10; i++) {
            double K1 = K1(x,y);
            System.out.println("K1: " + K1);
            double K2 = K2(x, y, K1);
            System.out.println("K2: " + K2);
            double K3 = K3(x, y, K1, K2);
            System.out.println("K3: " + K3);
            System.out.println("y" + i + "=" + y(y, K1, K2, K3));
            y = y(y, K1, K2, K3);
            x += h;
            saiSo = Math.abs(yCorrect(x) - y);
            System.out.println("Sai so: " + saiSo);
            System.out.println();
        }
    }
}
