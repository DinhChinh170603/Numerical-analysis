package GiaiHePT;

import java.util.Arrays;

public class GaussSeidelSolver {
    private static final double EPSILON = 1e-3; // Độ chính xác

    public static double[] solve(double[][] coefficients, double[] constants) {
        int n = coefficients.length; // Số lượng phương trình
        double[] guess = new double[n]; // Giả định ban đầu

        double[] previousGuess;
        double[] error = new double[n];
        int iteration = 0;

        do {
            previousGuess = Arrays.copyOf(guess, n); // Sao chép giả định trước đó

            for (int i = 0; i < n; i++) {
                double sum = constants[i];

                for (int j = 0; j < n; j++) {
                    if (j != i) {
                        sum -= coefficients[i][j] * guess[j];
                    }
                }

                guess[i] = sum / coefficients[i][i];
                error[i] = Math.abs(guess[i] - previousGuess[i]);
            }

            iteration++;
        } while (maxError(error) > EPSILON);

        System.out.println("Số lần lặp: " + iteration);

        return guess;
    }

    private static double maxError(double[] error) {
        double max = error[0];

        for (int i = 1; i < error.length; i++) {
            if (error[i] > max) {
                max = error[i];
            }
        }

        return max;
    }

    public static void main(String[] args) {
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

        double[] solution = solve(A, b);

        System.out.println("Nghiệm:");
        for (int i = 0; i < solution.length; i++) {
            System.out.printf("x%d = %.6f\n", i + 1, solution[i]);
        }
    }
}
