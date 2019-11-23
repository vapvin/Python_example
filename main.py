print("Hello World")
print("Mary's cosmetics")

print('신씨가 소리질렀다. "도둑이야".')
print('"C:\\Windows"')

print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n 줄바꿈 \t 들여쓰기

print("오늘은", "일요일")

print("naver", "kakao", "sk", "samsung", sep=";")
print("naver", "kakao", "sk", "samsung", sep="/")
print("first", end=" ")
print("second")

string = "dk2jd923i1dk2jd93jfd92jd918943jfd8923"

print(len(string))

a = "3"
b = "4"

print(a+b)

s = "hello"
t = "python"

print(s, end="! ")
print(t)

print("Hi"*3)
print("-"*80)

t1 = 'python'
t2 = 'java'

print((t1+' '+t2+' ')*4)

print(20000*10)

print(2 + 2 * 3)

f = "132"

print(type(f))

num_str = "720"
num_str = int(num_str)

num = 100
num = str(num)

lang = 'python'
print(lang[0], lang[2])

license_plate = "24가 2210"
print(license_plate[4:])

string_odd = "홀짝홀짝홀짝"
print(string_odd[::2])
print(string_odd[1::2])

string_revers = "PYTHON"
print(string_revers[::-1])

phone_number = "010-1111-2222"
print(phone_number[:3], phone_number[4:8], phone_number[9:13])
print(phone_number.replace('-', ' '))
print(phone_number.replace('-', ''))

url = "http://sharebook.kr"
print(url[-2:])

lang_py = 'python'
print(lang_py)

# 만들어진 문자열은 바인딩 불가

english = "abcdfe2a354a32a"
print(english.replace('a', 'A'))

abc = 'abcd'
new_abc = abc.replace('b', 'B')
print(new_abc)

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

movie_rank.append("배트맨")

print(movie_rank)

movie_rank.insert(1, "슈퍼맨")

print(movie_rank)

movie_rank.remove("럭키")
# or del movie_rank[3]

del movie_rank[2:]
print(movie_rank)

lang1 = ["c", "c++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]

print("max:", max(nums))
print("min:", min(nums))

print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",
        "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]

print(len(cook))

numis = [1, 2, 3, 4, 5]

print(sum(numis)/len(numis))

price = ["20191115", 100, 130, 140, 150, 160, 170]

print(price[1:])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::2])
print(numbers[1::2])
print(numbers[::-1])

interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]

print(" ".join(interest))
print("\n".join(interest))

stringd = "삼성전자/LG전자/Naver"
interest2 = [stringd[0:4], stringd[5:9], stringd[10:15]]
print(interest2)

stringds = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest2 = [stringds[0:4], stringds[5:9],
             stringds[10:15], stringds[16:22], stringds[23:29]]
print(interest2)

interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)

interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)

my_variable = ()
t = (1, 2, 3)


# 투플은 값을 변경 할 수 없다.

my_tuple = (1,)

print(type(my_tuple))

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, a, b = scores

# *valid_score, _, _ = scores

print(valid_score)

_, _, *valid_score2 = scores

print(valid_score2)

_, *valid_score2, _ = scores

print(valid_score2)


temp = {

}


icecream = {
    "메로나": 1000,
    "폴라포": 1200,
    "빵빠레": 1800
}

print(icecream)

icecream['죠스바'] = 1200
icecream['월드콘'] = 1500

print(icecream)

icecream['메로나'] = 1300

print(icecream)

del icecream['메로나']

print(icecream)

inventory = {
    '메로나': [
        300, 20
    ],
    '비비빅': [
        400, 3
    ],
    '죠스바': [
        250, 1000
    ],
}

print(inventory)

print(inventory['메로나'][0], '원')
print(inventory['메로나'][1], '개')

inventory['월드콘'] = [500, 7]

print(inventory)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

dict_keys = list(icecream.keys())

print(dict_keys)

dict_val = list(icecream.values())

print(dict_val)

all_val = sum(dict_val)

print(all_val)

new_product = {'팥빙수': 2700, '아맛나': 1000}

icecream.update(new_product)

print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))

print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

result = dict(zip(date, close_price))

print(result)

# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가? Bool

print(3 == 5)  # False

print(3 < 5)  # True

x = 4
print(1 < x < 5)  # True

print((3 == 3) and (4 != 3))  # True

# print(3 => 4)  3은 4보다 크거나 같지 않기때문으 False로 오류를 출력

if 4 < 3:
    print("Hello World")
# 위 조건문은 조건식이 거짓임으로 실행되지 않는다.

if 4 < 3:
    print("Hello Wolrd")
else:
    print("Hi, there.")

# 위 조건문은 if문이 거짓임으로 else문이 실행되어 진다.

if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

# if문이 항상 참값임으로 1과 2가 순서대로 출력 후 else는 무시되어 진뒤 조건문 밖의 4가 출력된다.

if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

# 첫번째 if문이 True임으로 안쪽의 if False를 무시후 else를 실한한 후에 밖의 5를 출력한다.

user_data = input("입력해주세요")

print(user_data*2)

