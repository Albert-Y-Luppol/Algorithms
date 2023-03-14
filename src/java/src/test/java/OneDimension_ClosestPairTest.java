import org.DivideAndConquerParadigm.OneDimension_ClosestPair;
import org.DivideAndConquerParadigm.Pair;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class OneDimension_ClosestPairTest {
    @Test
    void standardInput() {
        Integer points[] = {1, 3, 5, 9, 12, 2, 4, 6, 8};

        OneDimension_ClosestPair closestPair = new OneDimension_ClosestPair();
        Assertions.assertEquals(new Pair(1, 2), closestPair.findClosestPair(points));
    }

    @Test
    void standardInput2() {
        Integer points[] = {12, 6, 2245};

        OneDimension_ClosestPair closestPair = new OneDimension_ClosestPair();
        Assertions.assertEquals(new Pair(6, 12), closestPair.findClosestPair(points));
    }

    @Test
    void standardInput3() {
        Integer points[] = {11, 11, 12, 1, 2, 3, 4, 5, 6};

        OneDimension_ClosestPair closestPair = new OneDimension_ClosestPair();
        Assertions.assertEquals(new Pair(11, 11), closestPair.findClosestPair(points));
    }
}
