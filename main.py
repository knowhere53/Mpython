# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from selenium import webdriver
import op
from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 파이썬 폴더가 아니면 작업 폴더 바꿔주기

""" 윕스온 웹 크롤링 """
driver = webdriver.Chrome("C:\python3.8\chromedriver\chromedriver.exe")
""" 윕스온 웹 크롤링 """
driver = webdriver.Chrome("/Users/yongjinjang/SynologyDrive/M파이썬/chromdriver/chromedriver")

from selenium import webdriver
driver = webdriver.Chrome('/Users/yongjinjang/SynologyDrive/M파이썬/chromdriver/chromedriver')


-----
부트캠프. 1. 26. 박준규

1. 파이썬 데이터(객체)
- 정수, 실수, 문자열, Bool, none, 리스트, 딕서녀리, 응답, bs,....
- 우리가 파이썬에 명령을 내릴 수 있는 모듯 것들이 다데이터
- 데이터를 생성하면 이름부터(변수) 만들어 줍시다.
- 파이썬의 모든 데이터는 고유한 기능이 있음. .dot 연산자 이용.
- 점, 괄호 정리.
   -> 점 . => 앞에 있는 데이터에서 무언가를 꺼내는 느낌(이어지는 느낌)
   -> 콤마 , => 테이터 분리 나열(단절, 데이터끼리 분리)

1,2,3 => 튜쁠(1,2,3)

<< [] vs {} vs () >>
[] : 리스트 만들때 쓴다. 자료구조에서 데이터 꺼낼 때.
[] 리스트 만들기
a = []
a = [1,2,3]

꺼내기. 리스트 말고 다른 것도 꺼낼 때는 대괄호.
a[0]

a = {'math':90, 'eng':80}
a['eng']


{} : 딕셔너리 만들 때.
{} : 만든거다.

() 함수 작동 시킬 때, 튜플 만들 때

문자열
 - 생성 : '', ""
 - 연산 : + 합쳐짐
 - 기능 : split, replace, format

format 은 바꿔 주는 것.

for i in range(1,6):
    print('data'+ str(i)+".xlsx")

포맷은 {} 빵꾸 뚫어 둔 곳에 채운다. 빵꾸 수 만큼 넣자.
for i in range(1,6):
    print('data {}.xlsx'.format(i))

구구단. 만들기. format( , , )
for i in range(2,10):
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j))


## 자료 구조.
  - 여러개의 데이터를 효율적으로 묶어서 관리하기
  - 파이썬의 기본 자료구조 : 리스트, 딕셔너리, 튜플, 셋 (리스트, 딕셔너리를 자주 씀)
  - 리스트는 순서!
  - 딕셔너리는 순서x 대신 키 값으로 데이터 매칭

3 개의 데이터, 속성은 3가지. 리스트와 딕셔너리로 저장하기
db = [
{'뉴스제목':'a', '링크': 'fb', '내용': 'C'},
{'뉴스제목':'b', '링크': 'ffb', '내용': 'etC'},
{'뉴스제목':'c', '링크': 'sb', '내용': 'dC'}]

빼올 때
db[0]['링크']
db[0]
db['링크'] =>   이건 안된다.

다 더해서 평균 구하기
num_list = [10,11,12,13,7,8,9]

sum = 0
for num in num_list :
    sum = sum + num

print(sum)
print(sum / len(num_list))

함수.
- 코드를 재사용하기 위해서 코드에 이름 붙여 줌
- def 함수이름 (필요에 따라 인풋들 (옵션) ):
    재사용 하려는 코드
    return 가지고 돌아올 데이터

re = 3.14 * 1.12
sum2 = [re, 10, 11, 0, 2]

def get_avg():
    num_list = [1,2,3]
    result = 0
    for num in num_list:
        result = result  + num
    avg = result/len(num_list)
    ## get_avg() 실행하면  이 상태는 avg에 있는게 아니고 실행하고 지워버림.
    ## return을 해줘야 데이터를 가저온다.
    ## 데이터를 가져오는 거지 변수는 가져오는게 아니다. 즉 변수 avg는 없는 거.
    return avg

