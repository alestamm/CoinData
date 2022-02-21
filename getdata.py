import os
import pandas as pd

class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Do not hardcode your path as it only works on your machine ('Users/username/code...')
        # Use __file__ instead as an absolute path anchor independant of your usename
        # Make extensive use of `import ipdb; ipdb.set_trace()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../data/csv')
        csv_path = os.path.normpath(path)
        file_names = [fn for fn in os.listdir(csv_path) if fn.endswith('csv')]
        key_names = [fn.replace('.csv', '') for fn in file_names]
        key_names = [fn.replace('_dataset', '') for fn in key_names]
        key_names = [fn.replace('olist_', '') for fn in key_names]
        dataframes = [pd.read_csv(os.path.join(csv_path, file)) for file in file_names]
        data = dict(zip(key_names, dataframes))
        return data