package GiaiPT;

import static java.lang.Math.pow;

public class BisectionMethod {

    public static void main(String[] args) {
        double a = 1; // Điểm bắt đầu
        double b = 2; // Điểm kết thúc
        double epsilon = 0.02; // Sai số mong muốn

        double solution = solve(a, b, epsilon);

        System.out.println("Nghiệm gần đúng của phương trình là: " + solution);
    }

    public static double f(double x) {
        return pow(x,3) - pow(x,1) - 1;
    }
    public static double solve(double a, double b, double epsilon) {
        double fa = f(a);
        double fb = f(b);

        if (fa * fb > 0) {
            System.out.println("Không thể áp dụng phương pháp chia đôi cho đoạn [" + a + ", " + b + "]");
            return Double.NaN;
        }

        double c;

        do {
            c = (a + b) / 2;
            double fc = f(c);

            if (fa * fc < 0) {
                b = c;
                fb = fc;
            } else {
                a = c;
                fa = fc;
            }
        } while (Math.abs(b - a) > epsilon);

        return (a + b) / 2;
    }
}