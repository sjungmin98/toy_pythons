# # 출제 문제
# list_problems = [
#         'Python에서 변수를 선언하는 방법은? (점수: 10점)',
#         '1) var name 2) name = value 3) set name 4) name == value',
# 		'Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)',
#         '1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다', 
#         'Python에서 조건문을 작성하는 방법은? (점수: 10점)', 
#         '1) if-else, 2) for-in, 3) while, 4) def',
#         'Python에서 함수를 정의하는 방법은? (점수: 5점)', 
#         '1) class, 2) def, 3) import, 4) return'
# ]
# # 문제 당 정답
# list_corrects = [2, 1, 1, 2]
def problems_main(questions, correct_answers) :
    results = [0, 0, 0, 0]
    problems_first = questions[1], questions[3], questions[5], questions[7]
    problems_second = questions[0], questions[2], questions[4], questions[6]
    list_results = []

    for question in [0, 1, 2, 3]:
        question_a = problems_second[question]
        question_b = problems_first[question]

        print("{}. {}".format(question + 1, question_a))
        print("{}".format(question_b))

        question_result = input("-정답 : ")
        num_question_result = int(question_result)
        index = num_question_result - 1
        results[index] = results[index] + 1

        list_results.append(question_result)

    return results, [int(i) for i in list_results]

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

list_corrects = [2, 1, 1, 2]

results, list_results = problems_main(list_problems, list_corrects)