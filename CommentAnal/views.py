# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from subprocess import call
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
import sys
import codecs
sys.path.append('/home/ducthang/Desktop/Comment/comment/CommentAnal/binhnp/spam_detection/libsvm/python/')
from train import *

# CommentAnal Function
def Comment(request):
    # comment = ''
    # check = ''
    # if(request.method == 'POST'):
    #     comment = request.POST['comment']
    #     print comment
    #     if (comment != ''):
    #         m = svm_load_model('spam.model')
    #         vocabs = load_vocabs('vocabs.obj')
    #         #message = u'fgjghkyhjkdgjdrgjhfgjghk'
    #         label = predict(m, vocabs, comment)
    #         print label
    #         if(label[0] == 0.0):
    #             check = 'showPass'
    #             print "ok"
    #         else:
    #             check = 'showFailed'
    #             print 'not ok'
    # data = {'check':check,'comment':comment}
    return render(request,'cmt.html')
    # return HttpResponse(json.dumps(data), content_type='application/json')

def Post(request):
    comment = ''
    check = ''
    if(request.is_ajax() and request.POST):
        comment = request.POST.get('comment')
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
    data = {'check':check,'comment':comment}
    return HttpResponse(json.dumps(data), content_type='application/json')

def AddTrain(request):
    if(request.method == 'POST'):
        comment = request.POST['comment-train']
        print "type: ", type(comment)
        print "cmt: " , comment
        with codecs.open('CommentAnal/binhnp/spam_detection/libsvm/python/train.txt','a', encoding='utf8') as fileTrain:
            print "open"
            comment = ".".join(comment.split("\n"))
            print comment
            print "type1:" , type((comment + '\n'))
            fileTrain.write(comment + '\n')
            print "comment-train: ", comment
            fileTrain.close()
    #call(["ls","-l"])
    return HttpResponseRedirect('/comment/')