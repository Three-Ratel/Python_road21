from django.shortcuts import render
from datetime import datetime

# def my_test(request):
# re = Reporter.objects.all()
# print(re, type(re))
# return HttpResponse(' ok')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        return '咱也不知道，咱也不敢问'

    def __str__(self):
        return '<Person obj: {}-{}>'.format(self.name, self.age)


def my_test(request):
    hobby = ['movies', 'musics', 'reading', 'play badminton']
    li = [1, 2, 3, 4]
    dic = {1: 'a', 2: 'b', 3: hobby}
    person_obj = Person('henry', 19)
    return render(request, 'my_test.html',
                  {
                      'hobby': hobby,
                      'dic': dic,
                      'person_obj': person_obj,

                      'test': 'hello',
                      'file_size': 1*1024*1024*1024*1024*1024*1024,
                      'add': 2,

                      'hello': 'hEllo bugs',
                      'li':li,
                      's': 'welcome to China, welcome to BeiJing',
                      's1': '欢迎来北京游玩',
                      'now': datetime.now(),
                      'value': "<a href='#'>点我</a>",
                      'js':
                            """
                            <script>
                                for (var i = 0; i < 5; i++) {
                                    alert('11111')
                                }
                            </script>
                            """,
                        }


)
