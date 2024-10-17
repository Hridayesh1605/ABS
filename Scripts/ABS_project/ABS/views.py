from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,UpdateView
from .models import UserForm,App_User,ExtraUserDetForm,ExtraUserDet,Image,ImageForm,Designation,AmbulanceForm,BookForm,Book,Ambulance,Accepted_rides,Finished_rides
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')


def signIn(request):

    # userN = []
    # pass1 = []
    # user = User.objects.raw('SELECT id,username as u FROM user')
    # for i in user:
    #     userN.append(i.u)

    # pas = User.objects.raw('SELECT id,password as p FROM user')
    # for i in pas:
    #     pass1.append(i.p)

    # print(userN)
    # print(pass1)


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        app = App_User.objects.get(username=username)

        
        

        user = authenticate(request,username=username,password=password)
        
        
        print(user)

        if user is not None:
            request.session['uid']=app.id
            login(request,user)
            f_name = user.first_name
            id1 = app.id 
            x=Book.objects.all()
            if app.is_staff==True:
                return render(request,"staff_home.html",{'fname':f_name,'form':x})
            else:
                return render(request,"userHome.html",{'fname':f_name,'id1':id1})
            # return redirect('/')
        else:
            # messages.error(request,"bad credentials")
            return redirect('/login')

       



    else:
        return render(request,'login.html')
    return redirect('/userHome')
    # return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        
        auth_user_data = User.objects.create_user(username,email,password)
        auth_user_data.first_name = f_name
        auth_user_data.last_name = l_name

        # if User1.objects.filter(username=username):
        #     messages.error(request,"username already exists")
        #     return redirect('/register')

        if App_User.objects.filter(email=email):
            messages.error(request,"Email already exists")
            return redirect('/register')


        f=UserForm(request.POST)
        if f.is_valid():
            f.save()
            auth_user_data.save()
            # messages.success(request,'Account has been succesfully created')
            return redirect('/login')
        else:
            return render(request,'register.html',{'form':f})
        
    else:
        f = UserForm
        context={'form':f}
        return render(request,"register.html",context)

def admin(request):
    if request.method == "POST":
        name = request.POST['name']
        designation = request.POST['designat']
        staf_id = request.POST['staf_id']

        d=Designation()
        d.name = name
        d.designation = designation
        d.staf_id = staf_id
        d.save()
        redirect('/admin')
        # x=Designation.objects.all()
        # x.delete()


    '''
    Admin page pieChart
    '''
    labels=['2-15','15-20','20-25','25-30','30-35','35-40','Above 40']
    data=[]
    age1 = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE age>=1 and age<15 and is_user=1;')

    for cou in age1:
        data.append(cou.c)

    age2 = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE age>=15 and age<20 and is_user=1;')

    for cou in age2:
        data.append(cou.c)

    age3 = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE age>=20 and age<25 and is_user=1;')

    for cou in age3:
        data.append(cou.c)

    age4 = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE age>=25 and age<30 and is_user=1;')

    for cou in age4:
        data.append(cou.c)

    age5 = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE age>=30 and age<35 and is_user=1;')

    for cou in age5:
        data.append(cou.c)

    age6 = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE age>=35 and age<40 and is_user=1;')

    for cou in age6:
        data.append(cou.c)

    age7 = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE age>=40 and is_user=1;')

    for cou in age7:
        data.append(cou.c)

    noOfUser = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE is_user=1')
    noOfStaff = App_User.objects.raw('SELECT id,count(*) as c FROM user WHERE is_staff=1')
    noOfAmb = Ambulance.objects.raw('SELECT ambulance_id,count(*) as c FROM Ambulance')
    user=0
    st=0
    amb=0

    for cou in noOfUser:
        user = user+cou.c

    for staf in noOfStaff:
        st = st+staf.c

    for a in noOfAmb:
        amb = amb+a.c

        

    

    # data.append(age1.id)
    staff_det = App_User.objects.filter(is_staff=True)
    # print(staff_det.email)

    f=Book.objects.all()



    
    

    context={
        'labels':labels,
        'data':data,
        'user':user,
        'st':st,
        'staff':staff_det,
        'form':f,
        'amb':amb
    }
    return render(request,'admin.html',context)