get_avg()
잘 나온다.

그럼, 이제 num_list를 다르게 할 수 있게 해보자.
def get_avg(num_list):
    result = 0
    for num in num_list:
        result = result  + num
    avg = result/len(num_list)
    ## get_avg() 실행하면  이 상태는 avg에 있는게 아니고 실행하고 지워버림.
    ## return을 해줘야 데이터를 가저온다.
    ## 데이터를 가져오는 거지 변수는 가져오는게 아니다. 즉 변수 avg는 없는 거.
    return avg

get_avg([1,2,3,4])
=> 잘나옴

Def는 층이 생기는 것이다. 층별로 이동할 때에는 변수는 그대로, 값이 이동하는 것.
- input 도하고, 계산하면 Return으로 가져온다.

get_avg(sum2)
=> 잘나옴.

import pandas

리스트, 딕셔너리는 기본기능만 있음.
판다스의 자료 구조.
- 새로운 자료구조 2개를 제공. -
- Series, DataFrame

## 1. Series는 1차원(1줄 짜리)
  - 시리즈는 구성요소가 2개. index, values  인덱스는 자동으로 주어진다.
  - 순서 있음.
  - 기본적으로 인덱스로 선택
  - 범위로 가져올 수 있음. 슬라이스. [1:3]
  - index= 으로 숫자를 다른 이름으로 바꿀 수 있다.(학생 이름 등)
  - index 이름 바꿔도 여전히 순서도 쓸 수 있다.
# A, B, C, D, E 학생이 있으면
math = [90,89,88,92,91]
sorted(math)
sort는 되는데, 누군지 모른다.

import pandas as pd
## 별명으로 pd로 줄여서 부르자. 차이는 없음. 대체로 그렇게 쓴다.

pd.Series(math)
시리즈는 구성요소가 2개. index, values  인덱스는 자동으로 주어진다.

math_sr = pd.Series(math)
math_sr[0]
math_sr[1:3]

## 학생이름으로 인덱스를 바꾸자. 순서도 된다.
math_sr = pd.Series(math,index=['A', 'B', 'C', 'D', 'E'])
math_sr['A']
math_sr[1:3]

# 시리즈 기능 엄청 많다.
# 검색해서 쓰자. 몇가지 소개하면
    # 정렬 (기본적으로 오름 차순)
math_sr.sort_values()
math_sr.sort_values(ascending=False) #내림차순 옵션

    # 분산, 평균..., 기본 통계값 describe
math_sr.describe()

    # 필터링 - 조건 이용 데이터 가져오기
math_sr[ math_sr > 90 ]

    # 시리즈 연산
math = [90,89,88,92,91]
eng = [89, 90,92,88,12]

eng
math + eng #리스트 합치면, 10개 데이터가 될 뿐.

eng_sr = pd.Series(eng, index=['A', 'B', 'C', 'D', 'E'])
eng_sr = pd.Series(eng,index=['A', 'B', 'C', 'D','E'])

(math_sr + eng_sr) /2
(math_sr + eng_sr)**2 # 제곱


## Data frame
 - 2차원 자료
 - colume, index, value, 3개가 있다. (순서 기억)
 - 순서 있음.(행 방향.(가로)) / 열은 순서가 없다(부여할 수는 있으나 기본값으로 없음)
-

math = [90, 89, 88, 92, 91]
eng = [89, 90, 92, 88, 12]
kor = [19, 20, 91, 84, 52]


#딕셔너리로 묶고.
temp = {'math' : math, 'engng' : eng, 'kor':kor}
#프레임.
pd.DataFrame(temp, index=['A','B','C','D','E'])
#colume, index, value, 3개가 있다.
#이름 넣고
grade_df = pd.DataFrame(temp, index=['A','B','C','D','E'])


grade_df['eng']
grade_df['eng']['A']

#.loc 횡으로 가져오기
grade_df.loc['A']
grade_df.loc['A']['eng']

#loc 좌표로 가져오기
grade_df.loc['A','eng']

