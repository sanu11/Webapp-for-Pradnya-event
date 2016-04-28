from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Junior,Senior,jquestions,squestions
from django.http import HttpRequest,HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import csv
from django.conf import settings
import random
import sys
from datetime import datetime
from django.utils import timezone

m_score = 0
m_time = 1800
m_percentage= 50
#adding ques to db..run only once
def db():
    s=settings.BASE_DIR+'/static/Juniors.csv'
    with open(s) as csvfile:
        reader = csv.DictReader(csvfile)
        i=1
        for row in reader:
            que= row['Question']
            op1= row['Option 1']
            op2= row['Option 2']
            op3= row['Option 3']
            op4= row['Option 4']
            ans=row['Answer']
            x=jquestions(qid=i,question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans)
            x.save()
            i=i+1

#sign up
def register(request):
    if request.method=="POST":
        get_mail=request.POST["email"]
        if(Senior.objects.filter(email=get_mail).exists() or Junior.objects.filter(email=get_mail).exists()):
            return HttpResponse('Exists')
        else:
            if(request.POST["level"]=="Junior"):
                c=Junior()
            else:
                c=Senior()
            mail=request.POST["email"]    
            c.user1=request.POST["user1"]
            c.user2=request.POST["user2"]
            c.college=request.POST["college"]
            c.phone=request.POST["phone"]
            c.email=mail
            c.password=request.POST["password"]
            c.save()
            request.session['email']= mail          #send cookie
            return HttpResponse('success');
    else:
        return HttpResponse('Error');
           
def login(request):
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    if(request.method=="POST"):
        get_mail=request.POST["email"]
        d=Senior.objects.filter(email=get_mail).exists()   #check if user exists
        c=Junior.objects.filter(email=get_mail).exists()
        get_pw=request.POST["password"]

# user in junior
        if (c==True):
            check_junior=Junior.objects.get(email=get_mail)
            if(check_junior.password==get_pw):
                flag1=1                                 
            else:
                flag2=1                                 #wrong pw
#user in senior       
        elif(d==True):
            check_senior=Senior.objects.get(email=get_mail)
            if(check_senior.password==get_pw):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                flag3=1                                  
            else:
                flag4=1                                 #wrong pw

#accordingly getting cookies and redirecting to instruct using check.js
        
        if(flag1==1): 
            request.session['email']=get_mail
            print request.session['email']
            request.session['level']="junior"
            return HttpResponse('Success')          #success in junior            
        elif(flag3==1):
            request.session['email']=get_mail
            request.session['level']="senior"
            print get_mail, "Senior"
            return HttpResponse('Success')          #success  in senior
        elif(flag2==1 or flag4==1): 
            return HttpResponse('Wrong')                            #wrong pw                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           se('Wrong')           #wrong pw
        else:
            return HttpResponse('Exists')                           #User doesnt exist
    else:
        return HttpResponse('Enter')                   
        
#first page
def index(request):
	con={}
	return render(request,'index.html',con)

#instruction page
def enter(request):
    return render(request,'register.html',{})

#fetch questions
def logout():
    print "in lgout"
    del request.session['email']
    del request.session['level']
    request.session.modified = True
    print "end"

def get_time():
    curr_time=str(datetime.now().strftime('%H %M %S'))
    curr_time=curr_time.split(' ')  
    curr_time=map(int,curr_time)                                      
    total_curr_time=curr_time[0]*3600+curr_time[1]*60+curr_time[2];
    return total_curr_time

