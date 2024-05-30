package GiaiPT;

import static java.lang.Math.pow;

public class FixedPointMethod {

    public static void main(String[] args) {
        double x0 = 0; // Giá trị ban đầu

        double solution = solve(x0);

        System.out.println("Nghiệm gần đúng của phương trình là: " + solution);
    }

    public static double g(double x) {
        return pow(3+x-2* pow(x,2),0.25);
    }

    public static double f(double x) {
        return pow(x,4) + 2*pow(x,2) - x - 3;
    }
    public static double solve(double x0) {
        double epsilon = 0.0000001; // Sai số mong muốn
        double x = x0;
        double fx = f(x);

        while (Math.abs(fx) > epsilon) {
            x = g(x); // Cập nhật giá trị mới
            fx = f(x); // Tính giá trị hàm f(x) tại x mới
        }

        return x;
    }
}