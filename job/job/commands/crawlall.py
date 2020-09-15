from scrapy.commands import ScrapyCommand
from scrapy.utils.conf import arglist_to_dict


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            pass
        # raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)

    def run(self, args, opts):
        # 获取爬虫列表
        spd_loader_list = self.crawler_process.spider_loader.list()  # 获取所有的爬虫文件。
        print(spd_loader_list)
        # 遍历各爬虫
        for spname in spd_loader_list or args:
            self.crawler_process.crawl(spname, **opts.spargs)
            print('此时启动的爬虫为：' + spname)
        self.crawler_process.start()

        # spider_loader = self.crawler_process.spider_loader
        # for spidername in args or spider_loader.list():
        #   print("*********cralall spidername************")  + spidername
        #   self.crawler_process.crawl(spidername, **opts.spargs)
        # self.crawler_process.start()
