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
