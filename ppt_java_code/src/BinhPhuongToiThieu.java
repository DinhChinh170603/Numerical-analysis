import java.util.Scanner;

public class BinhPhuongToiThieu {
    public static double[] solve(double[][] coefficients, double[] constants) {
        int rowCount = coefficients.length;
        int columnCount = coefficients[0].length;

        // Tạo ma trận mở rộng gồm ma trận hệ số và ma trận hằng số
        double[][] augmentedMatrix = new double[rowCount][columnCount + 1];
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < columnCount; j++) {
                augmentedMatrix[i][j] = coefficients[i][j];
            }
            augmentedMatrix[i][columnCount] = constants[i];
        }

        // Áp dụng phương pháp Gauss-Jordan
        for (int pivot = 0; pivot < rowCount; pivot++) {
            // Tìm hàng có giá trị tuyệt đối lớn nhất trong cột pivot
            int maxRowIndex = pivot;
            double maxRowValue = Math.abs(augmentedMatrix[pivot][pivot]);
            for (int i = pivot + 1; i < rowCount; i++) {
                double currentRowValue = Math.abs(augmentedMatrix[i][pivot]);
                if (currentRowValue > maxRowValue) {
                    maxRowValue = currentRowValue;
                    maxRowIndex = i;
                }
            }

            // Hoán đổi hàng có giá trị tuyệt đối lớn nhất lên đầu cột pivot
            double[] temp = augmentedMatrix[pivot];
            augmentedMatrix[pivot] = augmentedMatrix[maxRowIndex];
            augmentedMatrix[maxRowIndex] = temp;

            // Chia hàng pivot cho phần tử pivot để đưa phần tử pivot về 1
            double pivotValue = augmentedMatrix[pivot][pivot];
            for (int j = pivot; j < columnCount + 1; j++) {
                augmentedMatrix[pivot][j] /= pivotValue;
            }

            // Loại bỏ các phần tử trong cột pivot bên dưới phần tử pivot
            for (int i = 0; i < rowCount; i++) {
                if (i != pivot) {
                    double factor = augmentedMatrix[i][pivot];
                    for (int j = pivot; j < columnCount + 1; j++) {
                        augmentedMatrix[i][j] -= factor * augmentedMatrix[pivot][j];
                    }
                }
            }
        }

        // Trích xuất nghiệm từ ma trận mở rộng
        double[] solution = new double[rowCount];
        for (int i = 0; i < rowCount; i++) {
            solution[i] = augmentedMatrix[i][columnCount];
        }

        return solution;
    }
    public static double calculateFunction(double x) {
//        return Math.pow(Math.E, - x * x) / Math.pow(2 * Math.PI, -0.5);
        return Math.sin(x);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap a: ");
        double a = scanner.nextDouble();
        System.out.print("Nhap b: ");
        double b = scanner.nextDouble();
        System.out.print("Nhap n: ");
        int n = scanner.nextInt(); // n la so diem moc
        double h = (b - a) / n;
        double[] x = new double[n + 1];
        for (int i = 0; i <= n; i++) {
            x[i] = a + i * h;
        }
        System.out.print("Nhap bac cua phuong trinh: ");
        int lv = scanner.nextInt(); // lv la bac cua phuong trinh
        double[][] matrix = new double[lv + 1][lv + 1];
        for (int i = 0; i <= lv; i++) {
            for (int j = 0; j <= lv; j++) {
                double temp = 0;
                for (int k = 0; k <= n; k++) {
                    temp += Math.pow(x[k], i + j);
                }
                matrix[i][j] = temp;
            }
        }
        double[] y = new double[lv + 1];
        for (int i = 0; i <= lv; i++) {
            double temp = 0;
            for (int j = 0; j <= n; j++) {
                temp += Math.pow(x[j], i) * calculateFunction(x[j]);
            }
            y[i] = temp;
        }
        double[] result = solve(matrix, y);
        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }
        // fx = result[0] + result[1] * x + result[2] + x ^ 2 + ...
    }
}
