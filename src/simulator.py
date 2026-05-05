import numpy as np
import pandas as pd

def simulate_radiation_data(n_points=200, save_path=None):
    np.random.seed(42)

    time = np.arange(n_points)

    # Normal radiation levels (safe ~0.1–0.3 mSv/h)
    radiation = np.random.normal(loc=0.2, scale=0.05, size=n_points)

    # Radiation spike (leak event)
    spike_start, spike_end = 80, 100
    radiation[spike_start:spike_end] = np.random.normal(
        loc=2.5, scale=0.3, size=(spike_end - spike_start)
    )

    # Gradual containment degradation
    for i in range(120, n_points):
        radiation[i] += (i - 120) * 0.01

    data = pd.DataFrame({
        "time": time,
        "radiation": radiation
    })

    if save_path:
        data.to_csv(save_path, index=False)

    return data
