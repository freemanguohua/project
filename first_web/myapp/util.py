import tensorflow as tf
import tensorflow.keras.models as models
import numpy as np
import pandas as pd
from Bio import SeqIO

def pred_res(seq, k):
    model = models.load_model('new_model_2.h5')
    protein_id = []
    predicted_site = []
    for s in seq:
        protein = s.id
        ss = str(s.seq).upper()
        site = [i + 1 for i in range(len(ss)) if ss[i] == 'K']
        site = np.array(site)
        seq_matrix = char_win(site, ss, k)
        integer_matrix = encode_matrix(seq_matrix)
        integer_matrix = np.array(integer_matrix)
        pred_pro = model.predict(integer_matrix)
        #print(pred_pro)
        pred = np.squeeze(pred_pro, axis=-1)
        #print(pred)
        final_site = site[pred > 0.5]
        protein_id.extend([protein] * final_site.shape[0])
        predicted_site.extend(final_site)
    #res = zip(protein_id, predicted_site)
    #res.to_csv('predicted_site.csv')
    print('saved! ')
    return protein_id,predicted_site


def char_win(a, seq, k):
    a = a - 1  # a is list or array containing modification sites
    n = len(seq)  # seq is Seq object containing proteins sequence
    seq_list = []
    for i in a:
        if i - k < 0:
            s = seq[:i + k + 1].rjust(2 * k + 1, 'X')
        elif i + k >= n:
            s = seq[i - k:].ljust(2 * k + 1, 'X')
        else:
            s = seq[i - k:i + k + 1]
        seq_list.append(s)
    return seq_list


def encode_matrix(seq_matrix):
    ind_to_char = ['X', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'V', 'W', 'Y', 'B']
    char_to_ind = {char: i for i, char in enumerate(ind_to_char)}
    return [[char_to_ind[i] for i in s] for s in seq_matrix]