user_num = input("숫자를 입력하세요")

print(int(user_num)+10)

use_num = int(input("숫자를 입력하세요. 홀/짝을 판별합니다."))

if use_num % 2 == 0:
    print("짝수")
else:
    print("홀수")

users_inputs = int(input("숫자를 입력해주세요."))

if users_inputs + 20 > 255:
    print(255)
elif users_inputs + 20 < 0:
    print(0)
else:
    print(users_inputs+20)

pixel = int(input("입력깂 \b"))

print("출력값:", max(pixel - 20, 0))

user_time = input("현재시간:")

if user_time[3:] == "00" :
    print("정각입니다.")
else:
    print("정각이 아닙니다.")

fruit = ['사과', '포도', '홍시']

user_fav = input("좋이하는 과일은 무엇입니까?? ")

if user_fav in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "Samsung", "LG"]

user_inv = input("투자종목:")

if user_inv in warn_investment_list:
    print("투자위험종목")
else:
    print("투자안전종목")

fruits = {
    "봄": "딸기",
    "여름": "토마토",
    "가을": "사과"
}
#
# user_season = input("제가 좋아하는 과일은 무엇입니까?")
#
# if user_season in fruits.key():
#     print("정답입니다.")
# else:
#     print("틀렸습니다")
#
# if user_season in fruits.values():
#     print("정답입니다.")
# else:
#     print("틀렸습니다")

user_score = int(input("학점을 입력해주세요."))

if 81 <= user_score <= 100:
    print("grade is A")
elif 61 <= user_score <= 80:
    print("grade is B")
elif 41 <= user_score <= 60:
    print("grade is C")
elif 21 <= user_score <= 40:
    print("grade is D")
else:
    print("grad is E")

# user_in = input("입력:").split()
#
# amount = user_in[0]
# currency = user_in[1]
#
# if currency == "달라":
#     ratio = 1167
# elif currency == "엔":
#     ratio = 1.096
# elif currency == "유로":
#     ratio = 1268
# else:
#     ratio = 171

# print(ratio * int(amount), "원")

print("Hello World")


num1 = int(input("input number1:"))
num2 = int(input("input number2:"))
num3 = int(input("input number3:"))

if num1 > num2:
    max_num = num1
else:
    max_num = num2

if num3 > max_num:
    max_num = num3

print(max_num)

# max_num = max(num1,num2,num3)
# print(max_num)

phone_numbers = input("휴대전화 번호 입력 : ")

if phone_numbers[0:3] == "011":
    print("당신은 SKT 사용자 입니다.")
elif phone_numbers[0:3] == "016":
    print("당신은 KT 사용자 입니다.")
elif phone_numbers[0:3] == "019":
    print('당신은 LGT 사용자입니다.')
else:
    print("당신은 알 수 없는 사용자 입니다.")

zipcode = input("우편번호 : ")

if zipcode[2] in "012":
    print("강북구")
elif zipcode[2] in "345":
    print("도봉구")
else:
    print('노원구')

reg_num = input("주민등록번호 :")

if reg_num[7] in ['1','3']:
    print("남자")
else:
    print("여자")

reg_nums = input("주민등록번호: ")

if int(reg_nums[8:9]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

reg_numd = input("주민등록번호: ")

rem = sum % 11

valid_num 11 -rem

if int(reg_num[13]) == valid_num:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

volatility = int(btc['max_price']) - int(btc['min_price'])

if int(btc['opening_price']) + volatility > int(btc['max_price']):
    print('상승장')
else:
    print('하락장')

for a in ["가", "나", "다", "라"]:
    print(a)

for c in ["사과", "귤", "수박"]:
    print(c)

for d in ['사과', '귤', '수박']:
    print(d)
    print("--")

menu = ['김밥', '라면', '튀김']

for i in menu:
    print("오늘의 메뉴", i)

# main To sub

for food in menu:
    print("오늘의 메뉴"+food)

for ticker in portfolio:
    print(ticker,"보유중")

for pet in pets:
    print(pet,len(pet))

for price in prices:
    print(price + 10)

for price in prices:
    temp = price.replace(',', '')
    print(int(temp))

for food in menu:
    print(food[::1])

my_list = ['가', '나', '다', '라']

for val in my_list[1:]:
    if val != "가":
        print(val)

for val in my_list[::2]:
    print(val)


for val in my_list[1::2]:
    print(val)


for val in my_list[::-1]:
    print(val)

for val in my_list:
    if val < 0:
        print(val)

for val in my_list:
    if val % 3 == 0:
        print(val)

for val in my_list:
    if len(val) >= 3:
        print(val)

for val in my_list:
    if val > 5 and val < 10:
        print(val)

for val in my_list:
    if val > 10 and val < 20 and val % 3 == 0:
        print(val)

for val in my_list:
    if val % 3 == 0 and val % 4 == 0:
        print(val)

for val in my_list:
    if val.isupper():
        print(val)

for val in my_list:
    if not val.isupper():
        print(val)

for val in my_list:
    if val.isupper():
        print(val.lower(), end="")
    else:
        print(val.upper(), end="")

