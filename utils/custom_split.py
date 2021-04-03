def custom_split(str_to_split):
    ignore_flag = False
    word_acc = ""
    str_acc = ""
    word_list = []
    for letter in str_to_split:
        if ignore_flag:
            str_acc += letter
            if letter == '"':
                ignore_flag = False
                word_list.append(str_acc)
                str_acc = ""
        else:
            if letter == ' ':
                if word_acc:
                    word_list.append(word_acc)
                    word_acc = ""
            elif letter == '"':
                str_acc += letter
                ignore_flag = True
                if word_acc:
                    word_list.append(word_acc)
                    word_acc = ""
            else:
                word_acc += letter
    if word_acc:
        word_list.append(word_acc)
    if word_list[0][0] == '#':
        return []
    return word_list
