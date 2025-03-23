import pandas
import numpy

print(pandas.__version__)
print(numpy.__version__)


def main():
    # 数値計算のテスト
    x = numpy.array([1, 2, 3, 4, 5])
    print("NumPyの配列:", x)
    print("平均値:", numpy.mean(x))

    # データフレームのテスト
    df = pandas.DataFrame(
        {"名前": ["田中", "鈴木", "佐藤"], "年齢": [25, 30, 35], "点数": [80, 90, 85]}
    )
    print("\nPandasのデータフレーム:")
    print(df)


if __name__ == "__main__":
    main()
