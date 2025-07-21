import pandas as pd
import matplotlib.pyplot as plt


def create_dataframe(data: dict, date_str: str) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from the input dictionary and assigns a date.
    
    Args:
        data (dict): Dictionary containing league data.
        date_str (str): Date string in the format 'dd/mm/yyyy'.

    Returns:
        pd.DataFrame: DataFrame with an added 'Date' column.
    """
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(date_str, format='%d/%m/%Y')
    return df


def load_all_data() -> pd.DataFrame:
    """
    Loads all matchday data and combines into a single DataFrame.

    Returns:
        pd.DataFrame: Combined DataFrame with data from all matchdays.
    """
    data1 = {
        'Position': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Team': ['Tits & Bits', 'Belles & Balls', 'Balls Out', 'Highfield Hornets',
                 'Deep In The D', 'See You Next Tuesday', 'Pivot Grigio',
                 'Donald Dodgers', 'Perfect Mix', 'May Contain Nuts'],
        'Played': [1]*10,
        'Won': [1]*5 + [0]*5,
        'Lost': [0]*5 + [1]*5,
        'Drawn': [0]*10,
        'Goals For': [34, 28, 25, 21, 19, 18, 15, 9, 8, 5],
        'Goals Against': [5, 8, 9, 15, 18, 19, 21, 25, 28, 34],
        'Goal Diff': [29, 20, 16, 6, 1, -1, -6, -16, -20, -29],
        'Goal average': [6.80, 3.50, 2.78, 1.40, 1.06, 0.95, 0.71, 0.36, 0.29, 0.15],
        'Points': [5]*5 + [2, 1, 0, 0, 0]
    }

    data2 = {
        'Position': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Team': ['See You Next Tuesday', 'Tits & Bits', 'Highfield Hornets',
                 'May Contain Nuts', 'Belles & Balls', 'Pivot Grigio', 'Balls Out',
                 'Deep In The D', 'Perfect Mix', 'Donald Dodgers'],
        'Played': [5, 4, 5, 5, 5, 4, 5, 4, 5, 4],
        'Won': [4, 4, 3, 3, 2, 2, 2, 2, 0, 0],
        'Lost': [1, 0, 1, 2, 2, 2, 3, 2, 5, 4],
        'Drawn': [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        'Goals For': [110, 132, 111, 82, 113, 82, 87, 74, 60, 26],
        'Goals Against': [74, 53, 84, 91, 79, 62, 106, 92, 124, 112],
        'Goal Diff': [36, 79, 27, -9, 34, 20, -19, -18, -64, -86],
        'Goal average': [1.49, 2.49, 1.32, 0.90, 1.43, 1.32, 0.82, 0.80, 0.48, 0.23],
        'Points': [22, 20, 20, 17, 15, 12, 12, 11, 3, 0]
    }

    data3 = {
        'Position': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Team': ['Highfield Hornets', 'Tits & Bits', 'See You Next Tuesday',
                 'Deep In The D', 'Balls Out', 'Belles & Balls', 'May Contain Nuts',
                 'Pivot Grigio', 'Perfect Mix', 'Donald Dodgers'],
        'Played': [4, 3, 3, 3, 4, 4, 3, 3, 4, 3],
        'Won': [3, 3, 2, 2, 2, 1, 2, 1, 0, 0],
        'Lost': [0, 0, 1, 1, 2, 2, 1, 2, 4, 3],
        'Drawn': [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        'Goals For': [91, 98, 66, 61, 74, 75, 39, 55, 45, 18],
        'Goals Against': [63, 40, 33, 58, 84, 71, 55, 47, 97, 74],
        'Goal Diff': [28, 58, 33, 3, -10, 4, -16, 8, -52, -56],
        'Goal average': [1.44, 2.45, 2.00, 1.05, 0.88, 1.06, 0.71, 1.17, 0.46, 0.24],
        'Points': [18, 15, 12, 11, 11, 10, 10, 7, 2, 0]
    }

    # Data from the provided image (14/07/2025)
    data4 = {
        'Position': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Team': ['See You Next Tuesday', 'Tits & Bits', 'May Contain Nuts', 'Highfield Hornets',
                 'Belles & Balls', 'Deep In The D', 'Balls Out', 'Pivot Grigio',
                 'Perfect Mix', 'Donald Dodgers'],
        'Played': [6, 5, 6, 6, 6, 5, 6, 5, 6, 5],
        'Won': [5, 5, 4, 3, 3, 3, 2, 2, 0, 0],
        'Lost': [1, 0, 2, 2, 2, 2, 4, 3, 6, 5],
        'Drawn': [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        'Goals For': [133, 165, 103, 134, 154, 96, 103, 99, 73, 38],
        'Goals Against': [90, 76, 104, 117, 96, 104, 129, 103, 145, 134],
        'Goal Diff': [43, 89, -1, 17, 58, -8, -26, -4, -72, -96],
        'Goal average': [1.48, 2.17, 0.99, 1.15, 1.60, 0.92, 0.80, 0.96, 0.50, 0.28],
        'Points': [27, 25, 22, 21, 20, 16, 13, 12, 4, 1]
    }

    df1 = create_dataframe(data1, '16/06/2025')
    df2 = create_dataframe(data2, '07/07/2025')
    df3 = create_dataframe(data3, '30/06/2025')
    df4 = create_dataframe(data4, '14/07/2025') # New data from image, renamed to df4

    return pd.concat([df1, df2, df3, df4], ignore_index=True)


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