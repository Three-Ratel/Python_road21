from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from . import models


def login_status(func):
    def inner(request, table, *args, **kwargs):
        status = request.session.get('login')
        # print(status, type(status))
        # status = request.COOKIES.get('login', None)
        # status = request.get_signed_cookie('login', salt='', default='')

        if status != '1':
            return redirect('/login/?return_url=/{}/'.format(table))
        return func(request, table, *args, **kwargs)

    return inner


def login_status_fun(func):
    def inner(request, *args, **kwargs):
        # status = request.COOKIES.get('login')
        # status = request.get_signed_cookie('login', salt='', default='')
        status = request.session.get('login')
        if status != '1':
            return redirect('/login/?return_url={}'.format(request.path_info))
        return func(request, *args, **kwargs)

    return inner


class Login(View):
    # @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        return render(request, 'login.html')

    # @method_decorator(csrf_protect)
    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'henry' and pwd == '123':
            url = request.GET.get('return_url', '/book/')
            response = redirect('{}'.format(url))
            # response.set_cookie('login', 1)
            # response.set_signed_cookie('login', '1', salt='')
            request.session['login'] = '1'
            return response
        return render(request, 'login.html', {'error': '用户名或密码错误'})


def logout(request):
    ret = redirect(reverse('login'))
    ret.set_cookie('login', '')
    return ret


@method_decorator(login_status, 'dispatch')
class List_item(View):

    def get(self, request, table):
        obj = getattr(models, table.capitalize())
        all_item = ''
        if obj:
            all_item = obj.objects.all()
        return render(request, 'list_{}.html'.format(table), {'all_item': all_item, 'table': table})


# 删除元素
@login_status_fun
def del_item(request, table, pk):
    obj = getattr(models, table.capitalize())
    obj.objects.filter(pk=pk).delete()
    return redirect(reverse('list', args=(table,)))


# 编辑作者
@login_status_fun
def edit_author(request, pk):
    error = ''
    author = models.Author.objects.get(pk=pk)
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        books = request.POST.getlist('books')
        if not author_name:
            error = '请输入作者姓名'
        if not error:
            author.name = author_name
            author.save()
            author.books.set(books)
            return redirect(reverse('list', args=('author',)))
    all_book = models.Book.objects.all()
    print(all_book, type(all_book))
    return render(request, 'edit_author.html', {'author': author, 'all_book': all_book, 'error': error})


# 增加作者
@login_status_fun
def add_author(request):
    error = ''
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        if models.Author.objects.filter(name=author_name):
            error = '作者已存在'
        books = request.POST.getlist('books')
        if not (author_name and books):
            error = '作者和作品信息不完整'
        if not error:
            author = models.Author.objects.create(name=author_name)
            author.books.set(books)
            return redirect(reverse('list', args=('author',)))
    all_book = models.Book.objects.all()
    return render(request, 'add_author.html', {'all_book': all_book, 'error': error})


# 添加书籍
@login_status_fun
def add_book(request):
    error = ''
    if request.method == 'POST':
        title = request.POST.get('book_name')
        pk = request.POST.get('id')
        print(title, pk)
        book_set = models.Book.objects.filter(title=title, pub_id=pk)

        if book_set:
            error = '书籍已存在'

        if not title: error = '请输入书名'

        if not error:
            models.Book.objects.create(title=title, pub_id=pk)
            return redirect(reverse('list', args=('book',)))

    all_publisher = models.Publisher.objects.all()
    return render(request, 'add_book.html', {'all_publisher': all_publisher, 'error': error})


# 编辑书籍
@login_status_fun
def edit_book(request, pk):
    error = ''
    book = models.Book.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('book_name')
        pub_id = request.POST.get('id')
        if book.title == title and book.pub_id == int(pub_id):
            error = '未做任何修改'
        if not title: error = '请输入书名'
        if models.Book.objects.filter(title=title, pub_id=pub_id):
            error = '该书籍已存在'
        if not error:
            book.title = title
            book.pub_id = pub_id
            book.save()
            return redirect(reverse('list', args=('book',)))

    all_publisher = models.Publisher.objects.all().order_by('pid')
    return render(request, 'edit_book.html', {'book': book, 'all_publisher': all_publisher, 'error': error})


# 增加出版社
@login_status_fun
def add_publisher(request):
    error = ''
    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')
        if models.Publisher.objects.filter(name=publisher_name):
            error = '出版社已存在'
        if not publisher_name:
            error = '内容不能为空'
        if not error:
            models.Publisher.objects.create(name=publisher_name)
            return redirect(reverse('list', args=('publisher',)))
    return render(request, 'add_publisher.html', {'error': error})


# 修改出版社
@login_status_fun
def edit_publisher(request, pk):
    obj_li = models.Publisher.objects.filter(pk=pk)
    if not obj_li:
        return HttpResponse('编辑的信息不存在')

    error = ''
    obj = obj_li[0]
    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        if not name:
            error = '内容不能为空'
        if models.Publisher.objects.filter(name=name):
            error = '出版社名称已存在'
        if obj.name == name:
            error = '未做修改'
        if not error:
            obj.name = name
            obj.save()
            return redirect(reverse('list', args=('publisher',)))
    return render(request, 'edit_publisher.html', {'name': obj.name, 'error': error})
