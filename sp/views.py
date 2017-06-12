import datetime
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import re
from sp.models import Call, Profile
from sp.forms import CallUpdateForm, ProfileUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.utils import _parse_tags


class CallAdd(LoginRequiredMixin, CreateView):
    login_url = 'authorization'
    redirect_field_name = 'next'
    template_name_suffix = '_add'
    model = Call
    fields = ['type', 'city', 'name', 'description', 'card', 'tags']
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.cleaned_data['tags'] = [n.lower() for n in form.cleaned_data['tags']]
        # print(form.cleaned_data['tags'])
        # print(self.object)
        return super(CallAdd, self).form_valid(form)


class CallUpdate(UserPassesTestMixin, UpdateView):
    raise_exception = True
    template_name_suffix = '_update'
    model = Call
    form_class = CallUpdateForm
    success_url = reverse_lazy('success')

    def test_func(self):
        obj = super(CallUpdate, self).get_object()
        return self.request.user == obj.user_id

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.cleaned_data['tags'] = [n.lower() for n in form.cleaned_data['tags']]
        # print(form.cleaned_data['tags'])
        return super(CallUpdate, self).form_valid(form)


class CallDelete(UserPassesTestMixin, DeleteView):
    raise_exception = True
    template_name = 'sp/call_delete.html'
    model = Call
    success_url = reverse_lazy('my_calls')

    def test_func(self):
        obj = super(CallDelete, self).get_object()
        return self.request.user == obj.user_id


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'authorization'
    redirect_field_name = 'next'
    template_name = 'sp/profile.html'
    model = Profile
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('success')

    def get_object(self):
        return Profile.objects.get(user_id=self.request.user)


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'sp/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        now_date = datetime.date.today()
        if(self.object.birthday):
            delta = now_date - self.object.birthday
            context['age'] = int(delta.days / 365.25)
        return context


class CallDetail(DetailView):
    model = Call
    template_name = 'sp/call_detail.html'


class MyCallsList(LoginRequiredMixin, ListView):
    login_url = 'authorization'
    redirect_field_name = 'next'
    context_object_name = 'call_list'
    template_name = 'sp/my_calls_list.html'
    model = Call

    def get_queryset(self):
        call_list = Call.objects.filter(user_id=self.request.user)
        city = self.request.GET.get('city', '')
        type_call = self.request.GET.get('type', '')
        tags = self.request.GET.get('tags', '').lower()
        name = self.request.GET.get('name', '')
        name = re.sub('[^\w -]', '', name)
        name = re.sub(' +', ' ', name)
        words = name.split(' ')
        for word in words:
            call_list = call_list.filter(name__contains=word)
        description = self.request.GET.get('description', '')
        description = re.sub('[^\w -]', '', description)
        description = re.sub(' +', ' ', description)
        words_descr = description.split(' ')
        for word_descr in words_descr:
            call_list = call_list.filter(description__contains=word_descr)
        tags_arr = _parse_tags(tags)
        for tag in tags_arr:
            call_list = call_list.filter(tags__name__iexact=tag)
        if city:
            call_list = call_list.filter(city=city)
        if type_call == 'offer':
            call_list = call_list.filter(type=True)
        elif type_call == 'search':
            call_list = call_list.filter(type=False)

        sort_calls = self.request.GET.get('sort', '')
        if sort_calls == 'new':
            call_list = call_list.order_by('-date_time')
        elif sort_calls == 'names':
            call_list = call_list.order_by('name')
        elif sort_calls == 'have-card':
            call_list = call_list.order_by('-card')
        paginator = Paginator(call_list, 5)
        page = self.request.GET.get('page')
        try:
            call_list = paginator.page(page)
        except PageNotAnInteger:
            call_list = paginator.page(1)
        except EmptyPage:
            call_list = paginator.page(paginator.num_pages)
        return call_list


