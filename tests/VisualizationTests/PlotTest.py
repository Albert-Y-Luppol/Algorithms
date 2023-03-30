import unittest

from src.Visualization.Plot import Plot
import numpy as np


class PlotTest(unittest.TestCase):
    def test_two_curves_1(self):
        Plot.two_curves(
            f1=lambda n: n ** 2,
            f2=lambda n: n * np.log(n),
        )

    def test_two_curves_2(self):
        Plot.two_curves(
            f1=lambda n: 5 ** np.log2(n),
            f2=lambda n: n ** 2,
        )

    def test_two_curves_3(self):
        Plot.two_curves(
            f1=lambda n: 5 ** np.log2(n),
            f2=lambda n: n ** 2,
            end_range=10**10,
        )

    def test_two_curves_4(self):
        Plot.two_curves(
            f1=lambda n: n ** 5,
            f2=lambda n: 2 ** (3 * np.log2(n)),
        )

    def test_two_curves_4(self):
        Plot.two_curves(
            f1=lambda n: n ** 5,
            f2=lambda n: 2 ** (3 * np.log2(n)),
            end_range=10 ** 10,
        )

    def test_two_curves_5(self):
        Plot.two_curves(
            f1=lambda n: np.log(n),
            f2=lambda n: n ** .5,
            end_range=10 ** 10,
        )

    def test_two_curves_6(self):
        Plot.two_curves(
            f1=lambda n: n * np.log2(n),
            f2=lambda n: 5 ** np.log2(n),
            end_range=10 ** 10,
        )

    def test_two_curves_7(self):
        Plot.two_curves(
            f1=lambda n: n ** 2,
            f2=lambda n: 2 ** n,
            end_range=10,
        )


if __name__ == '__main__':
    unittest.main()
