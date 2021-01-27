# 아래의 내용을 포함하는 run.py스크립트를 작성한다고 가정하자.
import argparse

parser = argparse.ArgumentParser() 

# 파싱할 인자를 add_argument메서드를 통해 추가한다.
parser.add_argument("-d", "--decimal", dest="decimal", action="store", help='원하는 숫자를 입력하세요')
# 추가 옵션을 받는 경우 action="store"
# 추가 옵션을 받지 않고 단지 옵션의 유/무 만이 필요한 경우 action="store_true"를 사용한다.
# 사용자가 입력한 옵션 값은 dest인자로 지정한 변수에 저장된다.

# extra value
parser.add_argument("-f", "--fast", dest="fast", action="store_true")

# existence/nonexistence
args = parser.parse_args()

if args.decimal == '1':
    print('decimal is 1')
if args.fast == True:
    print('-f option is used')