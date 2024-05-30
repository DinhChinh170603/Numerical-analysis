package GiaTriRieng;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class MaximumEntryScaling {
    public static int n;
    public static double[] calcAx(double A[][], double x[]) {
        double[] result = new double[n];
        int len = x.length;
        for (int i = 0; i < n; i++) {
            double value = 0;
            for (int j = 0; j < n; j++) {
                value += A[i][j] * x[j];
            }
            result[i] = value;
        }
        return result;
    }

    public static double calcLanda(double Ax[], double x[]) {
        double result = 0;
        double deno = 0;
        for (int i = 0; i < n; i++) {
            result += Ax[i]*x[i];
        }
        for (int i = 0; i < n; i++) {
            deno += Math.pow(x[i], 2);
        }
        return result / deno;
    }

    public static double[] calcX(double[] Ax) {
        double deno = findMax(Ax);
        for (int i = 0; i < n; i ++) {
            Ax[i] = Ax[i] / deno;
        }
        return Ax;
    }

    public static double findMax(double[] arr) {
        double max = arr[0];
        //Loop through the array
        for (int i = 0; i < arr.length; i++) {
            //Compare elements of array with max
            if(arr[i] > max)
                max = arr[i];
        }
        return max;
    }


    public static void main(String[] args) {
        double[][] A = {{3, 2, 2},
                {2, 2, 0},
                {2, 0, 4}};
        double[] x = {1, 1, 1};
        n = x.length;
        double[] Ax = calcAx(A, x);
        double[] tempAx = calcAx(A, x);
        for (int i = 0; i < 10; i++) {
            x = calcX(tempAx);
            tempAx = calcAx(A, x);
            System.out.print("Ax" + (i+1) + " = [ ");
            for (int j = 0; j < n; j++) {
                System.out.print(tempAx[j] + " ");
            }
            System.out.println("]");
            double landa = calcLanda(tempAx, x);

            System.out.println("Landa" + (i + 1) + " = " + landa);
            System.out.println();
        }
    }

}