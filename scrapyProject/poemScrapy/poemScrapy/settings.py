BOT_NAME = 'poemScrapy'
SPIDER_MODULES = ['poemScrapy.spiders']
NEWSPIDER_MODULE = 'poemScrapy.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 ' \
             'Safari/537.36 '
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# 设置日志打印的等级
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {'poemScrapy.pipelines.PoemscrapyPipeline': 1, }