#for first question
def get_ques(request):
    global m_score
    print "in get_ques"
    get_mail=request.session['email']
    get_level=request.session['level']
    if(get_level=="junior"):
        obj=Junior.objects.get(email=get_mail)
    else:
        obj=Senior.objects.get(email=get_mail)
    #if contest didnt end yet then show ques
    if(obj.flag==0):
        if(not obj.array):
            print "in not obj array"
            r=random.randint(1,21)
            if get_level=="junior":
                curr_que=jquestions.objects.get(qid=r)
            else:
                curr_que=squestions.objects.get(qid=r)
            string=str(r)
            obj.array=string
            #contest started
            total_curr_time=get_time()
            obj.logintime=total_curr_time
            obj.save()
            time=m_time
            request.session['time']=time
            return render(request,'samp.html',{"score":obj.score,"q":curr_que,"time":time,"percent":obj.percent})        
        else:
            fetched_arr=map(str,obj.array.split(','))       #questions array
            #int arry
            fetched_arr=map(int,fetched_arr)
            index=len(fetched_arr)
            print index
            #checl if questions exists in db
            if(index!=21):
                r=random.randint(1,21)
                while(r in fetched_arr):
                    r=random.randint(1,21)
                if get_level=="junior":
                    curr_que=jquestions.objects.get(qid=r)
                else:
                    curr_que=squestions.objects.get(qid=r)
                x=str(r)
                string=obj.array
                string=string+','+x
                obj.array=string
                obj.save()
                print obj.logintime
                total_time=get_time()
                time_diff=total_time-int(obj.logintime)
                time_diff=m_time-time_diff
                if time_diff<=0:
                    obj.timestamp = 0
                else:
                    obj.timestamp=time_diff
                obj.save()
                if obj.timestamp==0:
                    return HttpResponseRedirect("/timeup")
                return render(request,'samp.html',{"score":obj.score,"q":curr_que,"time":obj.timestamp,"percent":obj.percent})        
            #if end of questions in db logout
            else:
                obj.flag=1
                obj.save()
                del request.session['email']
                del request.session['level']
                print obj.score
                return render(request,'limit.html',{"score":obj.score,"percent":obj.percent}) 
    #if contest already ended
    else:
        del request.session['email']
        del request.session['level']
        #print "hi"
        return render(request,'result.html',{"score":obj.score,"percent":obj.percent})    

#for rest que
def ques(request):
    global m_score
    print "in ques"

    get_mail=request.session['email']
    get_level=request.session['level']
    if(get_level=="junior"):
        obj=Junior.objects.get(email=get_mail)
    else:
        obj=Senior.objects.get(email=get_mail)
    if(obj.flag==0):
        found=0
        fetched_arr=map(str,obj.array.split(','))       #questions array
        index=len(fetched_arr)
        #int array
        fetched_arr=map(int,fetched_arr)
        #check for pqid from post request. If refresh then same pqid dont update ans. display same que else update all
        if("qid" in request.POST):
            pqid=request.POST.get("qid")
        #if refersh found=1
        else:
            qid=fetched_arr[index-1]
            if(get_level=="junior"):
                curr_que=jquestions.objects.get(qid=qid)
            else:
                curr_que=squestions.objects.get(qid=qid)
            time_diff=get_time()-obj.logintime
            time_diff=m_time-time_diff
            obj.timestamp=time_diff
            obj.save()
            return render(request,'samp.html',{"q":curr_que,"time":time_diff,"score":obj.score,"percent":obj.percent})        
        #if refersh found=1
        if(int(pqid) in fetched_arr[:-1]):
            found=1
        #if not refresh get current ans    
        elif 'answer' in request.POST:
            print request.POST['answer']
            ans =request.POST['answer']
        else:
            curr_que=jquestions.objects.get(qid=pqid)
            time_diff=get_time()-obj.logintime
            time_diff=m_time-time_diff        
            obj.timestamp=time_diff
            obj.save()
            return render(request,'samp.html',{"message":"error","q":curr_que,"time":time_diff,"score":obj.score,"percent":obj.percent})    
        #print found