#슬라이싱
grade_df[ 1:4 ] #가로로 행으로 짜른다. 왜? 순서가 행만 있잖아.(기본적으로)

grade_df.sort_values('math',ascending=False )

#필터링(and : &,  or : | )
grade_df[ grade_df > 90 ] #이러면 전부다 90 이상인 값만 나옴.
grade_df[ grade_df['math'] > 90 ] #수학.

# and  &
grade_df[ (grade_df['math'] > 90) & (grade_df['kor'] > 90)] #수학.국어 & 넣는데 꼭!! () 넣자.
# or  |
grade_df[ (grade_df['math'] > 90) | (grade_df['kor'] > 90)] #수학.국어 & 넣는데 꼭!! () 넣자.


#깔끔하게 가보자.
cond1 = grade_df['math'] > 90
cond2 = grade_df['kor'] > 90

grade_df[ cond1 | cond2]


## 아래 타이타닉이 로드되지 않아서 아래 2줄 코드를 추가함. 22.1.26. https://minimin2.tistory.com/138
import ssl  #추가 1
ssl._create_default_https_context = ssl._create_unverified_context #추가 2

import  seaborn as sns
sns.get_dataset_names()
sns.load_dataset('titanic')

titanic_df = sns.load_dataset('titanic')
titanic_df.shape
titanic_df.head() #앞에꺼 5개.
titanic_df.head(10) #앞에꺼 10개.
titanic_df.tail(3) #뒤에꺼 3개.

#시리즈의 value count
titanic_df['survived'].value_counts(normalize=True) #산사람 비율

#성별과 생존률 관계 - 남자 중 산사람. 여자 중 산사람?
male = titanic_df[titanic_df['sex']=='male']
male['survived'].value_counts(normalize=True)
#남자 산사람 비율 나옴

female = titanic_df[titanic_df['sex']=='female']
female['survived'].value_counts(normalize=True)
#여자 산사람 비율 나옴

통계청, 공공데이터 포털 => 엑셀데이터. => Df로 가져오는 연습 몇번 만 하면 된다.



import requests
import bs4
bs4.BeautifulSoup(markup,'lxml')

page = 2
url  = 'https://movie.naver.com/movie/point/af/list.naver?&page={}' # {} 페이지 변하니
real_url = url.format(page)
resp = requests.get(real_url)
movie_bs = bs4.BeautifulSoup(resp.text, features="html.parser")  #features="html.parser" 이거 넣어줘야 함. 워닝 나옴.
td = movie_bs.find('td', class_ = 'title')  # class_  언더바 꼭 해주자
print( td.find('a').text ) #a 안에 있었다. <td> <a class=....>
print( td.find('em').text ) # em 안에 있다.
print( td.text.split('\n')[5] ) #<br> 뒤에 있는데, <br>은 의미 없다. 따라서 꾸며주는 아이가 없는 셈. 이럴때 다 가져와서 문장 구조 보고, \n이 많아서 나누소 몇번째 넣음.


#find_all로 모두 가져오자 바꿔보자.
td_list = movie_bs.find_all('td', class_ = 'title')  # class_  언더바 꼭 해주자
for td in td_list:
    print( td.find('a').text )
    print( td.find('em').text )
    print( td.text.split('\n')[5] )
    print("*" * 60)  # 구분자.

#저장하자.  딕셔너리. a['지정항목'] = 데이터
movie_data = []
for td in td_list:
    temp = {}
    temp['title'] = td.find('a').text
    temp['score'] = td.find('em').text
    temp['review'] = td.text.split('\n')[5]
    print(temp)
    movie_data.append(temp)

movie_data
pd.DataFrame( movie_data )

movie_data_df = pd.DataFrame(movie_data)
movie_data_df['score']


22.1.27.

1. 사용할 컬럼들 추리기
2. 컬럼 이름을 데이터 구조 (문맥)에 맞게 바꾸기


import pandas as pd

