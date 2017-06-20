# kuaidailiProxy
环境需要
python2.7
scrapy1.2.0
MySQLdb1.2.5
该程序用来爬取快代理的免费国外匿名代理ip，默认爬取一页，可以在spider里设置。结果会保存到mysql数据库中的kuaidaili
要在setting中把数据库的相关信息改成自己的。
反爬虫
设置了随机useragent，关闭了cookie，设置了爬取速度限制。