#if not refresh  then only append ans to array          
        if(not found):                                  
            if(obj.ans_array):                           #for 2nd que ans of 1st will be saved
                obj.ans_array=obj.ans_array + ","+str(ans)     #update ans array
            else:
                obj.ans_array=str(ans)         
            #check for correct ans   
            if get_level=="junior":
                prev_que=jquestions.objects.get(qid=pqid)    
            else:
                prev_que=squestions.objects.get(qid=pqid)
            correct_ans=prev_que.ans                 #correct ans
            if(correct_ans==ans):
                if obj.timestamp < 300 and obj.percent > m_percentage:
                    obj.percent_flag=1
                    
                obj.save()    
                if obj.percent_flag==1:
                    obj.score += 6
                else:
                    obj.score+=2
                obj.correct_count+=1
            else:
                if obj.timestamp < 300 and obj.percent > m_percentage:
                    obj.percent_flag =1
                    
                obj.save()
                if obj.percent_flag == 1:                        
                    obj.score -= 3
                else:
                    obj.score-=1
            obj.percent=obj.correct_count*100/(index)
            obj.save()
            print "correct" ,obj.correct_count 
            print obj.percent
            obj.save()
            m_score = obj.score
    #fetch curr_que
        if(index!=21):
     #if refresh display same que and calculate logintime-currenttime and send to server      
            if(found==1):
                print "refreshed!!!"
                if get_level=="junior":
                    curr_que=jquestions.objects.get(qid=fetched_arr[index-1])
                else:
                    curr_que=squestions.objects.get(qid=fetched_arr[index-1])
    #if  not refresh display another que
            else:
                r=random.randint(1,21)
                while(r in fetched_arr):
                    r=random.randint(1,21)
                if get_level=="junior":
                    curr_que=jquestions.objects.get(qid=r)
                else:
                    curr_que=squestions.objects.get(qid=r)
                x=str(r)
                string=obj.array
                string=string+','+x
                obj.array=string
                obj.save()
                print obj.array
        #send time to client
            print "Ans=",curr_que.ans
            time_diff=get_time()-int(obj.logintime)
            time_diff=m_time-time_diff        
            if time_diff<=0:
                obj.timestamp=0
            else:
                obj.timestamp=time_diff
            obj.save()
            print obj.timestamp
            print "hi"
            if obj.timestamp==0:
                HttpResponseRedirect('/timeup')
            return render(request,'samp.html',{"score":obj.score,"q":curr_que,"time":obj.timestamp,"percent":obj.percent})
      #if questions over
        else:
            obj.flag=1
            obj.save()
            percent=obj.percent
            del request.session['email']
            del request.session['level']
            return render(request,"limit.html",{"mail":get_mail,"score":obj.score,"percent":percent})
    else:
        return render(request,'result.html',{"score":obj.score,"percent":obj.percent,"percent":obj.percent})
 
def timeup(request):
    get_mail=request.session['email']
    get_level=request.session['level']
    if(get_level=="junior"):
        obj=Junior.objects.get(email=get_mail)
    else:
        obj=Senior.objects.get(email=get_mail)
    return render(request,'timeup.html',{"score":obj.score,"percent":obj.percent})
            

def result(request):
    get_mail=request.session['email']
    get_level=request.session['level']
    if(get_level=="junior"):
        obj=Junior.objects.get(email=get_mail)
    else:
        obj=Senior.objects.get(email=get_mail)    
    return render(request,"result.html",{"score":obj.score,"percent":obj.percent})

def log_out(request):
    get_mail=request.session['email']
    level=request.session['level']
    if(level=="junior"):
        obj=Junior.objects.get(email=get_mail)
    else:
        obj=Senior.objects.get(email=get_mail)
    score=obj.score
    del request.session['level']
    del request.session['email']
    print ""
    return render(request,"log_out.html",{"mail":get_mail,"score":score}) 
    
def timer(request):
    try:
        get_mail=request.session['email']
        get_level=request.session['level']
        if(get_level=="junior"):
            obj=Junior.objects.get(email=get_mail)
        else:
            obj=Senior.objects.get(email=get_mail)
        if(obj.timestamp!=0):
            obj.timestamp-=1
            obj.save()
        else:
            obj.flag=1
            obj.save()
            del request.session['email']
            del request.session['level']
            request.session.modified = True
            return HttpResponse('log_out')
        print obj.timestamp
    except:
        print ""
    return HttpResponse(obj.timestamp)

def leaderBoard(request):
    junior_list = list(Junior.objects.all().order_by('-score'))
    senior_list = list(Senior.objects.all().order_by('-score'))
    context = {
        "junior_list":junior_list[:5],
        "senior_list":senior_list[:5]
    }
    return render(request,"leaderboard.html",context)

def update_score(request):
    mail = request.session["email"]
    level = request.session["level"]
    if level=="junior":
        obj = Junior.objects.get(email=mail)
    else:
        obj = Senior.objects.get(email=mail)
    if request.method == "POST":
        if request.is_ajax():
            if obj.percent > 50:
                obj.percent_flag = 1
                obj.save()

                    # time=map(str,obj.logintime.split(' '))       #questions array            
                    # time=map(int,time)
                    # print  time         
                    # total_login_time=time[0]*3600+time[1]*60+time[2]
                    # curr_time=str(datetime.now().strftime('%H %M %S'))
                    # curr_time=curr_time.split(' ')  
                    # curr_time=map(int,curr_time)                                      
                    # total_curr_time=curr_time[0]*3600+curr_time[1]*60+curr_time[2];
                    # time_diff=total_curr_time-total_login_time
                    # print "login time",total_login_time
                    # print "curent time ",total_curr_time
                    # print "time after login " ,time_diff
