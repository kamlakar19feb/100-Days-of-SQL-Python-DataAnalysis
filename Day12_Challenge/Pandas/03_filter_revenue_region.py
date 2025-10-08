Filter rows where "Revenue" > 10000" and "Region" is "East" or "West".

df.loc[(df['Revenue']>10000 ) & (df['Region'].isin(['East','West']))]
