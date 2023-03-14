import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.DivideAndConquerParadigm.Sorter;

import java.util.Arrays;
import java.util.List;

public class SorterTest {
    @Test
    void standardInput() {
        List<Integer> input = Arrays.asList(3, 4, 6, 2, 1, 5, 9, 8, 7);
        List<Integer> expectedOutput  = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);

        Assertions.assertArrayEquals(expectedOutput.toArray(), Sorter.mergeSort(input).toArray());
    }

    @Test
    void emptyInput() {
        List<Integer> input = Arrays.asList();
        List<Integer> expectedOutput  = Arrays.asList();

        Assertions.assertArrayEquals(expectedOutput.toArray(), Sorter.mergeSort(input).toArray());
    }

    @Test
    void duplicatesInput() {
        List<Integer> input = Arrays.asList(4, 2, 3, 2, 3, 4, 1, 3, 0, 4, 4, -1);
        List<Integer> expectedOutput  = Arrays.asList(-1, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4);

        Assertions.assertArrayEquals(expectedOutput.toArray(), Sorter.mergeSort(input).toArray());
    }
}
