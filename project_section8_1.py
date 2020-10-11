# 8.6.1

#! python3
# make random quize and answer from 1 dictionary

# module import
import random
import os

if not os.path.exists:
    os.makedirs(".\\project8_1")

quize_dict = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "10", "k": "11", "l": "12", "m": "13", "n": "14", }

quize_amount_num = 35
for quize_num in range(quize_amount_num):

    quize_file_name = "quize_{}.txt".format(quize_num+1)
    ans_file_name = "answer_{}.txt".format(quize_num+1)

    quize_path = os.path.join(".", "project8_1", quize_file_name)
    ans_path = os.path.join(".", "project8_1", ans_file_name)

    # make file objects 
    quize_file_obj = open(quize_path, "w")
    ans_file_obj = open(ans_path, "w")

    # make header of quize
    quize_file_obj.write("name: \ndate: \nsemester: \n\n")
    quize_file_obj.write("quize_num: {}\n".format(quize_num+1))
    quize_file_obj.write("\n\n")

    # make header of answer
    ans_file_obj.write("Answer_sheet for No.{}\n\n".format(quize_num+1))

    # shuffle quize order
    alpha_codes_list = list(quize_dict.keys())
    random.shuffle(alpha_codes_list)

    # make choices of quize
    for question_num in range(len(quize_dict)):
        correct_ans = quize_dict[alpha_codes_list[question_num]]    # correct answer
        wrong_answer_list = list(quize_dict.values())
        wrong_answer_list.remove(correct_ans)                       # delete correct answer from wrong answer list
        wrong_answer_list = random.sample(wrong_answer_list, 3)
        ans_option_list = wrong_answer_list + [correct_ans]
        random.shuffle(ans_option_list)

        quize_file_obj.write("No.{}  What's the answer of {}?\n".format(question_num+1, alpha_codes_list[question_num]))
        quize_file_obj.write("Options\n")

        for i in range(4):
            quize_file_obj.write("{}. {}\n".format("WXYZ"[i], ans_option_list[i]))
        quize_file_obj.write("\n")

        print("correct ans: "+ str(correct_ans))
        print("ans_option_list: ", end = "")
        print(ans_option_list)

        ans_file_obj.write("No.{}  {}\n".format(question_num+1, "WXYZ"[ans_option_list.index(correct_ans)]))

    quize_file_obj.close()
    ans_file_obj.close()

# End of file