# 출제 문제
list_problems = [
        'Python에서 변수를 선언하는 방법은? (점수: 10점)',
        '1) var name 2) name = value 3) set name 4) name == value',
		'Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)',
        '1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다', 
        'Python에서 조건문을 작성하는 방법은? (점수: 10점)', 
        '1) if-else, 2) for-in, 3) while, 4) def',
        'Python에서 함수를 정의하는 방법은? (점수: 5점)', 
        '1) class, 2) def, 3) import, 4) return'
]
# 문제 당 정답
list_corrects = [2, 1, 1, 2]

# 학점 기준 : 
# A : 30 이상, B : 20 점 이상,  F : 20점 미만 


### 난이도 출력, 학점계산 : solvingProblems_grade

# 임의의 입력
input_temp = [2, 1, 1, 2]
count = 0

if input_temp[0] == 2: # 10점
    count += 10
    
elif input_temp[1] == 1:
    count += 15
elif input_temp[2] == 1:
    count += 10
elif input_temp[3] == 2:
    count += 5

    








print("—----- 결과 —-------------")
print("응답한 내용 : {}".format())
print("당신 응답 합계 : {}".format())
print("학점은 {} 입니다.".format())

