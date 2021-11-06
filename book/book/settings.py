BOT_NAME = 'book'

SPIDER_MODULES = ['book.spiders']
NEWSPIDER_MODULE = 'book.spiders'

ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {'book.pipelines.CustomFilePipelines': 1}
# ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
FILES_STORE = 'downloaded_files'
