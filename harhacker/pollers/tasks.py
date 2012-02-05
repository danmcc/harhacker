import os
import browsermobproxy as mob
from celery.task import task
from selenium import webdriver
from harhacker import settings

browsermob_path = os.environ.get(
    'BROWSERMOB_PROXY_PATH',
    os.path.join(settings.ROOT_PATH, '..', 'browsermob-proxy', 'bin', 'browsermob-proxy'),
)

@task(ignore_result=True)
def poll_har(url):
    s = mob.Server(browsermob_path)
    s.start()
    proxy = s.create_proxy

    profile = webdriver.FirefoxProfile()
    profile.set_proxy(proxy.selenium_proxy())
    driver = webdriver.Firefox(firefox_profile=profile)

    proxy.new_har(url)
    driver.get(url)

    print proxy.har

    driver.quit()
    s.stop()
