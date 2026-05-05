import matplotlib.pyplot as plt

def plot_results_final(data, anomalies, threshold_upper=0.5, threshold_lower=0.0):
    if data.empty:
        print("Warning: Data is empty.")
        return

    plt.figure(figsize=(12, 6))

    # Radiation line
    plt.plot(
        data["time"],
        data["radiation"],
        label="Radiation Level",
        color="#2c3e50",
        linewidth=1.5,
        alpha=0.7,
        zorder=1
    )

    # Threshold lines
    plt.axhline(y=threshold_upper, color="#c0392b", linestyle="--",
                linewidth=1.5, label=f"Upper Limit ({threshold_upper} mSv/h)", zorder=2)

    plt.axhline(y=threshold_lower, color="#c0392b", linestyle="--",
                linewidth=1.5, label=f"Lower Limit ({threshold_lower} mSv/h)", zorder=2)

    # Safe zone
    plt.fill_between(
        data["time"],
        threshold_lower,
        threshold_upper,
        color="#27ae60",
        alpha=0.1,
        label="Safe Operating Range"
    )

    # Anomalies
    if anomalies is not None and len(anomalies) > 0:
        plt.scatter(
            data["time"].iloc[anomalies],
            data["radiation"].iloc[anomalies],
            label="Anomalies Detected",
            color="#e74c3c",
            edgecolor="black",
            s=80,
            zorder=4
        )

    plt.xlabel("Time")
    plt.ylabel("Radiation Level (mSv/h)")
    plt.title("Radiation Monitoring: Containment & Safety Thresholds", fontweight="bold")

    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()