메타문자. 알파벳 => 특별한 효과. \n 줄바꿈. \t 탭.
윈도우는 r'...'으로 쓴다.(row의 약자. 백 슬러시 용도가 아니라 경로에 쓰는 진짜 \라는 의미) 맥은 /로 쓴다.
      윈도우는 path = r'C:\users\.......'
path = '/Users/yongjinjang/Desktop/126_Winter Bootcamp Programming(온라인) 안내_220119/수업 교재 및 데이터/졸업생의 진로 현황(전체).xlsx'
raw_df = pd.read_excel(path)
raw_df.columns
usc_cols = ['지역', '정보공시 \n 학교코드', '학교명', '졸업자.2', '(특수목적고)과학고 진학자.2',    '(특수목적고)외고ㆍ국제고 진학자.2']

raw_df2 = raw_df[usc_cols]
    #원래는 raw_df[ ['지역',    ......]  ] 대괄호 안에 리스트로 들어가야 한다. 원래는 1개만 읽는데 여러개면 리스트로 해서 리스트 안에 있는 걸 가져오라는 것.

#이름 바꾸기.
raw_df2.columns = ['지역', '코드', '학교명','졸업생', '과고','외고'] #여기 대괄호 1개이다. .columns는 이름 갖고오는 함수

raw_df3 = raw_df2.drop(0)
    # 여러개 하고 싶으면, .drop([0,1,2])

# 인덱스
#보통의 경ㅇ우 0,1,2,3 숫자가 잘 들어 있으면 됨.
# -> drop 때문에 중간중간 숫자가 빠져있는 것을 조심
# 시계열 데이터인 경우는 인덱스를 datetime(날짜)로 세팅

1. 결측 데이터 체크
2 데이터 타입 체크

raw_df3.isna().sum()
  # isna() : NaN 인지 물어보는 함수. 없으면 Flase 인데 파이썬은  False를 0으로도 인식(true는 1)
  # sum()

raw_df3[ raw_df3['지역'].isna()]
raw_df3[ raw_df3['과고'].isna()]

결측 데이터 처리. -> 상황에 따라 다름.
가급적 삭제 안하는 방법으로 가야 한다.
  - 지역은 실수이니까 인터넷 찾아서 넣고,
  - 졸업생 과고 가 없는 것은..  진짜일 것임. 그럼 버리자.
  - 여기서는 실습이니까 dropna 사용해서 벼렸다.

raw_df4 = raw_df3.dropna()  # NaN 있으면 그냥 버려. drop에도 여러가지가 있다.

#2. 데이터 속성 값 체크
raw_df4.dtypes #데이터 타입 체크

raw_df4['과고'][3]  # '2' 문자네....
#셀병합 때문에 그렇다.  object가 문자.

raw_df4['졸업생'] = pd.to_numeric(raw_df4['졸업생'])  #문자를 숫자로. (정수 or 실수)
raw_df4['과고'] = pd.to_numeric(raw_df4['과고'])  #문자를 숫자로. (정수 or 실수)
raw_df4['외고'] = pd.to_numeric(raw_df4['외고'])  #문자를 숫자로. (정수 or 실수)
  # to_numeric은 한번에 못바꿈. 하나씩만 됨.

여러 개면, for로 할 수 있다. 아래 처럼.
for col in ['졸업생', '과고', '외고']:
    raw_df4[col] = pd.to_numeric(raw_df4[col])

raw_df4.dtypes #바뀌어 있다. int으로
raw_df4

# 중간에 index 이빨이 빠졌다. 리셋하자.
raw_df4.reset_index(drop) # drop을 안하면 기존꺼도 유지된다. 그럼 인덱스가 2개.

# 주기적으로 사용하고 싶다. 데이터 다운 받으면 다시 이걸 해먹고 싶다.
# 그러면,함수로 해놓아 보자.

path =





path = '/Users/yongjinjang/Desktop/126_Winter Bootcamp Programming(온라인) 안내_220119/수업 교재 및 데이터/졸업생의 진로 현황(전체).xlsx'
raw_df = pd.read_excel(path)
raw_df.columns
usc_cols = ['지역', '정보공시 \n 학교코드', '학교명', '졸업자.2', '(특수목적고)과학고 진학자.2',    '(특수목적고)외고ㆍ국제고 진학자.2']

