Pandas Project: Regional Sales Performance Dashboard

Use orders.csv


Group by Region → sum Total_Revenue
Sort descending
regiona_df=(df.groupby('Region)['Total_Revenue'].sum().reset_index().sort_values(by='Total_Revenue',ascending=False))


(Optional) Plot a horizontal bar chart of Total_Revenue by Region

regional_df.plot(kind='bar', x='Region', y='Total_Revenue', color = 'Skyblue', legend=False)
plt.title('Total Revenue per Region')
plt.ylabel('Total Revenue')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.show()
