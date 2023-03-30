import matplotlib.pyplot as plt
import numpy as np
from typing import Callable
from dill.source import getsource


class Plot:
    @staticmethod
    def two_curves(
            f1: Callable[[int], int],
            f2: Callable[[int], int],
            start_range: int = 1,
            end_range: int = 10 ** 3,
    ) -> None:
        n = np.linspace(start_range, end_range)
        plt.plot(n, f1(n), label=getsource(f1))
        plt.plot(n, f2(n), label=getsource(f2))
        plt.legend(loc='upper left')
        plt.show()
