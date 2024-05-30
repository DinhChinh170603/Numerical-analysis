package GiaiPT;

public class FalsePositionMethod {

    public static void main(String[] args) {
        double a = 0; // Điểm bắt đầu
        double b = 1; // Điểm kết thúc

        double solution = solve(a, b);

        System.out.println("Nghiệm gần dúng của phương trình là: " + solution);
    }

    public static double f(double x) {
        return Math.cos(x) - x;
    }

    public static double solve(double a, double b) {
        double epsilon = 0.0001; // Sai số mong muốn

        double fa = f(a);
        double fb = f(b);

        if (fa * fb > 0) {
            System.out.println("Không thể áp dụng phương pháp điểm sai cho đoạn [" + a + ", " + b + "]");
            return Double.NaN;
        }

        double c;
        double fc;

        do {
            c = (a * fb - b * fa) / (fb - fa);
            fc = f(c);

            if (fa * fc < 0) {
                b = c;
                fb = fc;
            } else {
                a = c;
                fa = fc;
            }
        } while (Math.abs(fc) > epsilon);

        return c;
    }
}