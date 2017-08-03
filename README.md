# zdxsn's blog项目

[![](https://camo.githubusercontent.com/0b162e277a46df3fc0ed9ff6f3cb0463ed632ad8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d322e37253243332e342d626c75652e737667)](https://github.com/thomaszdxsn/blog) ![](https://camo.githubusercontent.com/6def34e1aa4e2e9e81448c8a57cf3e09d8af28cf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4253442d626c75652e737667)

更新日志

v0.1 - 2017/07/23

本blog项目使用django1.8,bootstrap3实现，暂不支持注册、评论功能

## 第三方django apps

- 使用`taggit`实现标签系统
- 使用`sorl-thumbnail`实现缩略图
- 使用`django-markdown`为admin添加markdown编辑器
- 使用`memcache-status`来监控缓存状态
- 使用`django-debug-toolbar`(可以使用命令`debugsqlshell`)
- 使用`silk`实现性能检测
- 使用`django-grappelli`美化admin界面[文档](http://django-grappelli.readthedocs.io/en/latest/customization.html)
- 使用`admin-honeypot`伪装admin页面
- 使用`django-rest-framework`REST框架

## 项目功能

* 实现sitemap
* 实现RSS feed
* 实现轮播图
* 实现文章搜索
* 实现分页，使用"class-based view"
* 实现文章按年分类，实现档案库
* 实现全站缓存机制
* 实现RESTful API


# 插件/应用

- 使用js库`tagcloud`实现3d标签云 [项目地址](https://github.com/mcc108/tagcloud)
- 使用`memcached`实现缓存机制
