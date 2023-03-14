package org.DivideAndConquerParadigm;

public class OneDimension_ClosestPair extends ClosestPair<Integer>{

    @Override
    int _countDistance(Integer p1, Integer p2) {
        return Math.abs(p2 - p1);
    }

    @Override
    int _countSize(Integer p) {
        return p;
    }
}
