from django.shortcuts import render,redirect

# Create your views here.
total=0
opt1=0
opt2=0
opt3=0
opt4=0
def home(request):
    global total,opt1,opt2,opt3,opt4
    question='1+2=?'
    o1=12
    o2=3
    o3=21
    o4=0
    Qus={'question':question,'o1':o1,'o2':o2,'o3':o3,'o4':o4}
    if request.method=="POST":
        get_result=request.POST.get('getresult')
        op1=request.POST.get('op1')
        op2=request.POST.get('op2')
        op3=request.POST.get('op3')
        op4=request.POST.get('op4')
        if op1:
            opt1+= 1
            total+=1
        if op2:
            opt2+= 1
            total+=1
        if op3:
            opt3+= 1
            total+=1
        if op4:
            opt4+= 1
            total+=1
        print("op values",opt1,opt2,opt3,opt4)
        if get_result:
            dict1={'polls':[]}
            lst1=[opt1,opt2,opt3,opt4]
            count1=1
            for i in lst1:
                count1+=1
                option='option'+str(count1)
                if i != 0:
                    dict2 = {}
                    if option not in dict1:
                        dict2['option'] = option
                        dict2['percentage'] = total / i
                        dict1['polls'].append(dict2)
                    else:
                        dict2['option']+=1
                        dict2['percentage'] = total / i
                else:
                    option='option'+str(i)
                    dict2['option'] = option
                    dict2['percentage'] = 0
                    dict1['polls'].append(dict2)
            print("dict1",dict1)
            print("dict2",dict2)
            return render(request,"votes.html",context=dict2)
        return redirect("home")
    return render(request,"votes.html",Qus)