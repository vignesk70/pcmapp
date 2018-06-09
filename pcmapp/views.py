from django.shortcuts import get_object_or_404, render
from django.db import transaction
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NewMemberRegistrationForm,SCCheckForm, CarRegistrationFormSet,PaymentFormSet
from .models import Member,Payment,Car
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#def index(request):
 #   member = Member.objects.all()
  #  context =  {'member' : member}
   # return render(request,'pcmapp/index.html', context)

class IndexView(generic.ListView):
    template_name = 'pcmapp/index.html'
    context_object_name = 'member'
    paginate_by = 10
    def get_queryset(self):
        return Member.objects.all()

#get details of car no
#def querymember(request, member_car_no):
 #   owner = Member.objects.get(member_car_no = member_car_no)
 #   context = {'owner': owner}
 #   return render(request,'pcmapp/memberdetail.html',context)

class DetailView(generic.DetailView):
    template_name = 'pcmapp/memberdetail.html'
    model = Member
    context_object_name = 'member'
    queryset = Member.objects.filter()

class PaymentInYearView(generic.ListView):
    template_name = 'pcmapp/paymentlist.html'
    model = Payment,Member
    context_object_name = 'payment'
    def get_queryset(self):
        return Payment.objects.all()

class NewRegistrationCreate(CreateView):
    model = Member
    template_name = 'pcmapp/newregistration.html'
    fields = ['member_name','member_email','member_phone','member_birthdate','member_address_state','member_address_postcode','member_on_chat','member_source']
    def get_context_data(self, **kwargs):
       context = super(NewRegistrationCreate, self).get_context_data(**kwargs)
       return context


class NewCarRegistrationCreate(CreateView):
    model = Car
    template_name = 'pcmapp/newcarregistration.html'
    fields = ['car_reg_no','car_model','car_engine_chasis']
    sucess_url = 'pcmapp:index'
    def get_context_data(self, **kwargs):
       context = super(NewCarRegistrationCreate, self).get_context_data(**kwargs)
       return context

class NewMemberRegistrationView(CreateView):
    template_name = 'pcmapp/newregistration.html'
    model = Member
    form_class = NewMemberRegistrationForm
    success_url = 'registrationsuccess'
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        car_form = CarRegistrationFormSet()
        receipt_form = PaymentFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  car_form=car_form,
                                  receipt_form=receipt_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        car_form = CarRegistrationFormSet(self.request.POST)
        receipt_form = PaymentFormSet(self.request.POST)
        if (form.is_valid() and car_form.is_valid() and receipt_form.is_valid()):
            return self.form_valid(form, car_form, receipt_form)
        else:
            return self.form_invalid(form, car_form, receipt_form)

    def form_valid(self, form, car_form, receipt_form):
        self.object = form.save()
        car_form.instance = self.object
        car_form.save()
        receipt_form.instance = self.object
        receipt_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, car_form,receipt_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  car_form=car_form,
                                  receipt_form=receipt_form))

class RegistrationSuccess(generic.TemplateView):
    template_name = 'pcmapp/registrationsuccess.html'

class SCcheckView(LoginRequiredMixin,generic.FormView):
    model=Car
    template_name = 'pcmapp/sccheck.html'
    form_class = SCCheckForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #carid = get_object_or_404(Car, car_reg_no=request.POST.get('car_reg_no'))
        #self.success_url = 'sccheckdetails/%s' % carid.pk
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self,form):
        carid = Car.objects.get(car_reg_no=form.cleaned_data['car_reg_no'])
        self.success_url = 'sccheckdetails/%s' % carid.pk
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self,form):
        return self.render_to_response(
            self.get_context_data(form=form))

class SCcheckDetailView(LoginRequiredMixin,generic.DetailView):
    model = Car
    template_name = 'pcmapp/sccheck_detail.html'
    def get_context_data(self, **kwargs):
        context =  super(SCcheckDetailView, self).get_context_data(**kwargs)
        context['car'] = Car.objects.get(pk=self.kwargs.get('pk',None))
        context['member'] = Member.objects.get(id=context['car'].pk)
        return context


class MemberDetailView(generic.DetailView):
    model=Member
    template_name='pcmapp/member_detail.html'

class NewMemberListView(generic.ListView):
    model=Member
    template_name= 'pcmapp/new_member_list.html'
    paginate_by=20
    queryset =  Member.objects.all().filter(member_expiry_date__isnull=True)
