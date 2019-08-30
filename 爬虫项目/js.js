define("common/components/list-base/main", ["require", "exports", "module", "common/components/base/Abstract", "common/components/util/sets", "dep/artTemplate/dist/template"], function (require, exports, module) {
    var a = require("common/components/base/Abstract"),
        c = require("common/components/util/sets"),
        h = require("dep/artTemplate/dist/template"),
        y = {
            more: '<li class="activeable list-more">\n    加载更多\n</li>',
            empty: '<li class="list-empty">\n    <span class="icon"></span>\n    <span class="text">当前没有符合条件的职位</span>\n</li>'
        },
        v = function (c) {
            a.call(this, c)
        };
    c.inherit(v, a, {
        TAG: "ListBaseConstructor",
        init: function (a) {
            var c = this;
            return c.showCount = c.showCount || 5, c.supertoucher("init", null, c), c.key || (c.key = function (a) {
                return a
            }), a ? (c.sets(), c.data && c.data.length && c.render(), c.bindEvents()) : c.sets().render().bindEvents(), c
        },
        sets: function () {
            var a = this;
            a.listOffset = 0, a.pen = h.compile(0 == a.layout.indexOf("#") ? $.trim($(a.layout).html()) : a.layout);
            try {
                a.totalpage = Math.ceil(a.total / a.pagesize)
            } catch (e) {
            }
            return a.handleMoreEmpty(), a
        },
        handleMoreEmpty: function () {
            var a = this;
            return y.more = function () {
                return void 0 == a.layoutmore ? y.more : a.layoutmore && 0 == a.layoutmore.indexOf("#") ? $.trim($(a.layoutmore).html()) : a.layoutmore
            }(), a.more = $(y.more), y.empty = function () {
                return void 0 == a.layoutempty ? y.empty : a.layoutempty && 0 == a.layoutempty.indexOf("#") ? $.trim($(a.layoutempty).html()) : a.layoutempty
            }(), a
        },
        render: function () {
            var a = this;
            return a.data && a.data.length ? a.refresh() : a.handleEmpty(), a
        },
        append: function () {
            var a = this;
            a.more.remove(), a.moreappened = !1;
            try {
                a.totalpage = Math.ceil(a.total / a.pagesize)
            } catch (e) {
            }
            return a.container.append(a.pen({
                data: a.adata,
                indexOffset: a.listOffset,
                extra: a.extra
            })), a.data = a.data.concat(a.adata), a.handleMore().handleEmpty(), a.show(), a.listOffset += a.adata.length, a
        },
        refresh: function () {
            var a = this;
            a.listOffset = 0, a.more.remove(), a.moreappened = !1;
            try {
                a.totalpage = Math.ceil(a.total / a.pagesize)
            } catch (e) {
            }
            return a.container.hide(), a.container.html(a.pen({
                data: a.data,
                indexOffset: a.listOffset,
                extra: a.extra
            })), a.showMoreTip && 1 == a.showMoreTip && a.container.find(".item_ul_li:nth-child(n+" + (a.showCount + 1) + ")").addClass("none"), a.container.show(), a.handleMore().handleEmpty(), a.show(), a.listOffset = a.data.length, a
        },
        handleEmpty: function () {
            var a = this;
            if (!a.noempty) return a.data.length || (a.container.html(y.empty), a.emitter.emit("listbase:empty")), a
        },
        handleMore: function () {
            var a = this;
            return !a.nomore && a.totalpage && a.curpage ? (a.layoutmore || a.more.text("加载更多"), a.pending = !1, a.data.length ? 0 == a.showMoreTip ? (a.moreappened && a.more.hide(), a) : a.totalpage != a.curpage || 1 == a.totalpage && a.data.length > a.showCount ? (a.moreappened && a.more.show(), a.moreappened || (a.container.append(a.more), a.moreappened = !0), a) : (a.moreappened && a.more.hide(), a) : (a.moreappened && a.more.hide(), a.handleEmpty(), a)) : a
        },
        bindEvents: function () {
            var a = this;
            return a.container.on("click", ".item", function (e) {
                var c = $(this);
                a.emitter.emit("listbase:itemclick", a.data[c.data("index")], c, e)
            }), a.container.on("click", ".list-more", function () {
                $(this);
                a.pending || (a.pending = !0, a.more.text("加载中..."), a.emitter.emit("listbase:moreclick"))
            }), a.container.on("click", ".more_button", function () {
                var c = $(this);
                a.pending || (a.pending = !0, c.text("加载中..."), a.emitter.emit("listbase:moreclick"))
            }), a
        },
        select: function (a) {
            var c = this;
            c.lis || (c.lis = c.container.find(".item")), c.lis.removeClass("selected");
            var h;
            return $.each(c.data, function (y, v) {
                return c.key(v) == a ? (h = y, !1) : void 0
            }), $(c.lis[h]).addClass("selected"), c
        }
    }), module.exports = v
});