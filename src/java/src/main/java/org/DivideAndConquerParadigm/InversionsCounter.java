package org.DivideAndConquerParadigm;

import java.util.ArrayList;
import java.util.List;

record PairL<T>(long first, T second) {
}
public class InversionsCounter {
    public static long countNumberOfInversions(List<Integer> arr) {
        return _countInversionsAndSort(arr).first();
    }

    private static PairL<List<Integer>> _countInversionsAndSort(List<Integer> arr) {
        if (arr.size() < 2) return  new PairL(0, arr);

        List<Integer> leftSubArray = new ArrayList();
        List<Integer> rightSubArray = new ArrayList();

        for(int i = 0; i < arr.size(); i++) {
            if (i < arr.size() / 2) leftSubArray.add(arr.get(i));
            else rightSubArray.add(arr.get(i));
        }

        PairL<List<Integer>> leftCountAndSort = _countInversionsAndSort(leftSubArray);
        PairL<List<Integer>> rightCountAndSort = _countInversionsAndSort(rightSubArray);

        long leftCount = leftCountAndSort.first();
        List<Integer> leftArr = leftCountAndSort.second();

        long rightCount = rightCountAndSort.first();
        List<Integer> rightArr = rightCountAndSort.second();

        List<Integer> sortedArr = new ArrayList();
        long splitCount;
        int leftI, rightI;
        splitCount = leftI = rightI = 0;

        for(int n = 0; n < arr.size(); n++) {
            if (leftI == leftArr.size()) {
                sortedArr.add(rightArr.get(rightI));
                rightI++;
            } else if (rightI == rightArr.size()) {
                sortedArr.add(leftArr.get(leftI));
                leftI++;
            } else if (leftArr.get(leftI) > rightArr.get(rightI)) {
                sortedArr.add(rightArr.get(rightI));
                rightI++;
                splitCount += leftArr.size() - leftI;
            } else {
                sortedArr.add(leftArr.get(leftI));
                leftI++;
            }
        }

        return new PairL(splitCount + leftCount + rightCount, sortedArr);
    }
}
