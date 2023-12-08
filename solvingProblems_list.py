    
# 아래는 4개의 Python 관련 문제와 각 문항의 난이도에 따른 점수화  

# 1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)
#    1) var name, 2) name = value, 3) set name, 4) name == value
#    - 정답: 2

# 2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)
#    1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다
#    - 정답: 1

# 3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)
#    1) if-else, 2) for-in, 3) while, 4) def
#    - 정답: 1

# 4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)
#    1) class, 2) def, 3) import, 4) return
#    - 정답: 2

# 출제 문제
list_problems = [
        '문제 :Python에서 변수를 선언하는 방법은? (점수: 10점)',
        '1) var name 2) name = value 3) set name 4) name == value',
		'문제 :Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)',
        '1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다',
        '문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)' ,
        '1) if-else, 2) for-in, 3) while, 4) def',
        '문제: Python에서 함수를 정의하는 방법은? (점수: 5점)',
        '1) class, 2) def, 3) import, 4) return'

]
# 문제 당 정답
list_corrects = [2, 1, 1, 2]
list_result = [0, 0, 0, 0]
list_problems_first = list_problems[1], list_problems[3], list_problems[5], list_problems[7]
list_problems_second = list_problems[0], list_problems[2], list_problems[4], list_problems[6]

for question in [0, 1, 2, 3] :
    question_a = list_problems_second[question] 
    question_b = list_problems_first[question]

    print("{}. {}".format(question+1, question_a))
    print("{}".format(question_b))

    for corrects in [0, 1, 2] :
        corrects_a = list_corrects[corrects]
        
    question_result = input("-정답 : ")
    num_question_result = int(question_result)
    index = num_question_result - 1
    list_result[index] = list_result[index] + 1






