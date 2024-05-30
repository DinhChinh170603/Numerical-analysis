package TichPhan;

import java.lang.Math;
import java.util.Scanner;

public class MidpointRule {
    private static final double pi = Math.PI;
    private static double a, b, h;

    public static double f(double x) {
        return Math.exp(x);
    }

    public static double g(double x) {
        return Math.exp(x);
    }

    public static double solve(double left, double right ) {
        return 2*h*f(right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap a: ");
        a = sc.nextDouble();
        System.out.print("Nhap b: ");
        b = sc.nextDouble();
        System.out.print("Nhap n: ");
        int n;
        while (true) {
            n = sc.nextInt();
            if (n % 2 == 0) {
                break;
            } else {
                System.out.println("n phai la so chan");
                System.out.print("Nhap n: ");
            }
        }
        h = (b - a)/ (n+2);
        double result = 0;
        for (int i = 0; i <= n; i++) {
            if(i % 2 == 0) result += solve(a+ i*h, a+ (i+1)*h);
        }
        System.out.println("Gia tri sap si tich phan tu a den b cua f(x): " + result);
        System.out.println("Sai so: " + Math.abs(g(b) - g(a) - result));
    }
}
