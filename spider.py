from urllib.request import Request, urlopen
from link_finder import LinkFinder
import threading
from general import *
from domain import *


class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    headers = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name, user_agent):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = project_name + '/queue.txt'
        Spider.crawled_file = project_name + '/crawled.txt'
        Spider.headers = {'User-Agent': user_agent}
        self.boot()
        self.crawl_page(threading.current_thread().name, Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' is crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_str = ''
        try:
            request = Request(page_url, headers=Spider.headers)
            response = urlopen(request)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_str = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_str)
        except:
            print('Cannot access ' + page_url)
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for link in links:
            if link not in Spider.queue and link not in Spider.crawled:
                if Spider.domain_name == get_domain_name(link):
                    Spider.queue.add(link)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue_file, Spider.queue)
        set_to_file(Spider.crawled_file, Spider.crawled)