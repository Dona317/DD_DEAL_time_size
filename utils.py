import numpy as np

class Utils():

    @staticmethod
    def remove_outliers_iqr(data: list[float]) -> list[float]:
        if not data:
            return []

        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        return [x for x in data if lower_bound <= x <= upper_bound]
