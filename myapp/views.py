from django.shortcuts import render, redirect
from .models import pg_data, user_data
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import os
from PIL import Image
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    # pg_dta=pg_data.objects.all()
    # context={'pg_dta': pg_dta}
    return render(request, 'search.html')

def searchdata(request):
    query = request.GET.get("q")
    context_query=0
    if request.method=='POST' and query !="" and query !=" ":
        # print(query)
        #Context QUERY to send to HTML Page
        context_query=1

        #WRITE THE FILTER QUERY HERE--------------
        filter_price = int(request.POST.get("price_input"))
        filter_price_q = filter_price  * 1000
        filter_distance = int(request.POST.get("distance_input"))
        filter_distance_q = filter_distance * 100
        sorting = request.POST.get("sort")
        # print(type(filter_price), filter_price, type(filter_price_q), filter_price_q, type(filter_distance), filter_distance, type(filter_distance_q), filter_distance_q)
        if filter_price_q ==10000 and filter_distance_q==1000:
            if sorting=="s_dist":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).order_by('distance')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            elif sorting=="s_price":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).order_by('price')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            else:
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).order_by('-id')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
        
        elif filter_price_q < 10000 and filter_distance_q==1000:
            # print("inside less than price")
            if sorting=="s_dist":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(price__lte=filter_price_q).order_by('distance')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            elif sorting=="s_price":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(price__lte=filter_price_q).order_by('price')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            else:
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(price__lte=filter_price_q).order_by('-id')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
        elif filter_price_q == 10000 and filter_distance_q < 1000:
            # print("inside less than price")
            if sorting=="s_dist":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(distance__lte=filter_distance_q).order_by('distance')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            elif sorting=="s_price":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(distance__lte=filter_distance_q).order_by('price')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            else:
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(distance__lte=filter_distance_q).order_by('-id')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
        else:
            if sorting=="s_dist":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(price__lte=filter_price_q).filter(distance__lte=filter_distance_q).order_by('distance')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            elif sorting=="s_price":
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(price__lte=filter_price_q).filter(distance__lte=filter_distance_q).order_by('price')
                # context={'pg_dta': pg_dta}
                # return render(request, 'search.html', context)
            else:
                pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).filter(price__lte=filter_price_q).filter(distance__lte=filter_distance_q).order_by('-id')

        context={'pg_dta': pg_dta, 'filter_price': filter_price, 'filter_price_q': filter_price_q, 'filter_distance': filter_distance, 'filter_distance_q': filter_distance_q, 'sorting': sorting, 'context_query': context_query}
        return render(request, 'search.html', context)
            
    else:
        #Assigning the value we are getting through SEARCH BAR to 'query' named variable
        # query = request.GET.get("q")
        if query !="" and query !=" ":
            pg_dta=pg_data.objects.filter(status='active').filter(college__icontains=query).order_by('-id')
            context={'pg_dta': pg_dta, 'context_query':2}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html', {'context_query':2})
    
    
def result(request, post_id):
    # print(post_id)
    myobj = pg_data.objects.get(id=post_id)
    context={'myobj':myobj}
    return render(request, 'result.html', context)

def signup(request):
    if request.method=="POST":
        u_name = request.POST.get("name")
        u_email = request.POST.get("email")
        u_phone = request.POST.get("phone")
        u_password = request.POST.get("password")
        u_cpassword = request.POST.get("cpassword")
        # print(u_name, u_email, u_phone, u_password, u_cpassword)

        #Checking Password and Confirm Password matches or not
        if u_password == u_cpassword:
            # print("pass match")
            hashed_u_password = make_password(u_password)
            # print(hashed_u_password)

            # Query the database to check if the email exists in the user_data model
            existing_user = user_data.objects.filter(user_email=u_email).exists()

            if existing_user:
                # Email exists in the database (User is already registered)
                # print("Email exists.")
                #Message to be sent to user (Email already registered)
                messages.error(request,"The Email provided is already in use")
            else:
                # Email does not exist in the database
                # print("Email does not exist.")
                #Creating a Model Object and setting the data
                u=user_data()
                u.user_name=u_name
                u.user_email=u_email
                u.user_phone=u_phone
                u.user_password=hashed_u_password

                #SAVE the data
                u.save()

                #Message to be sent to user (Signup Success)
                messages.success(request,"Signup was Success, Now you can Login.")
                # print("Signup is Success")

                #Redirecting to Login Page after successful Signup
                return redirect('/login')

        else:
            # print("pass NO match")
            #Message to be sent to user (pass and Confirm pass does not match)
            messages.error(request,"Password and Confirm Password does not match")

        #Checking Email already exists or not

    return render(request, 'signup.html')

