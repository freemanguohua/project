from Bio import SeqIO
# from django.shortcuts import render
from django.shortcuts import render_to_response,redirect


from django.http import HttpResponse

from myapp.form import UserForm
from myapp.models import User
from io import StringIO
from Bio import SeqIO
from myapp.util import pred_res
# import collections
from django.http import FileResponse

# import tensorflow as tf
# import numpy as np
# import pandas as pd


# from tensorflow.keras import Sequential, Model
# from tensorflow.keras.layers import Bidirectional, LSTM, Embedding, Dense, Dropout


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # 获取表单数据
            #print(username)
            content = form.cleaned_data['content']
            filename = form.cleaned_data['filename']  # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
            if (filename is None) and (len(content) ==0):
                return render_to_response('register.html', {'form': form})

            if filename is not None:
                t = filename.read()  # 读取他的内容，为bytes类型
                tt = str(t, encoding='utf-8')  # 转化为字符
                ttt = StringIO(tt)
                seq = SeqIO.parse(ttt, 'fasta')
                print('filename')
            else:
                ttt = StringIO(content)
                seq = SeqIO.parse(ttt, 'fasta')
            protein_id,predicted_site = pred_res(seq,15)
            pp = zip(protein_id,predicted_site)
            return render_to_response('result.html', {'athlete':pp})
    else:
        form = UserForm()
    return render_to_response('register.html', {'form': form})


def example(request):
    return render_to_response('example.html', {})

def pos_download(requst):
    file = open('train_pos.csv', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="pos_train.csv"'
    return response

def neg_download(request):
    file = open('train_neg.csv', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="neg_train.csv"'
    return response