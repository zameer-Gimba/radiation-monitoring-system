from src.simulator import simulate_radiation_data
from src.detector import (
    detect_anomalies_zscore,
    detect_anomalies_ai,
    detect_anomalies_threshold
)
from src.visualization import plot_results_final


def main():
    data = simulate_radiation_data(
        n_points=200,
        save_path="data/simulated_radiation_data.csv"
    )

    # Default: engineering safety detection (aligned with visualization)
    anomalies = detect_anomalies_threshold(
        data,
        upper=0.5,
        lower=0.0
    )

    # Optional alternatives:
    # anomalies = detect_anomalies_ai(data)
    # anomalies = detect_anomalies_zscore(data)

    plot_results_final(
        data,
        anomalies,
        threshold_upper=0.5,
        threshold_lower=0.0
    )

    print(f"Total anomalies detected: {len(anomalies)}")


if __name__ == "__main__":
    main()
