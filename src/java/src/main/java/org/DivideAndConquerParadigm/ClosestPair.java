package org.DivideAndConquerParadigm;

import java.util.ArrayList;
import java.util.Arrays;

public abstract class ClosestPair<T> {
    public Pair<T, T> findClosestPair(T[] points) {
        final T[] sortedPoints = _sort(points);

        T p1 = sortedPoints[0];
        T p2 = sortedPoints[1];

        int minDistance = _countDistance(p1, p2);
        for (int i = 2; i < points.length; i++) {
            final int distance = _countDistance(sortedPoints[i], sortedPoints[i - 1]);
            if (minDistance > distance) {
                minDistance = distance;
                p1 = sortedPoints[i - 1];
                p2 = sortedPoints[i];
            }
        }

        return new Pair(p1, p2);
    }

    private T[] _sort(T[] points) {
        if (points.length > 1) {
            Pair<T[], T[]> splitArray = _split(points);
            final T[] x = _sort(splitArray.first());
            final T[] y = _sort(splitArray.second());

            final T[] sortedArray = _merge(x, y);
            return  sortedArray;
        } else {
            return points;
        }
    }

    private Pair<T[], T[]> _split(T[] z) {
        final ArrayList<T> x = new ArrayList<T>();
        final ArrayList<T> y = new ArrayList<T>();

        for (int i = 0; i < z.length; i++) {
            if (i < z.length / 2) x.add(z[i]) ;
            else y.add(z[i]);
        }

        return new Pair(x.toArray(), y.toArray());
    }

    protected T[] _merge(T[] x, T[] y) {
        final ArrayList<T> z = new ArrayList<T>();
        int i = 0;
        int j = 0;
        for (int n = 0; n < x.length + y.length; n++) {
            if (i == x.length) {
                z.add(y[j]);
                j++;
            } else if (j == y.length) {
                z.add(x[i]);
                i++;
            } else if (_countSize(x[i]) < _countSize(y[j])) {
                z.add(x[i]);
                i++;
            } else {
                z.add(y[j]);
                j++;
            }
        }
        return (T[]) z.toArray();
    }

    abstract int _countDistance(T p1, T p2);

    abstract int _countSize(T p);
}
