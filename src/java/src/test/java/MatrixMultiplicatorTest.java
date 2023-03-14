import java.util.Random;
import org.DivideAndConquerParadigm.MatrixMultiplicator;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class MatrixMultiplicatorTest {
    @Test
    void standardAlgorithm_standardInput() {
        int[][] A = new int[2][2];
        int[][] B = new int[2][2];
        int[][] R = new int[2][2];

        A[0][0] = 1;
        A[0][1] = 2;
        A[1][0] = 3;
        A[1][1] = 4;

        B[0][0] = 5;
        B[0][1] = 6;
        B[1][0] = 7;
        B[1][1] = 8;

        R[0][0] = 19;
        R[0][1] = 22;
        R[1][0] = 43;
        R[1][1] = 50;

        Assertions.assertArrayEquals(R, MatrixMultiplicator.standardAlgorithm(A, B));
    }

    @Test
    void standardAlgorithm_input2x3() {
        int[][] A = new int[2][3];
        int[][] B = new int[3][2];
        int[][] R = new int[2][2];

        A[0][0] = 1;
        A[0][1] = 2;
        A[0][2] = 2;
        A[1][0] = 3;
        A[1][1] = 4;
        A[1][2] = 2;

        B[0][0] = 5;
        B[0][1] = 6;
        B[1][0] = 7;
        B[1][1] = 8;
        B[2][0] = 7;
        B[2][1] = 8;

        R[0][0] = 33;
        R[0][1] = 38;
        R[1][0] = 57;
        R[1][1] = 66;

        Assertions.assertArrayEquals(R, MatrixMultiplicator.standardAlgorithm(A, B));
    }

    @Test
    void standardAlgorithm_emptyInput() {
        int[][] A = new int[0][0];
        int[][] B = new int[0][0];
        int[][] R = new int[0][0];

        Assertions.assertArrayEquals(R, MatrixMultiplicator.standardAlgorithm(A, B));
    }

    @Test
    void strassenAlgorithm_emptyInput() {
        int[][] A = new int[0][0];
        int[][] B = new int[0][0];
        int[][] R = new int[0][0];

        Assertions.assertArrayEquals(R, MatrixMultiplicator.strassenAlgorithm(A, B));
    }

    @Test
    void strassenAlgorithm_2x2() {
        final int[][] A = _randomMatrixGenerator(2, 2);
        final int[][] B = _randomMatrixGenerator(2, 2);

        final int[][] result = MatrixMultiplicator.strassenAlgorithm(A, B);
        final int[][] R = MatrixMultiplicator.standardAlgorithm(A, B);

        Assertions.assertArrayEquals(R, result);
    }

    @Test
    void strassenAlgorithm_3x3() {
        final int[][] A = _randomMatrixGenerator(3, 3);
        final int[][] B = _randomMatrixGenerator(3, 3);

        final int[][] result = MatrixMultiplicator.strassenAlgorithm(A, B);
        final int[][] R = MatrixMultiplicator.standardAlgorithm(A, B);

        Assertions.assertArrayEquals(R, result);
    }

    @Test
    void strassenAlgorithm_4x4() {
        final int[][] A = _randomMatrixGenerator(4, 4);
        final int[][] B = _randomMatrixGenerator(4, 4);

        final int[][] result = MatrixMultiplicator.strassenAlgorithm(A, B);
        final int[][] R = MatrixMultiplicator.standardAlgorithm(A, B);

        Assertions.assertArrayEquals(R, result);
    }

    @Test
    void strassenAlgorithm_8x8() {
        final int[][] A = _randomMatrixGenerator(8, 8);
        final int[][] B = _randomMatrixGenerator(8, 8);

        final int[][] result = MatrixMultiplicator.strassenAlgorithm(A, B);
        final int[][] R = MatrixMultiplicator.standardAlgorithm(A, B);

        Assertions.assertArrayEquals(R, result);
    }

    @Test
    void strassenAlgorithm_4x6() {
        final int[][] A = _randomMatrixGenerator(4, 6);
        final int[][] B = _randomMatrixGenerator(6, 4);

        final int[][] result = MatrixMultiplicator.strassenAlgorithm(A, B);
        final int[][] R = MatrixMultiplicator.standardAlgorithm(A, B);

        Assertions.assertArrayEquals(R, result);
    }

    @Test
    void strassenAlgorithm_10x8() {
        final int[][] A = _randomMatrixGenerator(10, 8);
        final int[][] B = _randomMatrixGenerator(8, 10);

        final int[][] result = MatrixMultiplicator.strassenAlgorithm(A, B);
        final int[][] R = MatrixMultiplicator.standardAlgorithm(A, B);

        Assertions.assertArrayEquals(R, result);
    }

    @Test
    void strassenAlgorithm_32x32() {
        final int[][] A = _randomMatrixGenerator(32, 32);
        final int[][] B = _randomMatrixGenerator(32, 32);

        final int[][] result = MatrixMultiplicator.strassenAlgorithm(A, B);
        final int[][] R = MatrixMultiplicator.standardAlgorithm(A, B);

        Assertions.assertArrayEquals(R, result);
    }

    private static int[][] _randomMatrixGenerator(int rows, int cols) {
        int[][] result = new int[rows][cols];
        Random rand = new Random();

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                result[row][col] = rand.nextInt(1000);
            }
        }

        return  result;
    }

    private static int[][] _randomMatrixGenerator(int rows, int cols, int bound) {
        int[][] result = new int[rows][cols];
        Random rand = new Random();

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                result[row][col] = rand.nextInt(bound);
            }
        }

        return result;
    }
}
