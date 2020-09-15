import scrapy


class Spiderexample4Spider(scrapy.Spider):
    name = 'spiderexample4'
    # allowed_domains = ['www.qq.com']
    start_urls = ['https://www.cnblogs.com/llssx/p/8378832.html']

    def parse(self, response): # resonse相当于从网络中返回内容所存储的或对应的对象
        # fname = response.url.split('/')[-1] # 定义文件名字，把response中的内容写到一个html文件中
        fname="4444"+"."+response.url.split('.')[-1]
        print(fname)
        with open (fname, 'wb') as f: # 从响应的url中提取文件名字作为保存为本地的文件名，然后将返回的内容保存为文件
            f.write(response.body)
        self.log('Saved file %s.' % fname) # self.log是运行日志，不是必要的
        print("~~~~~成功~~~~~")