def ulist(request):
    user = App_User.objects.filter(is_user=True)
    context = {'ul':user}
    return render(request,'ulist.html',context)

def slist(request):
    staff = App_User.objects.filter(is_staff=True)
    context = {'ul':staff}
    return render(request,'slist.html',context)

def delete(request,id1):
    user = App_User.objects.get(id=id1)
    user.delete()
    print(user.username)

    auth_del = User.objects.filter(username=user.username)
    auth_del[0].delete()

    # dell = User.objects.all()
    # dell.delete()

    return redirect('/user_list')

# def edit(request,id1):
#     user = User.objects.get(id=id1)
#     if request.method == 'POST':
#         f=UserForm(request.POST,instance=user)
#         f.save()
#         return redirect('/user_list')
#     else:
#         f=UserForm(instance=user)
#         return render(request,'register.html',{'form':f})

class editUser(UpdateView):
    model=App_User
    template_name='admin-user-edit.html'
    fields=['f_name','l_name','m_name','username','email','age','contact']
    success_url='/user_list'

# @login_required
def uHome(request):
    uid = request.session.get('uid')
    if uid is not None:
        return render(request,'userHome.html')
    else:
        return redirect('/login')


    
    


def signOut(request):
    logout(request)
    return redirect('/')

def s_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        m_name = request.POST['m_name']
        age = request.POST['age']
        contact = request.POST['contact']
        is_staff = True
        is_user = False

        auth_user_data = User.objects.create_user(username,email,password)
        auth_user_data.first_name = f_name
        auth_user_data.last_name = l_name

        e=App_User()
        e.username = username
        e.email = email
        e.password = password
        e.f_name = f_name
        e.l_name = l_name
        e.m_name = m_name
        e.age = age
        e.contact = contact
        e.is_staff = is_staff
        e.is_user = is_user
        e.save()
        auth_user_data.save()

        
        return redirect('/admin')
    else:
        f = UserForm
        context={'form':f}
        return render(request,"staffRegister.html",context)


def staffH(request):
    uid = request.session.get('uid')
    user = App_User.objects.get(id=uid)
    

    staff = user.f_name
    amb_no = Ambulance.objects.filter(Q(doctor=staff) | Q(cleaner=staff) | Q(driver=staff))
    for amb_nos in amb_no:
        ambulance_plate_no = amb_nos.ambulance_plate
    

    active_ride = Accepted_rides.objects.filter(accepted_by=staff).exists()

    # if active_ride == True:
    #     r = Accepted_rides.objects.all()
    #     r.delete()

    

    print(active_ride)
    print(ambulance_plate_no)

    if active_ride == True:
        ongoing = Accepted_rides.objects.get(accepted_by=staff)
        print(ongoing)
        context = {'active_form':ongoing,'user':user}
    else:
        print('asdfghjk')
        f=Book.objects.filter(ambulance_plate=ambulance_plate_no)
        context={'form':f,'user':user}

    if uid is not None:
        return render(request,"staff_home.html",context)
    else:
        return redirect('/login')
    



def addExtraUserDet(request):
    uid = request.session.get('uid')
    app_u = App_User.objects.get(id=uid)
    user_id = app_u.id
    
    

    if ExtraUserDet.objects.filter(user_id=user_id):
        
        extra = ExtraUserDet.objects.get(user_id=user_id)
        img = Image.objects.get(user_id=user_id)
        username = app_u.username
        f_name = app_u.f_name
        if request.method == 'POST':

            f=ExtraUserDetForm(request.POST,instance=extra)
            i=ImageForm(request.POST,request.FILES,instance=img)
            f.save()
            i.save()
            context={
                "id1":user_id,
                "fname":f_name,
            }
            # messages.error(request,"Email already exists")
            return render(request,'userHome.html',context)
        else:
            f=ExtraUserDetForm(instance=extra)
            i=ImageForm(instance=img)
            context={'form':f,'img':i}
            return render(request,"addExtraUserDet.html",context)
        # return redirect('/login')
    elif request.method == "POST":
        # app_u = App_User.objects.get(id=id1)
        user_id = user_id
        # print(user2)
        Addhar = request.POST['Addhar']
        Pan = request.POST['Pan']
        img = request.FILES.get('image')
        

        e=ExtraUserDet()
        i=Image()
        i.user_id = user_id
        i.image = img
        e.user_id = user_id
        e.Addhar = Addhar
        e.Pan = Pan
        e.save()
        i.save()

        # if ExtraUserDet.objects.filter(user_id=user_id):
        #     f=ExtraUserDetForm(request.POST,instance=app_u)
        #     f.save()
        #     # messages.error(request,"Email already exists")
        #     return redirect('/login')


        return redirect('/login')

    else:
        f = ExtraUserDetForm
        i=ImageForm
        context={'form':f,'img':i}
        return render(request,"addExtraUserDet.html",context)


