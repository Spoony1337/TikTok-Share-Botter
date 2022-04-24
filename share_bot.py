try:
    import requests, string, random, os, platform, ctypes, threading
    from colorama import Fore, init
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")

init(convert=True)

ascii_text = """
        _   _ _    _        _    
       | | (_) |  | |      | |   
       | |_ _| | _| |_ ___ | | __
       | __| | |/ / __/ _ \| |/ /
       | |_| |   <| || (_) |   < 
        \__|_|_|\_\\__\___/|_|\ _\\
  """

if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"

class tiktok:

    def __init__(self):
        self.lock = threading.Lock()
        self.shared = 0
        self.errors = 0
    
    def safe_print(self, arg):
        self.lock.acquire()
        print(arg)
        self.lock.release()

    def update_title(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"TikTok Share Botter | Sent Shares: {self.shared} | Errors: {self.errors} | https://github.com/Spoony1337")

    def send_share(self, video_id):
        try:
            data = "item_id={}&share_delta=1".format(video_id)
            headers = {
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "user-agent": "com.zhiliaoapp.musically/2022309050 (Linux; U; Android 7.1.2; en; G011A; Build/N2G48H;tt-ok/3.10.0.2)"
            }
            device_id = ("").join(random.choices(string.digits, k = 19))
            session = requests.Session()
            url = f"https://api31-core-useast1a.tiktokv.com/aweme/v1/aweme/stats/?channel=googleplay&device_type=G011A&device_id={device_id}&os_version=7.1.2&version_code=220400&app_name=musically_go&device_platform=android&aid=1988"
            r = session.post(url,headers=headers,data=data)
            if r.json()["status_code"] == 0:
                #self.safe_print(f"       {Fore.WHITE}[{Fore.GREEN}Success{Fore.WHITE}] Sent share!")
                self.shared += 1
            else:
                self.errors += 1
        except:
            self.errors += 1
        if clear == "cls":
            self.update_title()
        
    def parse_url(self, url):
        if "vm.tiktok.com" in url:
            r = requests.get(url, allow_redirects=False)
            url = r.headers["Location"]
        try:
            url = url.split("/video/")[1]
            url = url.split("?")[0]
        except IndexError:
            pass
        return url
        
    def main(self):
        os.system(clear)
        if clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW(f"TikTok Share Botter | https://github.com/Spoony1337")
        print(Fore.LIGHTMAGENTA_EX + ascii_text)
        tiktok_url = str(input(f"       {Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}Console{Fore.WHITE}] TikTok URL: "))
        threads = int(input(f"       {Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}Console{Fore.WHITE}] Threads: "))
        video_id = self.parse_url(tiktok_url)
        print(f"\n       {Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}Console{Fore.WHITE}] Sending shares...")
        print()
        def thread_starter():
            self.send_share(video_id)
        while True:
            if threading.active_count() <= threads:
                try:
                    threading.Thread(target = thread_starter).start()
                except:
                    pass

obj = tiktok()
obj.main()
