package GiaiHePT;

import java.util.Arrays;

public class CholeskySolver {

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

//         Kiểm tra tính đối xứng và xác định dương của ma trận A
        if (!isSymmetric(A)) {
            System.out.println("Ma trận A không đối xứng");
            return null;
        }

        // Phân tích Cholesky
        double[][] L = choleskyDecomposition(A);
        System.out.println("Ma trận L:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(L[i][j] + " ");
            }
            System.out.println();
        }

        // Giải hệ phương trình Ly = b
        double[] y = forwardSubstitution(L, b);

        // Giải hệ phương trình L^T x = y
        double[] x = backwardSubstitution(transpose(L), y);

        return x;
    }

    // Kiểm tra tính đối xứng của ma trận
    public static boolean isSymmetric(double[][] A) {
        int n = A.length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (A[i][j] != A[j][i]) {
                    return false;
                }
            }
        }

        return true;
    }

    // Kiểm tra tính xác định dương của ma trận
    public static boolean isPositiveDefinite(double[][] A) {
        int n = A.length;

        for (int k = 0; k < n; k++) {
            double sum = 0;
            for (int j = 0; j < k; j++) {
                sum += Math.pow(A[k][j], 2);
            }
            double diagonalElement = A[k][k] - sum;
            if (diagonalElement <= 0) {
                return false;
            }
        }

        return true;
    }

    // Phân tích Cholesky
    public static double[][] choleskyDecomposition(double[][] A) {
        int n = A.length;
        double[][] L = new double[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                double sum = 0;
                for (int k = 0; k < j; k++) {
                    sum += L[i][k] * L[j][k];
                }
                if (i == j) {
                    L[i][j] = Math.sqrt(A[i][i] - sum);
                } else {
                    L[i][j] = (A[i][j] - sum) / L[j][j];
                }
            }
        }

        return L;
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

    // Chuyển vị ma trận
    public static double[][] transpose(double[][] A) {
        int n = A.length;
        double[][] result = new double[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = A[j][i];
            }
        }

        return result;
    }
}