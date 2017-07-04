# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import sys
sys.path.append('/home/ducthang/Desktop/Comment/comment/CommentAnal/binhnp/spam_detection/libsvm/python/')
from train import *

# CommentAnal Function
def Comment(request):
    comment = ''
    check = ''
    if(request.method == 'POST'):
        comment = request.POST['comment']
        print comment
        if (comment != ''):
            m = svm_load_model('spam.model')
            vocabs = load_vocabs('vocabs.obj')
            #message = u'fgjghkyhjkdgjdrgjhfgjghk'
            label = predict(m, vocabs, comment)
            print label
            if(label[0] == 0.0):
                check = 'showPass'
                print "ok"
            else:
                check = 'showFailed'
                print 'not ok'
    return render(request,'cmt.html',{'check':check,'comment':comment})