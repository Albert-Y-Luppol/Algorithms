import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.DivideAndConquerParadigm.InversionsCounter;
import org.utils.ReadTextFile;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class InversionsCounterTest {
    @Test
    void countNumberOfInversions_0() {
        List<Integer> input = Arrays.asList(1, 3, 2);
        int expectedOutput  = 1;

        Assertions.assertEquals(expectedOutput, InversionsCounter.countNumberOfInversions(input));
    }

    @Test
    void countNumberOfInversions_1() {
        List<Integer> input = Arrays.asList(1, 3, 2, 4, 6, 5);
        int expectedOutput  = 2;
        System.out.println(InversionsCounter.countNumberOfInversions(input));
        Assertions.assertEquals(expectedOutput, InversionsCounter.countNumberOfInversions(input));
    }

    @Test
    void countNumberOfInversions_2() {
        ArrayList<String> inputFile = ReadTextFile.getValues("src/test/resources/InversionsCount.txt");
        final List<Integer> input = new ArrayList();
        for (int i = 0; i < inputFile.size(); i++) {
            input.add(Integer.parseInt(inputFile.get(i).trim()));
        }

        long expectedOutput = Long.valueOf("2407905288");

        Assertions.assertEquals(expectedOutput, InversionsCounter.countNumberOfInversions(input));
    }

    @Test
    void countNumberOfInversions_3() {
        List<Integer> input = Arrays.asList(3, 2, 1);
        int expectedOutput  = 3;

        Assertions.assertEquals(expectedOutput, InversionsCounter.countNumberOfInversions(input));
    }
}
