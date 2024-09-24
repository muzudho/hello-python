#
# python what_is_for_loop.py
#
# for ループって何だろう？
#
import traceback


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        print(f"""\
こんな感じの for ループを実行してみよう！

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]:
    print(f"{{i=}}")
""")

        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]:
            print(f"{i=}")

        print(f"ループを抜けたあとにも確認じゃ　{i=}")
        print() # 改行


        print(f"""\
こんな感じの for ループを実行してみよう！

for i in range(1, 11):
    print(f"{{i=}}")
""")

        for i in range(1, 11):
            print(f"{i=}")

        print(f"ループを抜けたあとにも確認じゃ　{i=}")
        print() # 改行


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！  
{err=}  {type(err)=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
