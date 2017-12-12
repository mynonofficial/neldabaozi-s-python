# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
BMI = weight/(height*height)

if BMI <18.5:
    print "过轻"
else:
    if BMI<25:
        print "正常"
    else:
        if BMI<28:
            print "过重"
        else:
            if BMI<32:
                print "肥胖"
            else:
                print "严重肥胖"
if...elif...else
