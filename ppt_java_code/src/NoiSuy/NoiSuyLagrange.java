package NoiSuy;// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import java.lang.Math;
import java.util.ArrayList;
import java.util.Scanner;

public class NoiSuyLagrange {
    private static final double pi = Math.PI;
    public static int num;
    public static ArrayList<Double> a = new ArrayList<>();

    public static double f(double x) {
        return Math.sin(x)*Math.exp(2*x);
    }
    public static String printL(int x) {
        String result = "";
        double denominator = 1;
        for (int i = 0; i < num ; i++) {
            if (i == x) continue;
            double val = (double) a.get(i);
            double valRound = (double) Math.round(val * 1000000) / 1000000;
            result += "(x-" + valRound + ")";
            denominator *= ((double) a.get(x) - (double) a.get(i));
        }
        result += "/" + (double) Math.round(denominator * 1000000) / 1000000;
        result += " * " + (double) Math.round(f(a.get(x)) * 1000000) / 1000000;
        return result;
    }
    public static double calcL(int x, double val) {
        double result = 1;
        double denominator = 1;
        for (int i = 0; i < num ; i++) {
            if (i == x) continue;
            result *= (val - a.get(i));
            denominator *= ((double) a.get(x) - (double) a.get(i));
        }
        result /= denominator;
        result *= f(a.get(x));
        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        System.out.println("Nhap lan luot 2 moc trai phai khoang xac dinh cua f(x):");
        double left = 0;
        double right = pi / 2;
//        System.out.println("Nhap so diem moc cach deu: ");
        num = 50;
        a = new ArrayList<>();
        for (int i = 0; i < num; i++) {
            double val = left + (right - left) / (num - 1) * i;
            a.add(val);
        }
        System.out.println("Da thuc noi suy cua f(x) theo phuong phap Lagrange theo 50 diem moc cach deu:");
        for (int i = 0; i < num; i++) {
            System.out.println(printL(i) + (i<num-1 ? " + " : ""));
        }
//        System.out.println("Nhap gia tri cua x:");
        double x = pi / 200;
        double result = 0;
        for (int i = 0; i < num; i++) {
            result += calcL(i, x);
        }
        System.out.println("Gia tri cua f(x) tinh boi da thuc noi suy Lagrange la:");
        System.out.println(result);
        System.out.println("Sai so cua bieu thuc la:");
        System.out.println(Math.abs(f(x) - result));
//        System.out.println(f(x));
    }
}