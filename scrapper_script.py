#!/usr/bin/python
import urllib2
import _mysql
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str


class SpitUrls(object):
    def __init__(self,counter=0 ):
        self.counter = counter
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.counter > 5:
            raise StopIteration
        else:
            counter = self.counter
            self.counter += 1
            url = 'http://vimeo.com/channels/staffpicks/videos/page:%d/sort:likes/format:thumbnail'%self.counter
            return url


def main():
    #import pdb;
    #pdb.set_trace()
    for url in SpitUrls():
        response = urllib2.urlopen(smart_str(url))
        soup = BeautifulSoup(response.read())
        video_titles =  [each.text.strip() for each in soup.find_all('p', class_="title")]
        for title in video_titles:
            href = soup.find('a', attrs={'title':title})['href']
            video_id = href.split("/")[-1]
            detail_page = "http://www.vimeo.com/%s" %(video_id)
            soup2 = BeautifulSoup(urllib2.urlopen(detail_page).read())
            try:
                if soup2.find('a', attrs={'rel':'author'}).find_next_sibling()['href'] == '/plus':
                    paying_user = 1
                else:
                    paying_user = 0
            except Exception:
                paying_user = 0
            
            username = soup2.find('a', attrs={'rel':'author'}).text
            is_staff_pick = 1
            has_video = 1
            userprofile = "http://www.vimeo.com%s" %(soup2.find('a', attrs={'rel':'author'})['href'])
            db = _mysql.connect(host="localhost",user="django_vimeo",passwd="vimeo", db="vimeo")
            try:
                query = "INSERT INTO items_item (username,userprofile,is_paying_user,has_video,is_staff_pick) \
                    values ('%s','%s',%d,%d,%d);"%(smart_str(username), smart_str(userprofile), paying_user,has_video,is_staff_pick);
                db.query(query)
            except Exception:
                pass

if __name__ == '__main__':
    main()
