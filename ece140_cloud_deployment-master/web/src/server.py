from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import FileResponse
import mysql.connector as mysql
import os

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/home.html', {'users': records}, request=req)

def get_page1(req):
  return FileResponse('templates/page1.html')

def get_page2(req):
  return FileResponse('templates/page2.html')

def get_page3(req):
  return FileResponse('templates/page3.html')

def get_page4(req):
  return FileResponse('templates/page4.html')

def get_page5(req):
  return FileResponse('templates/page5.html')
''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('get_page1', '/page1')
  config.add_view(get_page1, route_name='get_page1')

  config.add_route('get_page2', '/page2')
  config.add_view(get_page2, route_name='get_page2')

  config.add_route('get_page3', '/page3')
  config.add_view(get_page3, route_name='get_page3')

  config.add_route('get_page4', '/page4')
  config.add_view(get_page4, route_name='get_page4')

  config.add_route('get_page5', '/page5')
  config.add_view(get_page5, route_name='get_page5')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app) 
  server.serve_forever()