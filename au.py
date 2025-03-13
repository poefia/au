#NTSC-J only
code_str = '''
C2009590 00000028
38604000 38800020
80ADA360 80A50024
7CBA2B78 3D808022
618C9734 7D8803A6
4E800021 7C7E1B78
3F808016 4800001D
2F736861 72656432
2F737973 2F535953
434F4E46 00000000
7C6802A6 7C7D1B78
38800001 639BAD7C
7F6803A6 4E800021
2C030000 418000C8
7C7F1B78 7FC4F378
38A04000 639BB11C
7F6803A6 4E800021
2C034000 408200A8
7FE3FB78 639BB2A4
7F6803A6 4E800021
2C030000 41800090
387EFFFF 38A04000
8C830001 2C040007
40A20028 88C3FFFF
2C060010 4082001C
3C80XXYY 90830001
3C80ZZZZ 6084GGGG
90831005 4800000C
34A5FFFF 4082FFCC
7FA3EB78 38800002
639BAD7C 7F6803A6
4E800021 2C030000
41800034 7C7F1B78
7FC4F378 38A04000
639BB1E0 7F6803A6
4E800021 2C034000
40820014 7FE3FB78
639BB2A4 7F6803A6
4E800021 3D80801A
618C8778 7D8803A6
4E800020 00000000
'''

import pyperclip
import os

def get_region_code():
    while True:
        try:
            XX_value = int(input('国籍コードの値を入力 (参考: https://wiki.tockdom.com/wiki/Extended_Regions#Region_List): '))
            if XX_value < 1 or XX_value > 254:
                print('1から254の範囲で入力してください。')
                continue
            XX_value_hex = str(format(XX_value, 'X'))
            print(f'HEX値: {XX_value_hex}')
            return XX_value_hex
        except ValueError:
            print('無効な入力です。')

def check_flag():
    YY_value = input('フラグを有効にしますか？(enterで有効 / nで無効): ')
    if YY_value == '':
        YY_value = '01'
        print('フラグを有効にしました。')
    else: #
        YY_value = '00'
        print('フラグを無効にしました。')
    return YY_value

def get_position():
    while True:
        try:
            Z_value = input('座標の値を入力: ')
            if len(Z_value) != 8:
                print('8文字で入力してください。')
                continue
            Z_1 = Z_value[:4].upper()
            Z_2 = Z_value[4:].upper()
            return Z_1, Z_2
        except ValueError:
            print('無効な入力です。')

def replace_code(code_str, XX_value_hex, YY_value, Z_1, Z_2):
    code_str = code_str.replace('XX', XX_value_hex)
    code_str = code_str.replace('YY', YY_value)
    code_str = code_str.replace('ZZZZ', Z_1)
    code_str = code_str.replace('GGGG', Z_2)
    return code_str

def main():
    XX_value_hex = get_region_code()
    YY_value = check_flag()
    Z_1, Z_2 = get_position()
    new_code = replace_code(code_str, XX_value_hex, YY_value, Z_1, Z_2)
    pyperclip.copy(new_code)
    print('コードをクリップボードにコピーしました。')
    os.system('pause')

if __name__ == '__main__':
    main()