def login(request):

    #Fetching the data from the login Form
    if request.method=="POST":
        login_email = request.POST.get("l_email")
        login_password = request.POST.get("l_password")
        # print(login_email, login_password)

        #Checking if the email provided is registered or not
        existing_user = user_data.objects.filter(user_email=login_email).exists()

        if existing_user:
            # Email exists in the database (Authentic User)
            # print("Email exists.")

            #Fetching the password from the DB associated to the provided email
            user = user_data.objects.get(user_email=login_email)
            db_password = user.user_password
            
            #Checking whether the provided password and DB password matches or not
            if check_password(login_password, db_password):
                #Storing the EMAIL of user in the SESSION
                request.session['loggedin_email'] = login_email
                # print(request.session.get('loggedin_email'))///////////
                return redirect("/home")
                

            # Passwords match, proceed with login
            else:
                #Passing Message (WRONG PASSWORD)
                messages.error(request,"Wrong Email or Password")
        else:
            # Email does not exist in the database (NO USER FOUND)
            # print("Email does not exist.")
            #Passing Message (Email Does not exist
            messages.error(request,"Wrong Email or Password")

    return render(request, 'login.html')

def dashboard(request):
    if 'loggedin_email' in request.session:
        current_email = request.session.get('loggedin_email')
        if request.method=="POST":
            u_det_name = request.POST.get("user_det_name")
            u_det_phone = request.POST.get("user_det_phone")
            # print(u_det_name, u_det_phone)

            #Getting the Object with emaail the user is logged in
            udate_obj=user_data.objects.get(user_email=current_email)
            udate_obj.user_name=u_det_name
            udate_obj.user_phone=u_det_phone
            #Updating the DATA
            udate_obj.save()
            # print("DATA UPDATED")

            #Passing Message (Email Does not exist
            messages.success(request,"Data Updated Successfully")

            #Redirecting Back to Dashboard Page
            return redirect('/dashboard')
        # -------------------------------------
        current_email = request.session.get('loggedin_email')
        myobj = user_data.objects.get(user_email=current_email)

        #Name FIRST LETTER
        name_first_letter = myobj.user_name[0]

        #COunting Number Of TOTAL, ACTIVE, DEACTIVE POSTS
        total_post_count = pg_data.objects.filter(email=current_email).count()
        active_post_count = pg_data.objects.filter(email=current_email).filter(status='active').count()
        deactive_post_count = pg_data.objects.filter(email=current_email).filter(status='deactive').count()
        # print(total_post_count, active_post_count, deactive_post_count)

        context={'myobj':myobj, 'name_first_letter': name_first_letter, 'total_post_count':total_post_count, 'active_post_count':active_post_count, 'deactive_post_count':deactive_post_count}
        return render(request, 'dashboard.html', context)
    else:
        messages.warning(request, "You need to LOGIN in order to use Dashboard and related features")
        return redirect('/login')
    
