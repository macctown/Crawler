import threading
from spider import Spider
from queue import Queue
from general import *
from domain import *

PROJECT_NAME = 'thenewbost'
HOME_PAGE = 'http://app.xiaomi.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
NUM_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME, USER_AGENT)


def create_worker():
    for _ in range(NUM_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + ' links are in the queue')
        create_jobs()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


create_worker()
crawl()
