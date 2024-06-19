# 銘柄データ
current_prices = [200, 150, 300]
shares_outstanding = [1000000, 500000, 200000]
base_prices = [100, 120, 250]

# 各銘柄の現在の時価総額
current_market_caps = [current_prices[i] * shares_outstanding[i] for i in range(len(current_prices))]

# 各銘柄の基準時点の時価総額
base_market_caps = [base_prices[i] * shares_outstanding[i] for i in range(len(base_prices))]

# 現在の時価総額の合計
current_total_market_cap = sum(current_market_caps)

# 基準時点の時価総額の合計
base_total_market_cap = sum(base_market_caps)

# 基準時点の指数値（例として100を使用）
base_index_value = 100

# 時価加重平均株価指数の計算
weighted_index = (current_total_market_cap / base_total_market_cap) * base_index_value
weighted_index
