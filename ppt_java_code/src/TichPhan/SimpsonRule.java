package TichPhan;

import java.lang.Math;
import java.util.Scanner;

public class SimpsonRule {
    private static final double pi = Math.PI;
    private static double a, b, h;

    public static double f(double x) {
        return Math.log(2.7*x+5.6);
    }

    public static double g(double x) {
        return 1/2.7*(2.7*x*Math.log(2.7*x+5.6)+5.6*Math.log(2.7*x+5.6)-2.7*x-5.6);
    }

    public static double solve(double left, double right ) {
        return (right - left) / 6 * (f(left) + 4 * f(left + (right - left) / 2) + f(right));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap a: ");
        a = sc.nextDouble();
        System.out.print("Nhap b: ");
        b = sc.nextDouble();
        System.out.print("Nhap n: ");
        int n = sc.nextInt();
        h = (b - a)/ n;
        double result = 0;
        for (int i = 0; i < n; i++) {
            result += solve(a+ i*h, a+ (i+1)*h);
        }
        System.out.println("Gia tri sap si tich phan tu a den b cua f(x): " + result);
        System.out.println("Sai so: " + Math.abs(g(b) - g(a) - result));
    }
}
