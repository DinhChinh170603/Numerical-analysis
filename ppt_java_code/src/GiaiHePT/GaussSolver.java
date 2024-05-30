package GiaiHePT;

public class GaussSolver {

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

        // Tạo ma trận mở rộng bao gồm ma trận A và vector b
        double[][] augmentedMatrix = new double[n][n + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                augmentedMatrix[i][j] = A[i][j];
            }
            augmentedMatrix[i][n] = b[i];
        }

        // Áp dụng phương pháp Gauss
        for (int pivot = 0; pivot < n - 1; pivot++) {
            // Tìm hàng chứa phần tử chính hợp lệ không bằng 0
            int nonZeroRow = -1;
            for (int i = pivot; i < n; i++) {
                if (augmentedMatrix[i][pivot] != 0) {
                    nonZeroRow = i;
                    break;
                }
            }

            // Hoán đổi hàng
            if (nonZeroRow != -1) {
                double[] temp = augmentedMatrix[pivot];
                augmentedMatrix[pivot] = augmentedMatrix[nonZeroRow];
                augmentedMatrix[nonZeroRow] = temp;
            } else {
                // Hệ phương trình vô nghiệm hoặc có vô số nghiệm
                return null;
            }

            // Loại bỏ phần tử chính hợp lệ khỏi các hàng dưới
            for (int i = pivot + 1; i < n; i++) {
                double factor = augmentedMatrix[i][pivot] / augmentedMatrix[pivot][pivot];
                for (int j = pivot; j <= n; j++) {
                    augmentedMatrix[i][j] -= factor * augmentedMatrix[pivot][j];
                }
            }
        }

        // Tạo mảng nghiệm
        double[] solution = new double[n];

        // Lặp lại từ hàng cuối cùng đến hàng đầu tiên để tìm nghiệm
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0;
            for (int j = i + 1; j < n; j++) {
                sum += augmentedMatrix[i][j] * solution[j];
            }
            solution[i] = (augmentedMatrix[i][n] - sum) / augmentedMatrix[i][i];
        }

        return solution;
    }
}