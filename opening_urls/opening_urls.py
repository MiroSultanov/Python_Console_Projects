import webbrowser as wb

def web_automation():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS = ('facebook.com', 'instagram.com')
    for url in URLS:
        print(f'Opening:  ' + url)
        wb.get(chrome_path).open(url)
web_automation()