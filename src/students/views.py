from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView
from django.contrib.auth.views import LoginView
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.templatetags.staticfiles import static
import datetime
import pandas as pd
import os
from django.contrib.staticfiles import finders
# from django.views.generic.edit import UpdateView
from .models import StudentInfo
from .forms import StudentAddForm, StudentInfoCreateForm
from django.contrib.auth import authenticate, login
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CustomLoginView(LoginView):
	template_name = 'login.html'
		
class ContactTView(TemplateView):
	template_name = 'contact.html'

class StudentLView(LoginRequiredMixin, ListView):
	template_name = 'students/list_view.html'
	login_url	=	'/login/'

	def get_queryset(self):
		query				=	self.request.GET.get('q')
		order_by			=	self.request.GET.get('order_by')
		reverse				=	self.request.GET.get('rev')
		gender_select		=	self.request.GET.get('gender_select')
		state_select		=	self.request.GET.get('state_select')
		top_n				=	self.request.GET.get('top_n')

		if any([query, order_by, reverse, gender_select, state_select, top_n]):
			if not query: query = ''
			if not order_by: order_by = 'name'
			if not reverse: self.reverse = False
			else: 	self.reverse = True
			if not gender_select: gender_select = ''
			if not state_select: state_select = ''
			if not top_n: top_n = 100

			qs, self.total_qcount = StudentInfo.objects.search(		query 		  = query, 
																	order_by 	  = order_by, 
																	reverse 	  = self.reverse, 
																	gender_select = gender_select,																
																	state_select  = state_select,
																	top_n		  = int(top_n),
																	user 		  = self.request.user,
														)
			return qs
		if not reverse: self.reverse = False
		self.total_qcount = StudentInfo.objects.filter(owner = self.request.user).count()
		return StudentInfo.objects.filter(owner = self.request.user).order_by('name')[:100]

	def get_context_data(self, *args, **kwargs):
		context = super(StudentLView, self).get_context_data(*args, **kwargs)
		context['states_list']		=	[i[0] for i in StudentInfo.objects.order_by().values_list('state').distinct()]
		context['states_list'].sort()

		context['query']			=	self.request.GET.get('q')
		context['order_by']			=	self.request.GET.get('order_by')
		context['reverse']			=	self.reverse
		context['gender_select']	=	self.request.GET.get('gender_select')
		context['state_select']		=	self.request.GET.get('state_select')
		context['total_qcount']		=	self.total_qcount

		return context

class StudentDetails(LoginRequiredMixin, DetailView):
	template_name 	= 'students/detail_view.html'
	queryset 		= StudentInfo.objects.all()
	login_url		=	'/login/'

	def get_context_data(self, *args, **kwargs):
		context = super(StudentDetails, self).get_context_data(*args, **kwargs)
		if context['object'].gender == 'F':folder = f"students/images/images_id/girls/{context['object'].reg_no}.png"
		elif context['object'].gender == 'M': folder = f"students/images/images_id/girls/{context['object'].reg_no}.png"
		else: folder = 'unknown'
		
		if finders.find(folder):
			context['image_id'] = static(folder)
		else:
			context['image_id'] = static('images/image_not_found.png')
		return context

class StudentInfoCreateView(LoginRequiredMixin ,CreateView):
	form_class 		= StudentInfoCreateForm
	template_name 	= 'students/new_entry.html'
	success_url 	= '/students/students_list/'
	login_url		= '/login/'

	def form_valid(self, form):
		instance 		= form.save(commit = False)
		instance.owner 	= self.request.user
		return super(StudentInfoCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context 			= super(StudentInfoCreateView, self).get_context_data(*args, **kwargs)
		context['title']	= 'New Entry'
		return context

class StudentInfoUpdateView(LoginRequiredMixin, UpdateView):
	template_name 	= 'students/update.html'
	model 			= StudentInfo
	fields 			= ['name', 'reg_no', 'cgpa', 'dob', 'section', 'contact', 'batch', 'address', 'department', 'description']
	login_url		=	'/login/'
	# success_url = f'/students/details/{slug}'

	def get_success_url(self):
		obj = StudentInfo.objects.get(pk=self.kwargs['pk'])
		return f'/students/details/{obj.slug}'

	def get_context_data(self, *args, **kwargs):
		context = super(StudentInfoUpdateView, self).get_context_data(*args, **kwargs)
		context['title']	=	'Update Student:'

		return context

class UploadStudentDetails(LoginRequiredMixin, TemplateView):
	template_name	=	'students/upload_stu_data.html'
	login_url		=	'/login/'

	def post(self, request,  *args, **kwargs):
		uploaded_file	=	self.request.FILES['docfile']
		fs = FileSystemStorage()
		file_name	=	fs.save(uploaded_file.name, uploaded_file)
		df 	=	pd.read_csv(f'data/{file_name}')
		df['DOB'] = pd.to_datetime(df.DOB)
		time_now = pd.Timestamp.now()
		handle	=	open(f'data/upload_logs/LOG for uploading file:{file_name}--{time_now}.txt', 'w+')

		for index, row in df.iterrows():
			try:
				reg_no 		=	row[0]
				name 		=	row[1]
				dob 		=	row[2]
				cgpa 		=	row[3]
				address 	=	row[4]
				section 	=	row[5]
				contact 	=	row[6]
				batch 		=	row[7]
				department 	=	row[8]
				gender		=	row[9]
				description	=	None
				
				

				if not cgpa: cgpa = float(0)
				if cgpa == None: cgpa = float(0)
				try: cgpa = float(cgpa)
				except: cgpa = float(0)

				

				if not address: address = ' '	


				StudentInfo.objects.create(owner = request.user, name = name, reg_no = reg_no, cgpa = cgpa, dob =  dob,section =  section, contact = contact, batch = batch, gender = gender, address = address, department = department, description = description)
			except:
				handle.write(f'Failed for {row}\n\n\n')
				
		return HttpResponse('''<br/><br/><br/><br/>
			<div style="text-align: center;">
			upload successful, data stored.<br/><br/>
			check here:
			<a href="/students/students_list/">Student List</a>
			</div>
			'''
			)


























