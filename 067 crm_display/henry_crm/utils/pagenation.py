#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Pagenation:

    def __init__(self, request, all_num, per_page=10, max_item=11):
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
        li_li.append(
            ' <li><a href="?page=1" aria-label="Previous"><span aria-hidden="true">首页</span></a></li>')
        if self.start == self.end == 1:
            li_li.append('<li class="active"><a href="?page=1">1</a></li>')
            li_li.append(
                ' <li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">尾页</span></a></li>'.format(
                    self.total_page))
        else:
            if self.page == 1:
                li_li.append(
                    ' <li class="disabled" style="display:none"><span aria-hidden="true">&laquo;</span></li>')
            else:
                li_li.append(
                    ' <li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                        self.page - 1))
            if self.total_page < self.max_item:
                self.start_page = 1
                self.end_page = self.total_page + 1
            for i in range(self.start_page, self.end_page):
                if self.page == i:
                    li_li.append('<li class="active"><a href="?page={}">{}</a></li>'.format(i, i))
                else:
                    li_li.append('<li><a href="?page={}">{}</a></li>'.format(i, i))
            if self.page == self.total_page:
                li_li.append(
                    '<li class="disabled"  style="display:none"><span aria-hidden="true">&raquo;</span></li>')
            else:
                li_li.append(
                    '<li><a href="?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                        self.page + 1))
            li_li.append(
                ' <li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">尾页</span></a></li>'.format(
                    self.total_page))
        return ''.join(li_li)
