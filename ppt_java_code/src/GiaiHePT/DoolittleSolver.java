package GiaiHePT;

public class DoolittleSolver {

    public static void main(String[] args) {
        // Ma trận A
        double[][] A = {
                {4, -1, 0, 0, 0, 0, 0, 0, 0, 0},
                {-1, 4, -1, 0, 0, 0, 0, 0, 0, 0},
                {0, -1, 4, -1, 0, 0, 0, 0, 0, 0},
                {0, 0, -1, 4, -1, 0, 0, 0, 0, 0},
                {0, 0, 0, -1, 4, -1, 0, 0, 0, 0},
                {0, 0, 0, 0, -1, 4, -1, 0, 0, 0},
                {0, 0, 0, 0, 0, -1, 4, -1, 0, 0},
                {0, 0, 0, 0, 0, 0, -1, 4, -1, 0},
                {0, 0, 0, 0, 0, 0, 0, -1, 4, -1},
                {0, 0, 0, 0, 0, 0, 0, 0, -1, 4}
        };

        // Vector b
        double[] b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        // Giải hệ phương trình
        double[] x = solve(A, b);

        // In nghiệm
        System.out.println("Nghiệm của hệ phương trình:");
        for (int i = 0; i < x.length; i++) {
            System.out.println("x[" + i + "] = " + x[i]);
        }
    }

    public static double[] solve(double[][] A, double[] b) {
        int n = A.length;

        // Khởi tạo ma trận tam giác dưới L và ma trận tam giác trên U
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];

        // Phân tích Doolittle
        for (int i = 0; i < n; i++) {
            // Tính các phần tử của ma trận L
            for (int j = 0; j <= i; j++) {
                double sum = 0;
                for (int k = 0; k < j; k++) {
                    sum += L[i][k] * U[k][j];
                }
                L[i][j] = A[i][j] - sum;
            }

            // Tính các phần tử của ma trận U
            for (int j = i; j < n; j++) {
                double sum = 0;
                for (int k = 0; k < i; k++) {
                    sum += L[i][k] * U[k][j];
                }
                U[i][j] = (A[i][j] - sum) / L[i][i];
            }
        }

        System.out.println("Ma trận L:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(L[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("Ma trận U:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(U[i][j] + " ");
            }
            System.out.println();
        }
        // Giải hệ phương trình Ly = b
        double[] y = forwardSubstitution(L, b);

        // Giải hệ phương trình Ux = y
        double[] x = backwardSubstitution(U, y);

        return x;
    }

    // Giải hệ phương trình tam giác trước
    public static double[] forwardSubstitution(double[][] L, double[] b) {
        int n = L.length;
        double[] y = new double[n];

        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < i; j++) {
                sum += L[i][j] * y[j];
            }
            y[i] = (b[i] - sum) / L[i][i];
        }

        return y;
    }

    // Giải hệ phương trình tam giác sau
    public static double[] backwardSubstitution(double[][] U, double[] b) {
        int n = U.length;
        double[] x = new double[n];

        for (int i = n - 1; i >= 0; i--) {
            double sum = 0;
            for (int j = i + 1; j < n; j++) {
                sum += U[i][j] * x[j];
            }
            x[i] = (b[i] - sum) / U[i][i];
        }

        return x;
    }
}
