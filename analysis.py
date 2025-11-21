import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [800, 900, 500]}
df = pd.DataFrame(data)
print("Продажі по містах:")
print(df)
print("Середнє значення:", df["sales"].mean())