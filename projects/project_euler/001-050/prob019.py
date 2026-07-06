import pandas as pd

series = pd.Series(pd.date_range(start="1901-01-01", end="2000-12-31", freq="D"))
df = series.to_frame(name="Date")
df["Weekday"] = series.dt.dayofweek
df["SumColumn"] = (df["Weekday"] == 6) & (df["Date"].dt.day == 1)

print(sum(df["SumColumn"]))
