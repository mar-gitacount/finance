# 毎月の積立額
P = 20000  # 円

# 積立期間（年）
years = 30

# 月数
n = years * 12

# 各年利に対応する月利
annual_rates = [0.03, 0.05, 0.07]
monthly_rates = [rate / 12 for rate in annual_rates]


# 将来価値を計算
future_values = []
for r in monthly_rates:
    FV = P * (((1 + r) ** n - 1) / r) * (1 + r)
    future_values.append(FV)
print(f"毎月の積立金額{P}")
print(f"積立年数{years}")
print(future_values)
