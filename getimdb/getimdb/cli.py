import click
import requests

from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='tt2395427', required=False)
def main(name, as_cowboy):
    	"""getimdb"""
    	#greet = 'Howdy' if as_cowboy else 'Hello'
    	#click.echo('{0}, {1}.'.format(greet, name))
	Url='http://api.themoviedb.org/3/movie/{}/images?api_key=0ef20538f6e729adcbac42debfcfbb1c'.format(name)
	r=requests.get(Url)
	api=r.json()
	posters=api['posters']
	for poster in posters:
	url='http://image.tmdb.org/t/p/original{}'.format(poster['file_path'])
	req=requests.get(url)
	img=Image.open(StringIO(req.content))
	img.show()


