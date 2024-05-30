package DaoHam;

import java.lang.Math;
import java.util.Scanner;

public class FivepointFormulas {
    private static final double pi = Math.PI;
    private static double h;

    public static double f(double x) {
        return Math.sin(x);
    }

    public static double g(double x) {
        return Math.cos(x);
    }

    public static double solve(double x) {
        return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap h: ");
        h = sc.nextDouble();
        System.out.print("Nhap x: ");
        double x = sc.nextDouble();
        double result;
        result = solve(x);
        System.out.println("Gia tri xap xi cua f'(x): " + result);
        System.out.println("Sai so: " + Math.abs(g(x) - result));
    }
}
