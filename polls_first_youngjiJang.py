# list_question = [
#     "상품의 품질에 대해 어떻게 생각하시나요?",
#     "상품의 가격에 대해 어떻게 생각하시나요?",
#     "상품의 디자인에 대해 어떻게 생각하시나요?",
#     "상품에 대한 전반적인 만족도는 어떠신가요?"
# ]

# list_answer =  ["좋음", "중간", "좋아지길"]

# for num_count_question in range(4):
#     print("{}.{}".format(num_count_question+1, list_question[num_count_question]))
#     for num_count_answer in range(3):
#         print("{}.{}".format(num_count_answer+1, list_answer[num_count_answer]), end='   ')
#     if num_count_question+1 < 4:
#         print("\n----------")


list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer = ["좋음", "중간", "좋아지길"]

for num_count_question in [0, 1, 2, 3]:
    str_list_question = list_question[num_count_question]
    print("{}. {}".format(num_count_question+1, str_list_question))
    for num_count_answer in [0, 1, 2]:
        str_list_answer = list_answer[num_count_answer]
        print("{}.{}".format(num_count_answer+1, list_answer[num_count_answer]), end=" ")
    print("-----------------")

print("End program!")