raw_df2 = raw_df[usc_cols]
    #원래는 raw_df[ ['지역',    ......]  ] 대괄호 안에 리스트로 들어가야 한다. 원래는 1개만 읽는데 여러개면 리스트로 해서 리스트 안에 있는 걸 가져오라는 것.

#이름 바꾸기.
raw_df2.columns = ['지역', '코드', '학교명','졸업생', '과고','외고'] #여기 대괄호 1개이다. .columns는 이름 갖고오는 함수

raw_df3 = raw_df2.drop(0)
    # 여러개 하고 싶으면, .drop([0,1,2])

# 인덱스
#보통의 경ㅇ우 0,1,2,3 숫자가 잘 들어 있으면 됨.
# -> drop 때문에 중간중간 숫자가 빠져있는 것을 조심
# 시계열 데이터인 경우는 인덱스를 datetime(날짜)로 세팅

1. 결측 데이터 체크
2 데이터 타입 체크

raw_df3.isna().sum()
  # isna() : NaN 인지 물어보는 함수. 없으면 Flase 인데 파이썬은  False를 0으로도 인식(true는 1)
  # sum()

raw_df3[ raw_df3['지역'].isna()]
raw_df3[ raw_df3['과고'].isna()]

결측 데이터 처리. -> 상황에 따라 다름.
가급적 삭제 안하는 방법으로 가야 한다.
  - 지역은 실수이니까 인터넷 찾아서 넣고,
  - 졸업생 과고 가 없는 것은..  진짜일 것임. 그럼 버리자.
  - 여기서는 실습이니까 dropna 사용해서 벼렸다.

raw_df4 = raw_df3.dropna()  # NaN 있으면 그냥 버려. drop에도 여러가지가 있다.

#2. 데이터 속성 값 체크
raw_df4.dtypes #데이터 타입 체크

raw_df4['과고'][3]  # '2' 문자네....
#셀병합 때문에 그렇다.  object가 문자.

raw_df4['졸업생'] = pd.to_numeric(raw_df4['졸업생'])  #문자를 숫자로. (정수 or 실수)
raw_df4['과고'] = pd.to_numeric(raw_df4['과고'])  #문자를 숫자로. (정수 or 실수)
raw_df4['외고'] = pd.to_numeric(raw_df4['외고'])  #문자를 숫자로. (정수 or 실수)
  # to_numeric은 한번에 못바꿈. 하나씩만 됨.

여러개면, for로 할 수 있다. 아래 처럼.
for col in ['졸업생', '과고', '외고']:
    raw_df4[col] = pd.to_numeric(raw_df4[col])

raw_df4.dtypes #바뀌어 있다. int으로
raw_df4

# 중간에 index 이빨이 빠졌다. 리셋하자.
raw_df4.reset_index(drop) # drop을 안하면 기존꺼도 유지된다. 그럼 인덱스가 2개.

# 주기적으로 사용하고 싶다. 데이터 다운 받으면 다시 이걸 해먹고 싶다.
# 그러면,함수로 해놓아 보자.


path = '/Users/yongjinjang/Desktop/126_Winter Bootcamp Programming(온라인) 안내_220119/수업 교재 및 데이터/졸업생의 진로 현황(전체).xlsx'

