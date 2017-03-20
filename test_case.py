#!/usr/bin/python
# _*_ coding: utf-8 _*_
import os

caselist = os.listdir(r"/Users/interviewer/WorkPython/SeleniumPythonOne/test_case")
for a in caselist:
    s = a.split('.')[1:][0]
    if s=='py':
        os.system(r"/Users/interviewer/WorkPython/SeleniumPythonOne/test_case/%s 1>>log.txt 2>&1" %a)