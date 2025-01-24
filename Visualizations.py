import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set_theme(style="whitegrid")

# Visualization 1: Topic-wise accuracy for the current quiz
def plot_topic_accuracy(current_analysis):
    plt.figure(figsize=(8, 5))
    sns.barplot(
        x=current_analysis.index,
        y=current_analysis["Accuracy"],
        palette="viridis",
    )
    plt.title("Topic-wise Accuracy in Current Quiz", fontsize=14)
    plt.xlabel("Topics", fontsize=12)
    plt.ylabel("Accuracy (%)", fontsize=12)
    plt.ylim(0, 100)
    plt.axhline(y=70, color="red", linestyle="--", label="Weakness Threshold (70%)")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Visualization 2: Historical topic performance trends
def plot_historical_trends(historical_trends):
    plt.figure(figsize=(8, 5))
    topics = list(historical_trends.keys())
    accuracies = list(historical_trends.values())
    sns.lineplot(x=topics, y=accuracies, marker="o", color="blue")
    plt.title("Historical Topic Performance Trends", fontsize=14)
    plt.xlabel("Topics", fontsize=12)
    plt.ylabel("Average Accuracy (%)", fontsize=12)
    plt.ylim(0, 100)
    plt.axhline(y=70, color="orange", linestyle="--", label="Weakness Threshold (70%)")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Visualization 3: Combined weak areas
def plot_combined_weak_areas(current_analysis, historical_trends):
    combined = pd.DataFrame({
        "Current Accuracy": current_analysis["Accuracy"],
        "Historical Accuracy": [historical_trends.get(f"{topic} Accuracy", 0) for topic in current_analysis.index]
    })
    combined["Topic"] = current_analysis.index
    combined_melted = combined.melt(id_vars="Topic", var_name="Type", value_name="Accuracy")

    plt.figure(figsize=(10, 6))
    sns.barplot(x="Topic", y="Accuracy", hue="Type", data=combined_melted, palette="coolwarm")
    plt.title("Current vs. Historical Accuracy", fontsize=14)
    plt.xlabel("Topics", fontsize=12)
    plt.ylabel("Accuracy (%)", fontsize=12)
    plt.ylim(0, 100)
    plt.axhline(y=70, color="red", linestyle="--", label="Weakness Threshold (70%)")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Plotting the visualizations
plot_topic_accuracy(current_quiz_analysis)
plot_historical_trends(historical_trends)
plot_combined_weak_areas(current_quiz_analysis, historical_trends)