def gradu(path):
    raw_df = pd.read_excel(path, sheet_name=0)  #sheet
    usc_cols = ['지역', '정보공시 \n 학교코드', '학교명', '졸업자.2', '(특수목적고)과학고 진학자.2',    '(특수목적고)외고ㆍ국제고 진학자.2']
    raw_df2 = raw_df[usc_cols]
    raw_df2.columns = ['지역', '코드', '학교명','졸업생', '과고','외고'] #여기 대괄호 1개이다. .columns는 이름 갖고오는 함수
    raw_df3 = raw_df2.drop(0)

    raw_df4 = raw_df3.dropna().copy()  # NaN 있으면 그냥 버려. drop에도 여러가지가 있다. / copy()를 넣으면 df3에서 분리됨! 경고 안나옴.
    raw_df4['졸업생'] = pd.to_numeric(raw_df4['졸업생'])  #문자를 숫자로. (정수 or 실수)
    raw_df4['과고'] = pd.to_numeric(raw_df4['과고'])  #문자를 숫자로. (정수 or 실수)
    raw_df4['외고'] = pd.to_numeric(raw_df4['외고'])  #문자를 숫자로. (정수 or 실수)
    # 중간에 index 이빨이 빠졌다. 리셋하자.
    raw_df5 = raw_df4.reset_index(drop=True) # drop을 안하면 기존꺼도 유지된다. 그럼 인덱스가 2개.

    return raw_df5
# 파일 입력 경로만 바꿔 주면 되겠다.
a = '/Users/yongjinjang/Desktop/126_Winter Bootcamp Programming(온라인) 안내_220119/수업 교재 및 데이터/졸업생의 진로 현황(전체).xlsx'
grade_df = gradu(a)

#졸업생 많은 학교?
grade_df.sort_values('졸업생', ascending=False)[:20] #or head(20)

grade_df['과고']+grade_df['외고']

#colum 추가
grade_df["과고+외고"] = grade_df['과고']+grade_df['외고']
#중요! 추가하는 colme의 숫자와 추가된 데이터 숫자가 같아야 함.  표본 100개인데, 과고 +외고 100개 안되면 에러

grade_df["특목고 비율"] = grade_df['과고+외고'] / grade_df['졸업생'] * 100

grade_df.sort_values('특목고 비율', ascending=False)[:20]

grade_df.drop('과고+외고', axis = 1)

import  folium
folium.Map([37, 127])
파이썬 기본 테이터 타입.
문자열
- 생성 : '', ""
- 연산 : 더하기  => 하나로 합쳐짐
- 기능 : split, replace, format...

자료구조
- 여러개 데이터를 효율적으로 묶어서 관리
- 리스트 : 순서
- 딕셔너리 : 순서x, 키값
- 판다스 : 시리즈, DF

처음 데이터를 가져올 떄, 리스트 딕셔너리로 한다. 묶어주는 역할.
판다스 -> 시리즈, DF는 묶는 것이 아니라 핸들링(none값 찾아서 바꾸거나.. 한 줄씩 한번에 바꾸거나가 매우 쉽다)
        하지만 묶어주는 역할을 하지는 못함. 리스트, 딕셔너리로 갖고와서 나가는 것.


2. 데이터를 어떻게 다룰 것인가???
### 함수들.
- 코드를 재사용하기 위해서 코드에 이름을 붙여 줌.
- 재사용 해야!! 가독성, 관리, 가 좋고, 에러가 안남. - 나는 에러 많이 나더라 오타도나고 해서. 재사용 필요하네.

- 제어문
 - 반복문 : for, while문. for 가 강력하다. 순서있는 자료구조로 for 가 왔따!
    자료구조에다 작업을 하는 것이 아니라
    그 안에 데이터 값을 써먹는 것이다. 그런데 for 는 자동으로 꺼내준다.
 - 조건문,
  - if - elif - else
  - 하나의 조건문 안에서는 결과가 하나만 나옴.
변수 - 함수
 - 변수 : 값을 넣으려고 쓴다. 데이터를 재사용하려고 이름을 붙임(path 처럼. path = '주소값...')
 - 함수 : 연산을 하려고, 코드를 재상용하기 위해 코드에 이름을 붙여줌.
 - 객체 : 여러 프로그래머가 같이 만드려면??  작업분할이 필요해. 함수이름, 변수명 사람마다 조금이라도 바꿔버리면 우왕.... 망함.
 -


객체 지향 언어 파이썬???

사업체현황_산업대분류별_총괄.xlsx

import pandas as pd
path = '/Users/yongjinjang/Desktop/사업체현황_산업대분류별_총괄.xlsx'
raw_df = pd.read_excel(path)


