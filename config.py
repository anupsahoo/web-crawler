mimetypes_list = [ ]

file_extensions_list = [ '.html' ]

request_timeout = 60

request_delay = 0

use_selenium = True

browser_name = "Firefox"

urls_to_crawl = [
    {
        "url": "http://www.cuyoo.com/",
        "follow_links_containing": "cuyoo.com",
        "regex_filters": [ r"/article" ],
        "ignore_query_strings": True,
    },
]
