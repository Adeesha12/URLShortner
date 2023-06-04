import pyshorteners
short_obj = pyshorteners.Shortener()


def url_short(url):
    available_providers = [short_obj.clckru,short_obj.dagd,short_obj.isgd,short_obj.osdb,short_obj.tinyurl]
    for i in available_providers:
        print(i.short(url))
    # short_url = short_obj.tinyurl.short(url)
    # print(short_url)
    


if __name__== "__main__":
    url = 'https://www.google.com/maps/place/Thekka+kanda+(%E0%B6%AD%E0%B7%9A%E0%B6%9A%E0%B7%8A%E0%B6%9A+%E0%B6%9A%E0%B6%B1%E0%B7%8A%E0%B6%AF)/@7.333136,80.2391532,13z/data=!4m6!3m5!1s0x3ae3231bc119f34f:0x4b81266292a8ddd2!8m2!3d7.361899!4d80.209676!16s%2Fg%2F11t7l0flpz?entry=ttu'
    url_short(url)