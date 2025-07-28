# league_data.py
import pandas as pd

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

def get_all_league_data() -> pd.DataFrame:
    """
    Contains all historical matchday data and combines it into a single DataFrame.

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

    # New data from the provided image (21/07/2025)
    data5 = {
        'Position': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Team': ['Tits & Bits', 'See You Next Tuesday', 'Highfield Hornets',
                 'Belles & Balls', 'May Contain Nuts', 'Deep In The D', 'Balls Out',
                 'Pivot Grigio', 'Perfect Mix', 'Donald Dodgers'],
        'Played': [7, 7, 7, 7, 7, 6, 7, 6, 7, 7],
        'Won': [7, 5, 4, 4, 4, 3, 3, 2, 1, 0],
        'Lost': [0, 2, 2, 2, 3, 3, 4, 4, 6, 7],
        'Drawn': [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        'Goals For': [221, 143, 154, 187, 119, 126, 129, 116, 86, 51],
        'Goals Against': [92, 114, 133, 126, 124, 137, 146, 129, 152, 179],
        'Goal Diff': [129, 29, 21, 61, -5, -11, -17, -13, -66, -128],
        'Goal average': [2.40, 1.25, 1.16, 1.48, 0.96, 0.92, 0.88, 0.90, 0.57, 0.28],
        'Points': [35, 27, 26, 25, 24, 18, 18, 13, 9, 2]
    }

    df1 = create_dataframe(data1, '16/06/2025')
    df2 = create_dataframe(data2, '07/07/2025')
    df3 = create_dataframe(data3, '30/06/2025')
    df4 = create_dataframe(data4, '14/07/2025')
    df5 = create_dataframe(data5, '21/07/2025')

    return pd.concat([df1, df2, df3, df4, df5], ignore_index=True)