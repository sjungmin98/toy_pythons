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



list_result = [0, 0, 0, 0]
list_problems_first = list_problems[1], list_problems[3], list_problems[5], list_problems[7]
list_problems_second = list_problems[0], list_problems[2], list_problems[4], list_problems[6]
list_list = []
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

    list_list.append(question_result)


input_temp = [int(i) for i in list_list]


def total_responses(score):

    score = 0

    # 점수 합계
    if input_temp[0] == 2:
        score += 10
    if input_temp[1] == 1:
        score += 15
    if input_temp[2] == 1:
        score += 10
    if input_temp[3] == 2:
        score += 5

    # 학점
    if score >= 30:
        result = "A"
    elif score >= 20:
        result = "B"
    else:
        result = "F"
    
    print("—----- 결과 —-------------")
    print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}".format(input_temp[0], input_temp[1], input_temp[2], input_temp[3]))
    print("당신 응답 합계 : {}점".format(score))
    print("학점은 {} 입니다.".format(result))


total_responses(input_temp)

