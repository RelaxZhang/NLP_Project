import random

'''Remove stopwords from claim and evidence for reducing the computational consumption'''
def stopwords_func(stop_words, text_type, text_data):
    if text_type == "evidence":
        for i in text_data:
            sentence = text_data[i]
            words = sentence.split()
            filtered_words = [word for word in words if word.lower() not in stop_words]
            filtered_sentence = " ".join(filtered_words)
            text_data[i] = filtered_sentence
    else:
        for i in text_data.values():
            sentence = i["claim_text"]
            words = sentence.split()
            filtered_words = [word for word in words if word.lower() not in stop_words]
            filtered_sentence = " ".join(filtered_words)
            i["claim_text"] = filtered_sentence
    return text_data

'''Function for picking random keys from the dictionary after excluding the specified key(s)'''
def pick_random_keys(dictionary, excluded_keys, num_keys):
    available_keys = [key for key in dictionary.keys() if key not in excluded_keys]
    random_keys = random.sample(available_keys, num_keys)
    return random_keys

'''Function for turning the text into lowercase expression'''
def lower_processing(data, text_type):
    if text_type == "claim_text":
        for i in data:
            data[i][text_type] = data[i][text_type].lower()
    else:
        for i in data:
            data[i] = data[i].lower()
    return data