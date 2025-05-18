def calculate_S(price1, price2, price3, A1, A2, A3, year):
    """
    根据输入的价格和财年，计算采购指数 S 和总价格 W。
    """
    # 定义不同年份的 W 值
    W_mapping = {
        1: 4800000,
        2: 7600000,
        3: 12000000,
        4: 19200000,
    }

    # 获取 W 的值
    W = W_mapping.get(year)
    if W is None:
        raise ValueError("无效的财年，year 必须是 1, 2, 3 或 4")
    
    # 计算采购指数 S
    S1 = A1 / ((year + 1) * 5)
    S2 = (A1 * A2) / (2500 * (year + 1) ** 2)
    S3 = (A1 * A3) / (1875 * (year + 1) ** 2)

    return S1 + S2 + S3, W


def find_best_A(price1, price2, price3, year, step=1000, max_A3=10000):
    """
    根据输入的价格和财年，找到使采购指数 S 最大的 A1, A2, A3 组合。
    """
    # 特殊处理价格为 0 的情况，直接返回 A1, A2, A3 = 0
    if price1 == 0 and price2 == 0 and price3 == 0:
        return 0, {"A1": 0, "A2": 0, "A3": 0, "W": 0}

    # 输入合法性检查
    if not (0 <= price1 <= 2000):
        raise ValueError("price1 超出范围 (0 ≤ price1 ≤ 2000)")
    if not (0 <= price2 <= 2500):
        raise ValueError("price2 超出范围 (0 ≤ price2 ≤ 2500)")
    if not (0 <= price3 <= 3000):
        raise ValueError("price3 超出范围 (0 ≤ price3 ≤ 3000)")
    if year not in [1, 2, 3, 4]:
        raise ValueError("year 必须是 1, 2, 3 或 4")

    # 动态计算 A1 和 A2 的最小值
    A1_min = 1000 * (year + 1) if price1 > 0 else 0
    A2_min = 1000 * (year + 1) if price2 > 0 else 0

    # 初始化最大 S 和最佳组合
    max_S = float("-inf")
    best_combination = {"A1": None, "A2": None, "A3": None, "W": None}

    # 遍历可能的 A1, A2, A3 组合
    for A1 in range(A1_min, A1_min + 5000, step) if price1 > 0 else [0]:
        for A2 in range(A2_min, A2_min + 5000, step) if price2 > 0 else [0]:
            for A3 in range(0, max_A3, step) if price3 > 0 else [0]:
                S, W = calculate_S(price1, price2, price3, A1, A2, A3, year)
                if S > max_S:
                    max_S = S
                    best_combination.update({"A1": A1, "A2": A2, "A3": A3, "W": W})

    return max_S, best_combination


def get_input(prompt, valid_range=None):
    """
    获取用户输入的整数并验证范围。
    """
    while True:
        try:
            user_input = int(input(prompt))
            if valid_range and not (valid_range[0] <= user_input <= valid_range[1]):
                print(f"请输入有效的数值，范围是 {valid_range[0]} 到 {valid_range[1]}")
            else:
                return user_input
        except ValueError:
            print("无效输入，请输入一个整数。")


if __name__ == "__main__":
    # 获取用户输入
    year = get_input("请输入财年 (1, 2, 3 或 4): ", valid_range=(1, 4))
    price1 = get_input("请输入低档产品的价格 (0 ≤ price₁ ≤ 2000): ", valid_range=(0, 2000))
    price2 = get_input("请输入中档产品的价格 (0 ≤ price₂ ≤ 2500): ", valid_range=(0, 2500))
    price3 = get_input("请输入高档产品的价格 (0 ≤ price₃ ≤ 3000): ", valid_range=(0, 3000))

    # 计算最佳 A1, A2, A3 和最大 S
    try:
        max_S, best_combination = find_best_A(price1, price2, price3, year)
        print(f"\n在 year = {year} 时，最大采购指数分数 S = {max_S:.2f}")
        print(f"最佳参数组合：")
        for key, value in best_combination.items():
            print(f"  {key} = {value}")
    except ValueError as e:
        print(f"输入错误: {e}")
1