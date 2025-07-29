# Netball League Data Analysis 📊
This repository provides tools to analyze and visualize netball league data, with a special focus on "Pivot Grigio" (highlighted in plots!).

`league_data.py`
This file stores all historical netball league data, combining individual matchday records into a comprehensive pandas DataFrame.

`netball_plot.py`
This script visualizes the data from league_data.py. It generates:

- Cumulative Metric Plots: Shows overall trends for metrics like Goals For, Goals Against, Goal Difference, Goal Average, and Points.
- Per-Game Metric Plots: Displays game-by-game changes for the same metrics.
- "Pivot Grigio" Highlight: "Pivot Grigio" is prominently marked in red on all plots.

Running netball_plot.py saves these plots as .png files.

## How to Use It
- Install dependencies: pip install pandas matplotlib
- Run the script: python netball_plot.py
- Find generated plots in the directory.
- Enjoy the netball stats! 🥅