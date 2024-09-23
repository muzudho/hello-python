#
# python what_is_range.py
#
# range(1, 11) って何だろう？
#
import traceback


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        print(f"""\
1 から 10 までの数が入ったリストを作ってみよう！

{[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

{list(range(1, 11))}

{[i for i in range(1, 11)]}""")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！  
{err=}  {type(err)=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
