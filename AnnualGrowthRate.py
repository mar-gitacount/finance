def annual_growth_rate(V0, Vt, t):
    # Calculate the annual growth rate
    growth_rate = (Vt / V0) ** (1 / t)
    return growth_rate

# Example usage:
initial_value = 1000  # 初期の価値
final_value = 1500    # 時刻 t における価値
time_period = 5       # 時間 t（年数）

# 年次成長率を計算する
annual_rate = annual_growth_rate(initial_value, final_value, time_period)

# 結果を出力する
print(f"年次成長率: {annual_rate:.4f}")
