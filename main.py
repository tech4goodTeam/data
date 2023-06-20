import pandas as pd

import src.clean_data as clean




clean_data = clean.rename_cols(df)
clean_data = clean.select_cols(df)