package NoiSuy;// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,

// then press Enter. You can now see whitespace characters in your code.

import GiaiHePT.GaussJordanSolver;

import java.lang.Math;
import java.util.ArrayList;
import java.util.Scanner;

public class NoiSuySpline {
    private static final double pi = Math.PI;
    public static int num;
    public static ArrayList<Double> a = new ArrayList<>();

    public static double f(double x) {
        return Math.sin(x) * Math.exp(2 * x);
    }

    public static double[] calcCoef() {
        int size = (num - 1) * 4;
        double[][] arr = new double[size][size];
        double[] b = new double[size];
        double[] x;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                arr[i][j] = 0.0;
            }
        }
        int index = 0;
        int index2 = 0;
        while (index2 < size) {
            if (index == 0) {
                arr[index2][index * 4] = Math.pow(a.get(index), 3);
                arr[index2][index * 4 + 1] = Math.pow(a.get(index), 2);
                arr[index2][index * 4 + 2] = Math.pow(a.get(index), 1);
                arr[index2][index * 4 + 3] = Math.pow(a.get(index), 0);
                b[index2] = f(a.get(index));
            } else if (index == num - 1) {
                arr[index2][index * 4 - 4] = Math.pow(a.get(index), 3);
                arr[index2][index * 4 - 3] = Math.pow(a.get(index), 2);
                arr[index2][index * 4 - 2] = Math.pow(a.get(index), 1);
                arr[index2][index * 4 - 1] = Math.pow(a.get(index), 0);
                b[index2] = f(a.get(index));
            } else if (index > 0 && index < num - 1) {
                for (int i = 0; i < 2; i++) {
                    arr[index2][(index - 1) * 4 + i * 4] = Math.pow(a.get(index), 3);
                    arr[index2][(index - 1) * 4 + i * 4 + 1] = Math.pow(a.get(index), 2);
                    arr[index2][(index - 1) * 4 + i * 4 + 2] = Math.pow(a.get(index), 1);
                    arr[index2][(index - 1) * 4 + i * 4 + 3] = Math.pow(a.get(index), 0);
                    b[index2] = f(a.get(index));
                    if (i == 0)
                        index2++;
                }
            }

            if (index2 == size / 2) {
                arr[index2][0] = 6 * a.get(0);
                arr[index2][1] = 2;
                b[index2] = 4;
            }
            if (index2 == size / 2 + 1) {
                arr[index2][(num - 2) * 4] = 6 * a.get(num - 1);
                arr[index2][(num - 2) * 4 + 1] = 2;
                b[index2] = 3 * Math.exp(pi);
            }
            ;
            if (index2 > size / 2 + 1 && index2 < size) {
                for (int i = 0; i < num - 2; i++) {
                    arr[index2][i * 4] = 3 * Math.pow(a.get(i + 1), 2);
                    arr[index2][i * 4 + 1] = 2 * Math.pow(a.get(i + 1), 1);
                    arr[index2][i * 4 + 2] = 1 * Math.pow(a.get(i + 1), 1);
                    arr[index2][(i + 1) * 4] = -3 * Math.pow(a.get(i + 1), 2);
                    arr[index2][(i + 1) * 4 + 1] = -2 * Math.pow(a.get(i + 1), 1);
                    arr[index2][(i + 1) * 4 + 2] = -1 * Math.pow(a.get(i + 1), 1);
                    b[index2] = 0;
                    index2++;
                    arr[index2][i * 4] = 6 * Math.pow(a.get(i + 1), 1);
                    arr[index2][i * 4 + 1] = 2;
                    arr[index2][(i + 1) * 4] = -6 * Math.pow(a.get(i + 1), 1);
                    arr[index2][(i + 1) * 4 + 1] = -2;
                    b[index2] = 0;
                    index2++;
                }
                continue;
            }
            index2++;
            if (index < num)
                index++;
        }

        x = solve(arr, b);
        return x;
    }

    public static void printFx() {
        double x[] = calcCoef();
        for (int i = 0; i < num - 1; i++) {
            System.out.println("F" + i + "(x) = " + x[i * 4] + "*x^3 + " + x[i * 4 + 1] + "*x^2 + " + x[i * 4 + 2]
                    + "*x + " + x[i * 4 + 3]);
        }
    }

    public static double calcFx(double val) {
        double x[] = calcCoef();
        double result = 0;
        for (int i = 0; i < num - 1; i++) {
            if (val >= a.get(i) && val <= a.get(i + 1)) {
                result = x[i * 4] * Math.pow(val, 3) + x[i * 4 + 1] * Math.pow(val, 2) + x[i * 4 + 2] * Math.pow(val, 1)
                        + x[i * 4 + 3] * Math.pow(val, 0);
            }
        }
        return result;
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

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.println("Nhap lan luot 2 moc trai phai khoang xac dinh cua
        // f(x):");
        double left = 0;
        double right = pi / 2;
        // System.out.println("Nhap so diem moc cach deu: ");
        num = 50;
        a = new ArrayList<>();
        for (int i = 0; i < num; i++) {
            double val = left + (right - left) / (num - 1) * i;
            a.add(val);
        }
        System.out.println("Da thuc noi suy cua f(x) theo phuong phap Lagrange voi " + num + " diem moc cach deu:");
        printFx();
        // System.out.println("Nhap gia tri cua x:");
        double x = pi / 200;
        double result = calcFx(x);
        System.out.println("Gia tri cua f(x) tinh boi da thuc noi suy Spline la:");
        System.out.println(result);
        System.out.println("Sai so cua bieu thuc la:");
        System.out.println(Math.abs(f(x) - result));
        System.out.println("Gia tri chinh xac cua f(x) la: " + f(x));
    }
}