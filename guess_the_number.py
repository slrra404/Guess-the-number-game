import random

def main():
    # 範囲の入力
    n = int(input("最小値を入力してください: "))
    m = int(input("最大値を入力してください: "))

    # 最小値と最大値を確認
    if n > m:
        print("最小値は最大値以下でなければなりません。")
        return
    
    # 範囲内の乱数を作成
    target = random.randint(n, m)
    max_attempts = 5

    print(f"{n}から{m}まっでの数字を観測してください　最大{max_attempts}回の試行があります。")

    # 試行回数分ループ
    for attempt in range(max_attempts):
        guess = int(input(f"{attempt + 1}回目の試行: "))

        if guess < n or guess > m:
            print(f"入力は{n}から{m}の範囲内でなければなりません。 ")
        elif guess < target:
            print("これよりも大きい数字です。")
        elif guess > target:
            print("これよりも小さい数字です。")
        else:
            print("正解です！！！")
            break
    else:
        print(f"残念！正解は{target}でした。")

if __name__ == "__main__":
    main()