package GiaiPT;

public class SecantMethod {

    public static void main(String[] args) {
        double x0 = -0.5; // Giá trị ban đầu
        double x1 = 2; // Giá trị ban đầu khác x0

        double solution = solve(x0, x1);

        System.out.println("Nghiệm gần đúng của phương trình là: " + solution);
    }

    public static double f(double x) {
        return Math.sin(x) - Math.pow(x, 2) * Math.cos(x);
    }

    public static double solve(double x0, double x1) {
        double epsilon = 0.001; // Sai số mong muốn
        double x = x1;
        double fx = f(x);
        double xPrev = x0;
        double fxPrev = f(xPrev);

        while (Math.abs(fx-fxPrev) > epsilon) {
            if (Math.abs(fx - fxPrev) < epsilon) {
                System.out.println("Phương pháp dây cung không hội tụ với cặp điểm ban đầu (" + x0 + ", " + x1 + ")");
                return Double.NaN;
            }

            double xNext = x - (fx * (x - xPrev)) / (fx - fxPrev); // Cập nhật giá trị mới

            xPrev = x;
            fxPrev = fx;
            x = xNext;
            fx = f(x); // Tính giá trị hàm f(x) tại x mới
        }

        return x;
    }
}