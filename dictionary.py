# # character frequency

word = "banana"

def freq_cal(word):
    empt_dict = {}

    for i in word:
        if i in empt_dict:
            empt_dict[i] +=1
        else:
            empt_dict[i] = 1
    return empt_dict


print(freq_cal(word))