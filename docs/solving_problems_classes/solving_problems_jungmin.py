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

#질문과 답변기능을 하나로 묶은 클래스
class Question_Answer:
    #함수가 인스턴스 메소드라면 첫 인자를 'self'로 줘야 대상이 되는 인스턴스가 정확히 무엇인지 확인
    #__init__()은 반드시 첫 번째 인수로 self를 지정
    def __init__(self, problems, correct_answers):
        self.problems = problems
        self.correct_answers = correct_answers
        
    
    def problems_main(self):
        problems_first = self.problems[1], self.problems[3], self.problems[5], self.problems[7]
        problems_second = self.problems[0], self.problems[2], self.problems[4], self.problems[6]
        list_results = []
        
        for question in range(4):
            question_a = problems_second[question]
            question_b = problems_first[question]

            print("{}. {}".format(question + 1, question_a))
            print("{}".format(question_b))

            question_result = input("-정답 : ")

            
            list_results.append(question_result)
            print(list_results)

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

# class instance
question_answer = Question_Answer(list_problems, list_corrects)

# call funciton
question_answer.problems_main()

