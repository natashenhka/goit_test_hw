import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [12000, 9000, 5000]}
df = pd.DataFrame(data)
print("Продажі по містах:")
print(df)
print("Середнє значення:", df["sales"].mean())