Group data by "Region" and find the average Profit per Region.

avg_profit_region=df.groupby('Region)['Profit'].mean().reset_index()
