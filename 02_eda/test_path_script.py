import pandas as pd 
from pathlib import Path

current_path = Path(__file__).parent

df = pd.read_csv(current_path / "salaries.csv")
print(df.head())