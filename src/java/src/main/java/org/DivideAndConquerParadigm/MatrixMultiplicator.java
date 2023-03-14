package org.DivideAndConquerParadigm;

public class MatrixMultiplicator {

    /**
     * For squared matrixes only
     */
    public static int[][] strassenAlgorithm(int[][] X, int[][] Y) {
        if (X.length == 0 || X.length % 2 != 0
            || X[0].length == 0 || X[0].length % 2 != 0
            || Y.length == 0 || Y.length % 2 != 0
            || Y[0].length == 0 || Y[0].length % 2 != 0
            || X.length != X[0].length) {
            return standardAlgorithm(X, Y);
        }
        Squad<int[][]> ABCD = _splitMatrixTo4Pieces(X);
        Squad<int[][]> EFGH = _splitMatrixTo4Pieces(Y);


        int[][] P1 = strassenAlgorithm(ABCD.first(), _subMatrix(EFGH.second(), EFGH.forth()));
        int [][]P2 = strassenAlgorithm(_sumMatrix(ABCD.first(), ABCD.second()), EFGH.forth());
        int [][] P3 = strassenAlgorithm(_sumMatrix(ABCD.third(), ABCD.forth()), EFGH.first());
        int [][] P4 = strassenAlgorithm(ABCD.forth(), _subMatrix(EFGH.third(), EFGH.first()));
        int [][]P5 = strassenAlgorithm(_sumMatrix(ABCD.first(), ABCD.forth()), _sumMatrix(EFGH.first(), EFGH.forth()));
        int [][]P6 = strassenAlgorithm(_subMatrix(ABCD.second(), ABCD.forth()), _sumMatrix(EFGH.third(), EFGH.forth()));
        int [][]P7 = strassenAlgorithm(_subMatrix(ABCD.first(), ABCD.third()), _sumMatrix(EFGH.first(), EFGH.second()));

        int[][] resultA = _subMatrix(_sumMatrix(P5, P4, P6), P2);
        int[][] resultB = _sumMatrix(P1, P2);
        int[][] resultC = _sumMatrix(P3, P4);
        int[][] resultD = _subMatrix(_sumMatrix(P1, P5), P3, P7);

        return _join4Matrixes(resultA, resultB, resultC, resultD);
    }


    public static int[][] standardAlgorithm (int[][] X, int[][] Y) {
        if (X.length < 1 || X[0].length < 1 || Y.length < 1 || Y[0].length < 1) {
            return new int[0][0];
        }
        int [][] Z = new int[X.length][Y[0].length];
        for (int rowIndex = 0; rowIndex < X.length; rowIndex++) {
            for (int colIndex = 0; colIndex < Y[0].length; colIndex++) {
                int result = 0;
                for (int i = 0; i < Y.length; i++) {
                    result+= X[rowIndex][i] * Y[i][colIndex];
                }
                Z[rowIndex][colIndex] = result;
            }
        }
        return Z;
    }

    private static Squad<int[][]> _splitMatrixTo4Pieces (int[][] X) {
        int subRowLength = X.length / 2;
        int subColLength = X[0].length / 2;

        int[][] A = new int[subRowLength][subColLength];
        int[][] B = new int[subRowLength][subColLength];
        int[][] C = new int[subRowLength][subColLength];
        int[][] D = new int[subRowLength][subColLength];

        for (int row = 0; row < X.length; row++) {
            for (int col = 0; col < X[0].length; col++) {
                final boolean isTopSegments = row < subRowLength;
                final boolean isLeftSegments = col < subColLength;

                final int segmentIndex = isTopSegments
                        ? isLeftSegments ? 1 : 2
                        : isLeftSegments ? 3 : 4;

                switch (segmentIndex) {
                    case 1:
                        A[row][col] = X[row][col];
                        break;

                    case 2:
                        B[row][col - subColLength] = X[row][col];
                        break;

                    case 3:
                        C[row - subRowLength][col] = X[row][col];
                        break;

                    case 4:
                        D[row - subRowLength][col - subColLength] = X[row][col];
                        break;
                }
            }
        }

        return new Squad(A, B, C, D);
    }

    private static int[][] _join4Matrixes (int[][] A, int[][] B, int[][] C, int[][] D) {
        final int rows = A.length * 2;
        final int cols = A[0].length * 2;
        int[][] result = new int[rows][cols];

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                final boolean isTopSegments = row < rows / 2;
                final boolean isLeftSegments = col < cols / 2;

                final int segmentIndex = isTopSegments
                        ? isLeftSegments ? 1 : 2
                        : isLeftSegments ? 3 : 4;

                switch (segmentIndex) {
                    case 1:
                        result[row][col] = A[row][col];
                        break;

                    case 2:
                        result[row][col] = B[row][col - cols / 2];
                        break;

                    case 3:
                        result[row][col] = C[row - rows / 2][col];
                        break;

                    case 4:
                        result[row][col] = D[row - rows / 2][col - cols / 2];
                        break;
                }
            }
        }

        return result;
    }

    private static int[][] _sumMatrix (int [][] ...adds) {
        final int rows = adds[0].length;
        final int cols = adds[0][0].length;

        final int[][] result = new int [rows][cols];
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                result[row][col] = 0;
                for (int[][] M : adds) {
                    result[row][col]+= M[row][col];
                }
            }
        }
        return result;
    }

    private static int[][] _subMatrix (int [][] A, int [][] ...subs) {
        final int rows = A.length;
        final int cols = A[0].length;

        final int[][] result = new int [rows][cols];
        for (int row = 0; row < A.length; row++) {
            for (int col = 0; col < A[0].length; col++) {
                result[row][col] = A[row][col];
                for (int [][] M : subs) {
                    result[row][col]-= M[row][col];
                }
            }
        }
        return result;
    }

    private static void _printMatrix(int[][] M) {
        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[i].length; j++) {
                System.out.print(M[i][j] + "     ");
            }
            System.out.println();
        }
    }
}
