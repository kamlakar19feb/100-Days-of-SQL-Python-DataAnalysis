Use apply() with a custom function.
👉 Example: Add a column "Grade" based on salary:

Salary > 80,000 → "A"

Salary between 50,000–80,000 → "B"

Salary < 50,000 → "C"

def Grade(row):
    if row['salary'] >= 80000:
        return 'A'
    elif row['salary'] >= 60000 and row['salary']<80000:
        return 'B'
    else:
        return 'C'

df['Grade'] = df.apply(Grade, axis=1)
df
