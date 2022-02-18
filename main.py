
import urllib
import urllib.request
import webbrowser
import sys

class FetchLocalCopy:
    def __init(self):
        pass

    def GetPage(self, url, filename):
        html_text = ''
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
            encoding = response.headers.get_content_charset('utf-8')
            html_text = html_content.decode(encoding)

            f = open("file.html", "w", encoding="utf-8")
            f.write(html_text)
            f.close()

    def OpenPage(self, page):
        webbrowser.open_new_tab("file.html")

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Please Pass a URL")
        exit(0);

    URL = sys.argv[1]
    copy = FetchLocalCopy()
    copy.GetPage(URL, "file.html")
    copy.OpenPage(URL)