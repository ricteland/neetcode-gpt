class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        value = init
        for iter in range(iterations):
            new_value = value - learning_rate*(2*value)
            value = new_value
        return round(value, 5)

