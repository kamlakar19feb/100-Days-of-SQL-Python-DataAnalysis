df=pd.read_csv("staff.csv")
df.head()
df['email_length']=df["email"].str.len()
df
