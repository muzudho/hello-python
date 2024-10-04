#
# python what_is_len.py
#
# len(x) って何だろう？
#
import traceback


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        print(f"""\
リストの長さを調べよう！

{len([])}

{len([1])}

{len([1, 2])}

{len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}

{len(range(1, 11))}

{len(list(range(1, 11)))}

{len([i for i in range(1, 11)])}""")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
