package GiaiPT;

import static java.lang.Math.pow;

public class NewtonMethod {

    public static void main(String[] args) {
        double x0 = 1; // Giá trị ban đầu

        double solution = solve(x0);

        System.out.println("Nghiệm gần đúng của phương trình là: " + solution);
    }

    public static double g(double x) {
        return 4*pow(x,3) + 4*x - 1;
    }

    public static double f(double x) {
        return pow(x,4) + 2*pow(x,2) - x - 3;
    }

    public static double solve(double x0) {
        double epsilon = 0.0001; // Sai số mong muốn
        double x = x0;
        double fx = f(x);
        double fPrimeX = g(x);

        while (Math.abs(fx) > epsilon) {
            if (Math.abs(fPrimeX) < epsilon) {
                System.out.println("Phương pháp Newton không hội tụ tại điểm ban đầu x = " + x);
                return Double.NaN;
            }

            x = x - fx / fPrimeX; // Cập nhật giá trị mới

            fx = f(x); // Tính giá trị hàm f(x) tại x mới
            fPrimeX = g(x); // Tính giá trị đạo hàm f'(x) tại x mới
        }

        return x;
    }
}