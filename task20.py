#!/usr/bin/python2.7 -u

import argparse
import requests
import time
from bs4 import BeautifulSoup

domain_name = "https://en.wikipedia.org"

# start_url = domain_name + "/wiki/Python_(programming_language)"
phyl_url = domain_name + "/wiki/Philosophy"

fetch_interval = 5#sec

def main():
    parser = argparse.ArgumentParser(description="web crawler")
    parser.add_argument("start_url", help="start page address")
    parser.add_argument("depth", help="max. number of hops")
    args = parser.parse_args()
    start_url = args.start_url
    depth = int(args.depth)

    print "\nConfig: \n-Start page: {}\n-Depth: {}\n".format(start_url, depth)

    url_bag = set()
    page_url = None
    iter_cnt = 1
    while page_url != phyl_url and iter_cnt <= depth:
        if page_url is None:
            page_url = start_url

        if page_url not in url_bag:
            url_bag.add(page_url)
        else:
            print "Cycle detected. Exiting ... "
            break

        print "Iteration: {}".format(iter_cnt)

        print "-Fetching: {}".format(page_url)
        doc = requests.get(page_url).text

        print "-Parsing: {}".format(page_url)
        soup = BeautifulSoup(doc, "html.parser")

        for a in soup.select("#mw-content-text > p > a[href]"):
            if not a.get("href").startswith("/wiki"):
                continue
            if a.get("class") is not None and "new" in a.get("class"):
                continue
            lb, rb = 0, 0
            for t in a.find_previous_siblings(text = True):
                lb += t.count("(")
                rb += t.count(")")
            if lb - rb > 0:
                continue
            print "-Link: {}".format(domain_name + a.get("href")) 
            page_url = domain_name + a.get("href")
            iter_cnt += 1
            break

        print "-Sleeping ({}s) ... ".format(fetch_interval)
        time.sleep(fetch_interval)


if __name__ == "__main__":
    main()
