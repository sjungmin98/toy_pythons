# source from ../polls_first/polls_first_[Jungmin].py

# list_question = [
#     "상품의 품질에 대해 어떻게 생각하시나요?",
#     "상품의 가격에 대해 어떻게 생각하시나요?",
#     "상품의 디자인에 대해 어떻게 생각하시나요?",
#     "상품에 대한 전반적인 만족도는 어떠신가요?"
# ]

# list_answer =  ["좋음", "중간", "좋아지길"]

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer = ["좋음", "중간", "좋아지길"]

list_result = [0, 0, 0]

for question in [0, 1, 2, 3] :
    question_a = list_question[question] 
    print("{}. {}".format(question+1, question_a))
    for answer in [0, 1, 2] :
        answer_a = list_answer[answer]
        print("{}. {}".format(answer+1, answer_a), end="  ")

    print("")
    print("")
    question_result = input("당신의 생각은 몇 번 : ")
    num_question_result = int(question_result)
    index = num_question_result - 1
    list_result[index] = list_result[index] + 1
        
    if question < 3 :
        print("-----------------")
    else:
        pass

result = ((list_result[0] * 3) + (list_result[1] * 2) + (list_result[2] * 1)) / (list_result[0] + list_result[1] + list_result[2])

print("")
print("—--- 통 계 ----")
print("설문자 답항별 갯수 표시 : {}".format(list_result))
print("답변별 가중치 (좋음:3, 중간:2, 좋아지길:1)")
print("답항 가중 평균 : {}".format(result))

