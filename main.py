import pandas as pd
import numpy as np
from pathlib import Path


my_csv = Path(r"C:/Users/davidcui02/Desktop/CDP_Primary_demographics_v1.csv")
df = pd.read_csv(my_csv.resolve())
df.head()

