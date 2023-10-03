import random

def 替換K跟M(s):
    replacements = {
        'G': ('.', '00000000', '000000000'),
        'g': ('.', '00000000', '000000000'),
        'M': ('.', '00000', '000000'),
        'm': ('.', '00000', '000000'),
        'K': ('.', '00', '000'),
        'k': ('.', '00', '000')
    }
    for char, (dot, with_dot_replacement, without_dot_replacement) in replacements.items():
        if char in s:
            if '.' in s:
                s = s.replace(dot, '').replace(char, with_dot_replacement)
            else:
                s = s.replace(char, without_dot_replacement)
            break
    return s


顏色 = ["黑\033[0m(我是黑)", "棕", "紅", "橙", "黃", "綠", "藍", "紫", "灰", "白"]
色環 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ansi_codes = ["\033[0;30m", "\033[0;33m", "\033[0;31m", "\033[0;33m", "\033[93m", "\033[0;32m", "\033[0;34m", "\033[0;35m", "\033[0;37m", "\033[0;97m"]

倍色 = ["黑\033[0m(我是黑)", "棕", "紅", "橙", "黃", "綠", "藍", "紫", "灰", "白"]
倍數 = ["1", "10", "100", "1000", "10000", "100000", "1000000", "10000000", "100000000", "1000000000"]


while True:
    第一環= random.choice(顏色)
    index_1 = 顏色.index(第一環)
    corresponding_number_1 = 色環[index_1]
    ANSI_1 = ansi_codes[index_1]

    第二環= random.choice(顏色)
    index_2 = 顏色.index(第二環)
    corresponding_number_2 = 色環[index_2]
    ANSI_2 = ansi_codes[index_2]

    第三環= random.choice(倍色)
    index_3 = 倍色.index(第三環)
    corresponding_number_3 = 倍數[index_3]
    ANSI_3 = ansi_codes[index_3]
    
    倍數值 = str(index_1)+str(index_2)

    print(f"顏色：{ANSI_1}{第一環}\033[0m")
    # print(f"數字：{corresponding_number_1}")

    print(f"顏色：{ANSI_2}{第二環}\033[0m")
    # print(f"數字：{corresponding_number_2}")

    print(f"顏色：{ANSI_3}{第三環}\033[0m")
    # print(f"阻值：{倍數值*corresponding_number_3}")

    if ANSI_1 == "\033[0;33m":
        print("\033[0m因ANSI沒有橙，所以它跟黃色一樣是黃色")

    answer = input("請問阻值是多少？(請勿使用科學符號或英文代號)\n答：")

    if "k" or "k" or "m" or "M" or "." in answer:
        output_str = 替換K跟M(answer)
        answer = output_str
    

    if answer == str(int(倍數值)*int(corresponding_number_3)):
        print("\033[0;32m恭喜答對\033[0m\n-----------------------\n\n-----------------------")
    else:
        print(f"\033[0;31m上課是不是沒在聽\033[0m\n正確答案：{str(int(倍數值)*int(corresponding_number_3))}\n-----------------------\n\n-----------------------")

