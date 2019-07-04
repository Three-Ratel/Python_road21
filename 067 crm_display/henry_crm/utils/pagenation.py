#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Pagenation:

    def __init__(self, request, all_num, per_page=10, max_item=11):
        try:
            page = int(request.GET.get('page', 1))
            page = 1 if page <= 0 else page
        except Exception:
            page = 1

        total_page, b = divmod(all_num, per_page)
        total_page = total_page + 1 if b else total_page
        page = page if page < total_page else total_page
        self.end = page * per_page
        self.start = self.end - per_page
        half_item = max_item // 2

        self.start_page = page - half_item
        self.end_page = page + half_item
        self.page = page
        self.max_item = max_item
        self.total_page = total_page

    @property
    def show(self):

        start_page = 1 if self.start_page <= 0 else self.start_page
        if self.end_page > self.total_page:
            start_page = self.total_page - self.max_item + 1
        end_page = start_page + self.max_item
        li_li = []
        if self.page == 1:
            li_li.append(
                ' <li class="disabled"><span aria-hidden="true">&laquo;</span></li>')
        else:
            li_li.append(
                ' <li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.page - 1))
        for i in range(start_page, end_page):
            if self.page == i:
                li_li.append('<li class="active"><a href="?page={}">{}</a></li>'.format(i, i))
            else:
                li_li.append('<li><a href="?page={}">{}</a></li>'.format(i, i))
        if self.page == self.total_page:
            li_li.append(
                '<li class="disabled"><span aria-hidden="true">&raquo;</span></li>')
        else:
            li_li.append(
                '<li><a href="?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.page + 1))
        return ''.join(li_li)
