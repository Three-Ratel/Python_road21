#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.http.request import QueryDict
from django.utils.safestring import mark_safe


class Pagenation:

    def __init__(self, request, all_num, params=None, per_page=10, max_item=11):
        """
        :param request: request请求对象
        :param all_num: 需要分页的数据量
        :param per_page: 每页需要展示的数据条数
        :param max_item: 显示的页码
        page：如果page为非数字需要进行异常处理，并设置其为1
        """
        try:
            page = int(request.GET.get('page', 1))
            page = 1 if page <= 0 else page
        except Exception:
            page = 1
        # 查询条件
        self.params = params
        if not self.params:
            self.params = QueryDict(mutable=True)
        # total_page: 分的总页数
        total_page, b = divmod(all_num, per_page)
        total_page = total_page + 1 if b else total_page
        # page 对超出边界的page进行限制
        page = page if page < total_page else total_page
        # end和start表示显示的起始页码, views函数需要
        self.end = page * per_page
        self.start = self.end - per_page
        half_item = max_item // 2
        # 表示页码的起始数
        self.start_page = page - half_item
        self.end_page = page + half_item
        # page表示当前页码
        self.page = page
        self.max_item = max_item
        self.total_page = total_page

        self.start_page = 1 if self.start_page <= 0 else self.start_page
        if self.end_page > self.total_page:
            self.start_page = self.total_page - self.max_item + 1
        self.end_page = self.start_page + self.max_item

        if self.start < 0:
            self.start = 1
            self.end = 1

    @property
    def show(self):

        li_li = []
        self.params['page'] = 1
        li_li.append(
            ' <li><a href="?{}" aria-label=""><span aria-hidden="true">首页</span></a></li>'.format(
                self.params.urlencode()))
        # 如果只有一页，表示起始页码均为1
        if self.start == self.end == 1:
            li_li.append('<li class="active"><a href="?{}">1</a></li>'.format(self.params.urlencode()))
        else:
            if self.page == 1:
                li_li.append(
                    ' <li style="display:none"><span aria-hidden="true">&laquo;</span></li>')
            else:
                self.params['page'] = self.page - 1
                li_li.append(
                    ' <li><a href="?{}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                        self.params.urlencode()))

            if self.total_page < self.max_item:
                self.start_page = 1
                self.end_page = self.total_page + 1

            for i in range(self.start_page, self.end_page):
                self.params['page'] = i
                # 通过if判断，当前页把其类设置为 active 表示活跃状态
                if self.page == i:
                    li_li.append('<li class="active"><a href="?{}">{}</a></li>'.format(self.params.urlencode(), i))
                else:
                    li_li.append('<li><a href="?{}">{}</a></li>'.format(self.params.urlencode(), i))

            # 如果当前页是最后一页，则隐藏下一页按钮，否则page加1
            if self.page == self.total_page:
                li_li.append(
                    '<li style="display:none"><span aria-hidden="true">&raquo;</span></li>')
            else:
                self.params['page'] = self.page + 1
                li_li.append(
                    '<li><a href="?{}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                        self.params.urlencode(), self.page + 1))

            # 尾页
            self.params['page'] = self.total_page
            li_li.append(
                ' <li><a href="?{}" aria-label="Previous"><span aria-hidden="true">尾页</span></a></li>'.format(
                    self.params.urlencode()))
        return mark_safe(''.join(li_li))