class UserCallsList(ListView):
    context_object_name = 'call_list'
    template_name = 'sp/user_calls_list.html'
    model = Call

    def get_queryset(self):
        call_list = Call.objects.filter(user_id_id=self.kwargs['user_id'])
        city = self.request.GET.get('city', '')
        type_call = self.request.GET.get('type', '')
        tags = self.request.GET.get('tags', '').lower()
        name = self.request.GET.get('name', '')
        name = re.sub('[^\w -]', '', name)
        name = re.sub(' +', ' ', name)
        words = name.split(' ')
        for word in words:
            call_list = call_list.filter(name__contains=word)
        description = self.request.GET.get('description', '')
        description = re.sub('[^\w -]', '', description)
        description = re.sub(' +', ' ', description)
        words_descr = description.split(' ')
        for word_descr in words_descr:
            call_list = call_list.filter(description__contains=word_descr)
        tags_arr = _parse_tags(tags)
        for tag in tags_arr:
            call_list = call_list.filter(tags__name__iexact=tag)
        if city:
            call_list = call_list.filter(city=city)
        if type_call == 'offer':
            call_list = call_list.filter(type=True)
        elif type_call == 'search':
            call_list = call_list.filter(type=False)

        sort_calls = self.request.GET.get('sort', '')
        if sort_calls == 'new':
            call_list = call_list.order_by('-date_time')
        elif sort_calls == 'names':
            call_list = call_list.order_by('name')
        elif sort_calls == 'have-card':
            call_list = call_list.order_by('-card')
        paginator = Paginator(call_list, 5)
        page = self.request.GET.get('page')
        try:
            call_list = paginator.page(page)
        except PageNotAnInteger:
            call_list = paginator.page(1)
        except EmptyPage:
            call_list = paginator.page(paginator.num_pages)
        return call_list

    def get_context_data(self, **kwargs):
        context = super(UserCallsList, self).get_context_data(**kwargs)
        context['user_obj'] = User.objects.get(id=self.kwargs['user_id'])
        return context


class AllCallsList(ListView):
    context_object_name = 'call_list'
    template_name = 'sp/home.html'
    model = Call

    def get_queryset(self):
        call_list = Call.objects.all()
        city = self.request.GET.get('city', '')
        type_call = self.request.GET.get('type', '')
        tags = self.request.GET.get('tags', '').lower()
        name = self.request.GET.get('name', '')
        name = re.sub('[^\w -]','', name)
        name = re.sub(' +',' ',name)
        words = name.split(' ')
        for word in words:
            call_list = call_list.filter(name__contains=word)
        description = self.request.GET.get('description', '')
        description = re.sub('[^\w -]', '', description)
        description = re.sub(' +', ' ', description)
        words_descr = description.split(' ')
        for word_descr in words_descr:
            call_list = call_list.filter(description__contains=word_descr)
        tags_arr = _parse_tags(tags)
        for tag in tags_arr:
            call_list = call_list.filter(tags__name__iexact=tag)
        if city:
            call_list=call_list.filter(city=city)
        if type_call == 'offer':
            call_list=call_list.filter(type=True)
        elif type_call == 'search':
            call_list = call_list.filter(type=False)

        sort_calls = self.request.GET.get('sort', '')
        if sort_calls == 'new':
            call_list = call_list.order_by('-date_time')
        elif sort_calls == 'users':
            call_list = call_list.order_by('user_id')
        elif sort_calls == 'have-card':
            call_list = call_list.order_by('-card')
        paginator = Paginator(call_list, 5)
        page = self.request.GET.get('page')
        try:
            call_list = paginator.page(page)
        except PageNotAnInteger:
            call_list = paginator.page(1)
        except EmptyPage:
            call_list = paginator.page(paginator.num_pages)
        return call_list


def success(request):
    return render(request, 'sp/success.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def authorization(request):
    context = {}
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=login, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if request.GET.get('next') is not None:
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(reverse('my_profile'))
        else:
            context.update({'error': 'Неправильный логин или пароль'})
    return render(request, 'sp/authorization.html', context)


def registration(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rpassword = request.POST.get('rpassword')
        errors = []
        if User.objects.filter(username=login):
            errors.append('Данный логин уже используется')
        if not re.match('^\w+$', login):
            errors.append('Логин может содержать только буквы, цифры и знаки подчеркивания')
        if len(login) > 20:
            errors.append('Длина логина должна быть не более 20-ти символов')
        # if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
            errors.append('E-mail не верный')
        if len(password) > 25:
            errors.append('Длина пароля должна быть не более 25-ти символов')
        if password != rpassword:
            errors.append('Введенные пароли не совпадают')
        if len(errors):
            return render(request, 'sp/registration.html', {'errors': errors})
        user = User.objects.create_user(username=login, password=password)
        if user:
            Profile.objects.create(user_id=user, e_mail=email)
            user = auth.authenticate(username=login, password=password)
            auth.login(request, user)
            return HttpResponseRedirect("{}?sended=True".format(reverse('registration')))
        return render(request, 'sp/registration.html', {'errors': 'Ошибка при регистрации пользователя'})
    else:
        return render(request, 'sp/registration.html', {"sended": request.GET.get("sended", False)})
