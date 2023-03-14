package org.DivideAndConquerParadigm;

import java.util.ArrayList;
import java.util.List;

public class Sorter {
    public static<T extends Integer> List<T> mergeSort (List<T> listToSort){ // O(2n log(n))
        if (listToSort.size() <= 1) return listToSort;

        Pair<List<T>, List<T>> pair = _splitList(listToSort); // O(n)
        List<T> first = mergeSort(pair.first());
        List<T> second = mergeSort(pair.second());

        return _mergeSortedLists(first, second, listToSort.size()); // O(n)
    }


    private static<T> Pair<List<T>, List<T>> _splitList(List<T> list) { // O(n)
        List<T> first = new ArrayList<T>();
        List<T> second = new ArrayList<T>();

        for (int i = 0; i < list.size(); i++) {
            if (i < list.size() / 2) first.add(list.get(i));
            else second.add(list.get(i));
        }

        return new Pair<List<T>, List<T>>(first, second);
    }

    private static<T extends Integer> List<T> _mergeSortedLists(List<T> first, List<T> second, int n) { // O(n)
        List<T> result = new ArrayList();
        int i = 0;
        int j = 0;

        for (int index = 0; index < n; index++) {
            if (i ==  first.size()) {
                result.add(second.get(j));
                j++;
            } else if (j == second.size()) {
                result.add(first.get(i));
                i++;
            } else if (Integer.valueOf(first.get(i)) > Integer.valueOf(second.get(j))) {
                result.add(second.get(j));
                j++;
            } else {
                result.add(first.get(i));
                i++;
            }
        }

        return result;
    }
}