def add_post(request):
    
    if 'loggedin_email' in request.session:
        if request.method=="POST":
            # ----------------------------------------------
            #Chceking that the all file fields are filled
            if 'pgpic1' in request.FILES and 'pgpic2' in request.FILES and 'pgpic3' in request.FILES:
                 pg_pic1 = request.FILES['pgpic1']
                 pg_pic2 = request.FILES['pgpic2']
                 pg_pic3 = request.FILES['pgpic3']
            else:
                # print("All the Image files must be selected")
                messages.error(request, "All the image fields must be filled")
                return redirect('/add-post')
            if pg_pic1.size > 0 and pg_pic2.size > 0 and pg_pic3.size > 0:
                # print("file exists")
                #Checking File is within 1MB or not
                if pg_pic1.size <= 1024 * 1024 and pg_pic2.size <= 1024*1024 and pg_pic3.size <= 1024*1024:
                    #File is within 1MB
                    # print("File is within 1MB")
                    try:
                        # Open the uploaded file (If opened, then it is Image, if not then it is not Image)
                        with Image.open(pg_pic1) as img:
                            #FILE IS WITHIN 1MB, and in IMAGE Format
                            #Fetching the Form Data
                            # print("data coming")
                            pg_name = request.POST.get("pgname")
                            pg_price = request.POST.get("pgprice")
                            pg_college = request.POST.get("pgcollege")
                            pg_address = request.POST.get("pgaddress")
                            pg_dist = request.POST.get("pgdist")
                            pg_dis = request.POST.get("pgdis")
                            pg_for = request.POST.get("pgfor")

                            #FETCHING some datas (Email and Phone) from the user_data MOdel
                            current_email = request.session.get('loggedin_email')
                            my_obj=user_data.objects.get(user_email=current_email)
                            current_phone = my_obj.user_phone

                            #Validation (Can be done here)

                            #Creating a Model Object and setting the data
                            p=pg_data()
                            p.name=pg_name
                            p.price=pg_price
                            p.college=pg_college
                            p.distance=pg_dist
                            p.address=pg_address
                            p.image1=pg_pic1
                            p.image2=pg_pic2
                            p.image3=pg_pic3
                            p.discription=pg_dis
                            p.email=current_email
                            p.phone=current_phone
                            p.pgfor=pg_for

                            #SAVE the data
                            p.save()

                            #Message to be sent to user (DATA UPLOADED)
                            messages.success(request,"New Post Uploaded Successfully")
                            # print("Within 1MB and in Image Format")
                            return redirect('/add-post')
                            
                    except Exception as e:
                        #File is not in image format
                        # print("Invalid image format.")
                        messages.error(request, "Only IMAGE type file formats are supported")
                else:
                    #File uploaded is greater than 1MB
                    # print("The files uploaded is Greater than 1MB")
                    messages.error(request, "The Files uploaded should not be Greater than 1MB")
            else:
                #File is not uploaded
                # print("file does not exists")
                messages.error(request, "All the IMAGE fields must be filled")
            
            # -------------------------------------------------
        return render(request, 'add-post.html')
    else:
        return redirect('/home')
    

def all_post(request):
    if 'loggedin_email' in request.session:
        current_email = request.session.get('loggedin_email')
        my_obj=pg_data.objects.filter(email=current_email)
        context={'my_obj':my_obj}
        return render(request, 'all-post.html', context)
    else:
        return redirect('/home')

def delete_post(request, post_id):
    current_email = request.session.get('loggedin_email')
    #AUTHORIZING THE USER
    auth_user=pg_data.objects.filter(email=current_email).filter(id=post_id)
    if auth_user:
        post_id=int(post_id)
        # print(type(post_id))
        # DELETING THE IMAGES OF THAT ROW
        my_obj=pg_data.objects.get(id=post_id)
        os.remove(my_obj.image1.path)
        os.remove(my_obj.image2.path)
        os.remove(my_obj.image3.path)
        #----------------------------------
        pg_data.objects.filter(id=post_id).delete()
        return redirect('/all-post')
    else:
        return redirect('/home')