def viewUDet(request):
    uid = request.session.get('uid')

    img = Image.objects.get(user_id=uid)
    extra = ExtraUserDet.objects.get(user_id=uid)
    user = App_User.objects.get(id=uid)

    print(img.image)

    context={'img':img,'extra':extra,'user':user}

    return render(request,'viewUDet.html',context)


def a_reg(request):
    if request.method == "POST":
        f=AmbulanceForm(request.POST)
        f.save()
        return redirect('/admin')
    else:
        f=AmbulanceForm
        context={'form':f}
    return render(request,'ambRegister.html',context)

def AmbulanceCard(request):
    uid = request.session.get('uid')
    amb = Ambulance.objects.all()
    context={'amb':amb}
    return render(request,'ambCard.html',context)


def book(request,id3):
    uid1 = request.session.get('uid')
    print(uid1)
    app_u = App_User.objects.get(id=uid1)
    ambulance=Ambulance.objects.get(ambulance_id=id3)
    # print(app_u)
    user_id = app_u.id
    # print(user_id)
    extra = ExtraUserDet.objects.get(user_id=user_id)
    if request.method == "POST":
        ambulance_plate=ambulance.ambulance_plate
        username = app_u.username
        email = app_u.email
        contact = app_u.contact
        Addhar = extra.Addhar
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        address = request.POST['address']

        e=Book()
        e.ambulance_plate=ambulance_plate
        e.username = username
        e.email = email
        e.contact = contact
        e.Addhar = Addhar
        e.curr_long = longitude
        e.curr_lat = latitude
        e.address = address
        e.save()
        return redirect('/message_after_book')

    else:
        f=BookForm
        context={'app_u':app_u,'extra':extra,'form':f}
        return render(request,'book.html',context)


def deleteb(request,id1):
    user = Book.objects.get(id=id1)
    user.delete()
    print(user.username)

    # auth_del = User.objects.filter(username=user.username)
    # auth_del[0].delete()

    # dell = User.objects.all()
    # dell.delete()

    return redirect('/admin')

def message_after_book(request):
    return render(request,'message_after_book.html')


def delete_rides(request,id3):
    print(id3)
    ride = Book.objects.get(id=id3)
    ride.delete()

    return redirect('/staff_home')

def accept_ride(request,id4):
    uid1 = request.session.get('uid')
    user = App_User.objects.get(id=uid1)

    ride = Book.objects.get(id=id4)
    e=Accepted_rides()
    e.accepted_by=user.f_name
    e.username = ride.username
    e.email = ride.email
    e.contact = ride.contact
    e.Addhar = ride.Addhar
    e.address = ride.address
    e.pikup_lat = ride.curr_lat
    e.pikup_long = ride.curr_long
    e.save()

    ride.delete()
    return redirect('/staff_home')


def finish_ride(request,id5):
    uid1 = request.session.get('uid')
    

    ride = Accepted_rides.objects.get(id=id5)
    staff = ride.accepted_by
    plate_no = Ambulance.objects.get(Q(doctor=staff) | Q(cleaner=staff) | Q(driver=staff))
    username = ride.username
    contact= ride.contact
    ambulance_plate = plate_no.ambulance_plate
    doctor = plate_no.doctor
    driver = plate_no.driver
    cleaner = plate_no.cleaner
    address = ride.address
    e=Finished_rides()
    e.username=username
    e.contact=contact
    e.ambulance_plate=ambulance_plate
    e.doctor=doctor
    e.driver=driver
    e.cleaner=cleaner
    e.address=address
    e.save()
    
    ride.delete()
    return redirect('/staff_home')

    

