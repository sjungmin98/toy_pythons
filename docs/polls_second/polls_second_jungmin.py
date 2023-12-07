list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer = ["좋음", "중간", "좋아지길"]

# for num_count_question in range(4):
#     print("{}.{}".format(num_count_question+1, list_question[num_count_question]))
#     for num_count_answer in range(3):
#         print("{}.{}".format(num_count_answer+1, list_answer[num_count_answer]), end='   ')
#     if num_count_question+1 < 4:
#         print("\n----------")
# —--- 통 계 ----
# 설문자 답항별 갯수 표시 : [1, 1, 2]

# 답변별 가중치 (좋음:3, 중간:2, 좋아지길:1)
# 답항 가중 평균 : 

# (1*3 + 1*2 +2*1) / (3+2+1) = 0.86
2
list_statistics = [0, 0, 0]

for num_count_question in [0, 1, 2, 3]:
    str_list_question = list_question[num_count_question]

    print("{}. {}".format(num_count_question+1, str_list_question))
    for num_count_answer in [0, 1, 2]:
        str_list_answer = list_answer[num_count_answer]
        print("{}.{}  ".format(num_count_answer+1, list_answer[num_count_answer]), end=" ")   
    
    answer_a = input("\n당신의 생각은 몇 번 : ")
    answer_b = int(answer_a)
    index = answer_b - 1
    list_statistics[index] = list_statistics[index] + 1
    if num_count_question < 3:
        print("\n----------")   


result = ((list_statistics[0] * 3) + (list_statistics[1] * 2) + (list_statistics[2] * 1)) / (3 + 2 + 1) 
print("---통계---")
print("설문자 답항별 갯수 표시 : {}".format(list_statistics)) 
print("답항 가중 평균 : {}".format(result))