def deactivate_post(request, post_id):
    # print(post_id)
    current_email = request.session.get('loggedin_email')
    #AUTHORIZING THE USER
    auth_user=pg_data.objects.filter(email=current_email).filter(id=post_id)
    if auth_user:
        #Authentic User is trying to deactivate
        # print(auth_user)
        my_obj=pg_data.objects.get(id=post_id)
        my_obj.status='deactive'
        #Updating the DATA
        my_obj.save()
        messages.success(request, "Post Deactivated Successfully")
        return redirect('/all-post')
    else:
        #Wrong User is trying to deactivate
        return redirect('/home')
    # return redirect('/all-post')

def activate_post(request, post_id):
    # print(post_id)
    current_email = request.session.get('loggedin_email')
    #AUTHORIZING THE USER
    auth_user=pg_data.objects.filter(email=current_email).filter(id=post_id)
    if auth_user:
        #Authentic User is trying to Activate
        # print(auth_user)
        my_obj=pg_data.objects.get(id=post_id)
        my_obj.status='active'
        #Updating the DATA
        my_obj.save()
        messages.success(request, "Post Activated Successfully")
        return redirect('/all-post')
    else:
        #Wrong User is trying to Activate
        return redirect('/home')

def edit_post(request, post_id):

    current_email = request.session.get('loggedin_email')
    #AUTHORIZING THE USER
    auth_user=pg_data.objects.filter(email=current_email).filter(id=post_id)
    if auth_user:
        my_obj=pg_data.objects.get(id=post_id)

        if request.method=="POST":
            if 'pgpic1' in request.FILES:
                pg_pic1 = request.FILES['pgpic1']
                if pg_pic1.size > 0 and pg_pic1.size <= 1024 * 1024:
                    # print("Has a file")
                    os.remove(my_obj.image1.path)
                else:
                    messages.error(request, "The Image size should not be more than 1MB")
                    return redirect('/edit-post/'+ post_id)
                my_obj.image1=pg_pic1
            
            if 'pgpic2' in request.FILES:
                pg_pic2 = request.FILES['pgpic2']
                if pg_pic2.size > 0 and pg_pic2.size <= 1024 * 1024:
                    # print("Has a file")
                    os.remove(my_obj.image2.path)
                else:
                    messages.error(request, "The Image size should not be more than 1MB")
                    return redirect('/edit-post/'+ post_id)
                my_obj.image2=pg_pic2

            if 'pgpic3' in request.FILES:
                pg_pic3 = request.FILES['pgpic3']
                if pg_pic3.size > 0 and pg_pic3.size <= 1024 * 1024:
                    # print("Has a file")
                    os.remove(my_obj.image3.path)
                else:
                    messages.error(request, "The Image size should not be more than 1MB")
                    return redirect('/edit-post/'+ post_id)
                my_obj.image3=pg_pic3

            pg_name = request.POST.get("pgname")
            pg_price = request.POST.get("pgprice")
            pg_college = request.POST.get("pgcollege")
            pg_dist = request.POST.get("pgdist")
            pg_address = request.POST.get("pgaddress")
            pg_dis = request.POST.get("pgdis")
            pg_for = request.POST.get("pgfor")

            my_obj.name=pg_name
            my_obj.price=pg_price
            my_obj.college=pg_college
            my_obj.distance=pg_dist
            my_obj.address=pg_address
            my_obj.discription=pg_dis
            my_obj.pgfor=pg_for
            my_obj.save()
            messages.success(request, "Data Updated Successfully")
            return redirect('/all-post')

        # print(post_id)
        # my_obj=pg_data.objects.get(id=post_id)
        context={'my_obj':my_obj}
        return render(request, 'edit-post.html', context)
    else:
        #Wrong User is trying to Activate
        return redirect('/home')

    

def logout(request):
    if 'loggedin_email' in request.session:
        del request.session['loggedin_email']
        return redirect('/home')
    else:
        return redirect('/home')



# def delall(request):
#     pg_data.objects.all().delete()
#     return redirect('/home')