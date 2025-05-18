def calculate_S(price1, price2, price3, A1, A2, A3, year):
    S1 = A1 / ((year + 1) * 5)
    S2 = (A1 * A2) / (2500 * (year + 1) ** 2)
    S3 = (A1 * A3) / (1875 * (year + 1) ** 2)
    return S1 + S2 + S3

def calculate_S(price1, price2, price3, A1, A2, A3, year):
    # 根据 year 设置 W 的固定值
    if year == 1:
        W = 4800000  # 修改为新的 W
    elif year == 2:
        W = 7600000  # 修改为新的 W
    elif year == 3:
        W = 12000000  # 修改为新的 W
    elif year == 4:
        W = 19200000  # 修改为新的 W
    else:
        raise ValueError("无效的财年")

# 定义范围
price1_range = (300, 2000)
price2_range = (500, 2500)
price3_range = (700, 3000)
year_values = [1, 2, 3, 4]  # 限制 year 为 1, 2, 3, 4
A1_limit = lambda year: 1000 * (year + 1)
A2_limit = lambda year: 1000 * (year + 1)

# 初始化存储每个 year 的最佳结果
results = []

# 遍历每个 year 并求最大 S 的参数组合
for year in year_values:
    max_S = -float('inf')
    best_combination = None
    for price1 in range(price1_range[0], price1_range[1] + 1, 100):  # 每次递增 100
        for price2 in range(price2_range[0], price2_range[1] + 1, 100):
            for price3 in range(price3_range[0], price3_range[1] + 1, 100):
                for A1 in range(A1_limit(year), A1_limit(year) + 5000, 1000):  # 每次递增 1000
                    for A2 in range(A2_limit(year), A2_limit(year) + 5000, 1000):
                        for A3 in range(0, 10000, 1000):  # 假设最大 A3 为 10000
                            S = calculate_S(price1, price2, price3, A1, A2, A3, year)
                            if S > max_S:
                                max_S = S
                                best_combination = (price1, price2, price3, A1, A2, A3, year)
    # 将结果存储
    results.append((year, max_S, best_combination))

# 输出结果
for result in results:
    year, max_S, best_combination = result
    print(f"财年 {year} 的最大采购指数分数 S = {max_S:.2f}")
    print("最佳参数组合：")
    print(f"  price1 = {best_combination[0]}")
    print(f"  price2 = {best_combination[1]}")
    print(f"  price3 = {best_combination[2]}")
    print(f"  A1 = {best_combination[3]}")
    print(f"  A2 = {best_combination[4]}")
    print(f"  A3 = {best_combination[5]}")
    print()
