import numpy as np
random_values = np.random.rand(100)
normal_values = (random_values - np.min(random_values)) / (np.max(random_values) - np.min(random_values))
print(normal_values)