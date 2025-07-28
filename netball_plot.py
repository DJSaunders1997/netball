# netball_plot.py
import pandas as pd
import matplotlib.pyplot as plt
from league_data import get_all_league_data # Import the new function

def load_all_data() -> pd.DataFrame:
    """
    Loads all matchday data by calling the function from league_data.py.

    Returns:
        pd.DataFrame: Combined DataFrame with data from all matchdays.
    """
    return get_all_league_data()


def plot_cumulative_metrics(df: pd.DataFrame, metrics: list[str], metric_labels: dict) -> None:
    """
    Plots cumulative metrics over time for all teams and saves them as PNGs.
    """
    for metric in metrics:
        plt.figure(figsize=(14, 8))
        pivot_df = df.pivot_table(index='Date', columns='Team', values=metric)

        for team in pivot_df.columns:
            # Highlight "Pivot Grigio"
            if team == "Pivot Grigio":
                plt.plot(
                    pivot_df.index,
                    pivot_df[team],
                    marker='o',
                    label=team,
                    color='red',
                    linewidth=3,
                    zorder=10
                )
            else:
                plt.plot(
                    pivot_df.index,
                    pivot_df[team],
                    marker='o',
                    label=team,
                    alpha=0.5
                )

        plt.title(f'Cumulative {metric_labels.get(metric, metric)} Over Time', fontsize=14)
        plt.ylabel(f'Cumulative {metric_labels.get(metric, metric)}')
        plt.xlabel('Date')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(f"Cumulative_{metric.replace(' ', '_')}_over_time.png")
        plt.close()


def plot_per_game_metrics(df: pd.DataFrame, metrics: list[str], metric_labels: dict) -> None:
    """
    Plots per-game change for all metrics over time and saves them as PNGs.
    """
    df_sorted = df.sort_values(by=['Team', 'Date']).copy()
    for metric in metrics:
        plt.figure(figsize=(14, 8))
        
        # Calculate the per-game change
        df_sorted[f'{metric} In Each Game'] = df_sorted.groupby('Team')[metric].diff().fillna(0)
        
        pivot_change = df_sorted.pivot_table(index='Date', columns='Team', values=f'{metric} In Each Game')

        for team in pivot_change.columns:
            # Highlight "Pivot Grigio"
            if team == "Pivot Grigio":
                plt.plot(
                    pivot_change.index,
                    pivot_change[team],
                    marker='o',
                    label=team,
                    color='red',
                    linewidth=3,
                    zorder=10
                )
            else:
                plt.plot(
                    pivot_change.index,
                    pivot_change[team],
                    marker='o',
                    label=team,
                    alpha=0.5
                )

        plt.title(f'{metric_labels.get(metric, metric)} In Each Game Over Time', fontsize=14)
        plt.ylabel(f'{metric_labels.get(metric, metric)} In Each Game')
        plt.xlabel('Date')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(f"Each_Game_{metric.replace(' ', '_')}_over_time.png")
        plt.close()


def plot_team_metrics(df: pd.DataFrame, metrics: list[str]) -> None:
    """
    Main plotting function that calls sub-functions to generate all plots.
    """
    metric_labels = {
        'Goals For': 'Goals Scored',
        'Goals Against': 'Goals Conceded',
        'Goal Diff': 'Goal Difference',
        'Goal average': 'Goal Average',
        'Points': 'Points'
    }

    plot_cumulative_metrics(df, metrics, metric_labels)
    plot_per_game_metrics(df, metrics, metric_labels)


def main():
    """
    Main entry point: Loads the data and plots team metrics.
    """
    df = load_all_data()
    metrics_to_plot = ['Goals For', 'Goals Against', 'Goal Diff', 'Goal average', 'Points']
    plot_team_metrics(df, metrics_to_plot)


if __name__ == '__main__':
    main()