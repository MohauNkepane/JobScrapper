import urllib3
import os
import re
from bs4 import BeautifulSoup
from datetime import date
from dotenv import load_dotenv
load_dotenv()


def get_today_jobs():
    """
    Get Jobs Posted today.
    Returns a list of jobs
    :return:
    """
    http = urllib3.PoolManager()
    r = http.request('GET', os.getenv("URL"))
    if r.status == 200:

        html_doc = str(r.data)

        soup = BeautifulSoup(html_doc, "lxml")
        t = date.today()  # Get today's Date

        jobs = []

        for tag in soup.find_all(class_=re.compile("td_module_1 td_module_wrap td-animation-stack td_module_no_thumb")):
            job = BeautifulSoup(str(tag), "lxml").find(class_=re.compile("entry-title td-module-title"))
            # print(BeautifulSoup(str(job), "lxml"))
            link = BeautifulSoup(str(job), "lxml").find("a")["href"]
            title = BeautifulSoup(str(job), "lxml").find("a")["title"]
            post_date = BeautifulSoup(str(tag), "lxml").find(
                class_=re.compile("entry-date updated td-module-date")).text

            if post_date == t.strftime("%B %d, %Y"):
                job_dict = {"Title": title, "Link": link}
                jobs.append(job_dict)

        return jobs


def get_jobs():
    """
    Get a list Jobs posted over the last few days.
    Returns a list of jobs
    :return:
    """
    http = urllib3.PoolManager()
    r = http.request('GET', os.getenv("URL"))
    if r.status == 200:

        html_doc = str(r.data)

        soup = BeautifulSoup(html_doc, "lxml")

        jobs = []

        for tag in soup.find_all(class_=re.compile("td_module_1 td_module_wrap td-animation-stack td_module_no_thumb")):
            job = BeautifulSoup(str(tag), "lxml").find(class_=re.compile("entry-title td-module-title"))
            # print(BeautifulSoup(str(job), "lxml"))
            link = BeautifulSoup(str(job), "lxml").find("a")["href"]
            title = BeautifulSoup(str(job), "lxml").find("a")["title"]
            post_date = BeautifulSoup(str(tag), "lxml").find(
                class_=re.compile("entry-date updated td-module-date")).text

            job_dict = {"Title": title, "Link": link, "Date": post_date}
            jobs.append(job_dict)

        return jobs


if __name__ == '__main__':
    print(get_jobs())
