import json
import re
import numpy as np


def filter_word(w):
    return re.sub('[().,!@#$?:;]<>', '', w).lower()
def get_vocab(word_list):
    return {word:index for (index, word) in enumerate(set(word_list))}
def get_indexes(fname):
    lyrics = json.load(open(fname))
    word_list  = [filter_word(word) for word in " <eos> ".join(lyrics).replace("\\n\\n", "\\n").replace("\\n", " <eos> ").replace("\"", " ").split()]
    vocab = get_vocab(word_list)
    json.dump(vocab, open("vocab_indexes.json", "w+"))
    return [vocab[word] for word in word_list]
def get_data(fname, pct=1):
    total = np.array(get_indexes(fname), dtype=np.int32)
    return np.split(total[:int(pct*len(total))], [int(.7*pct*len(total)), int(.9*pct*len(total))]), max(total)+1
if __name__ == "__main__":
    json.dump(get_indexes("country_lyrics.json"), open("indexes.json", "w+"))
    #train, test, val = get_data('country_lyrics.json')
    #print len(train), len(test), len(val)
>>>>>>> parent of a016d59... fixed merge colflictsgit diff! :)
