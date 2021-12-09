import pandas as pd
import numpy as np

trace = pd.read_csv('./basic1.csv')
print(trace.head())

trace = trace.sort_values('f5', ascending=False)
print(trace.head(10))

min_val = trace['f5'][:10].min()
print(min_val)

trace['f5'][:10] = min_val
print(trace.head(10))

print(trace[trace['age'] >= 80]['f5'].mean())

"""
    <문제 2>
    데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서,
    'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고
    두 표준편차 차이 계산하기
"""
df = pd.read_csv('./basic1.csv')
data70, data30 = np.split(df, [int(.7*len(df))])
print(data70.tail())

# 결측치 확인
print(data70.isnull().sum())

# 중앙값 채우기 전 표준편차
std1 = data70['f1'].std()

# 중앙값 계산
mid = data70['f1'].median()

# 결측치를 중앙값으로 채움
data70['f1'] = data70['f1'].fillna(mid)

# 결측치를 채운 후 표준편차
std2 = data70['f1'].std()

print(data70.isnull().sum())

print(std1 - std2)

"""
    <문제3>
    데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
    단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함
"""

df = pd.read_csv('./basic1.csv')

std = df['age'].std() * 1.5
mean = df['age'].mean()

min_out = mean - std
max_out = mean + std
print(min_out, max_out)

print(df.loc[(df['age'] < min_out)]['age'].sum() + df.loc[(df['age'] > max_out)]['age'].sum())