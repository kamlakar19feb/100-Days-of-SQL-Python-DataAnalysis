Find total revenue per Region and Month.

total_revenue=df.groupby(['Region','Month'])['Revenue'].sum().reset_index()
