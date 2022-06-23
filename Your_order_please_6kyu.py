# Your order, please

def order(sentence):
    if sentence == "":
        return ""
    else:    
        empt_str = ""
        split_sentence = sentence.split()
        lst_empt_str = []
        for is_nums in sentence:
            if is_nums.isdigit():
                empt_str = empt_str + is_nums
                lst_empt_str = empt_str
                result_list = [i for _,i in sorted(zip(lst_empt_str,split_sentence))]
        return " ".join(result_list)

print(order("is2 Thi1s T4est 3a"))