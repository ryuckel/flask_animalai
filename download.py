from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

key = "e430ac34937da2d56b453c5bd5f6e195"
secret = "915c2826b6bf9944"
wait_time = 1

animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
  text = animalname,
  per_page = 400,
  media = 'photos',
  sort = 'relevance',
  safe_search = 1,
  extras = 'url_q, licence'
)

photos = result['photos']
# pprint(photos)


for i, photo in enumerate(photos['photo']):
  url_q = photo['url_q']
  filepath = savedir + '/' + photo['id'] + '.jpg'
  if os.path.exists(filepath): continue
  urlretrieve(url_q, filepath)
  time.sleep(wait_time)