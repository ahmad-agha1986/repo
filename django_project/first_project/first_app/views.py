from django.shortcuts import render, redirect
from first_app.models import AccessRecord,Topic,Webpage,Userr 
from first_app.forms import FormName, UserForm, UserProfileInfoForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# from django.urls import reverse




# Create your views here.




def index(request):
	Webpages_list = AccessRecord.objects.order_by('date')
	context = {'access_records':Webpages_list}
	return render(request,'first_app/index.html', context)

def user_s(request):
	users_list = Userr.objects.all()
	users_dict = {'users_info':users_list}
	return render(request,'first_app/user_s.html', context= users_dict )


def form_name_view(request):
	form = FormName()

	

	if request.method == 'POST':
		form = FormName(request.POST)
		if form.is_valid():
			print ('name:  '+form.cleaned_data['name'])
			print ('email: '+form.cleaned_data['email'])
			print ('text:  '+form.cleaned_data['text'])

	return render(request, 'first_app/form_page.html',{'form':form})


def users(request):
	form = NewUserForm()
	if request.method == "POST":
		form = NewUserForm(request.POST)


		if form.is_valid():
			form.save()
			# return index(request)
			return redirect('first_app:index')
		else:
			print('Error form invalid')

	return render(request,'first_app/users.html',{'form':form})



def register(request):
	registered = False 

	if request.method =='POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile= profile_form.save(commit= False)
			profile.user= user 

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form=UserForm()
		profile_form=UserProfileInfoForm

	return render (request,'first_app/registration.html',
		                    {'user_form':user_form,
		                     'profile_form':profile_form,
		                      'registered':registered})





def user_login(request):
	if request.method =="POST":

		username= request.POST.get('username')
		username.upper()
		password= request.POST.get('password')
		user= authenticate(username =username , password= password)
		if user:
			if user.is_active:
				login(request,user)
				return redirect('first_app:index')
			else:
				return HttpResponse('Account Not Active')
	else:
		print('someone tried to login and failed!')
		# print('username:{} and password:{}'.format (username,password))
		return render(request, 'first_app/login.html')




@login_required
def special(request):
    return HttpResponse ('You are logged out')




@login_required
def user_logout(request):
	logout(request)
	return redirect('first_app:index')

