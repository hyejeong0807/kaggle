import pandas as pd

trace = pd.read_csv('./basic1.csv')
print(trace.head())

trace = trace.sort_values('f5', ascending=False)
print(trace.head(10))

min_val = trace['f5'][:10].min()
print(min_val)

trace['f5'][:10] = min_val
print(trace.head(10))

print(trace[trace['age'] >= 80]['f5'].mean())
