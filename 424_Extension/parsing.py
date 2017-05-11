import os
import sqlite3
import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
import requests
import metadata_parser
from bs4 import BeautifulSoup
import datetime
from http.server import BaseHTTPRequestHandler,HTTPServer
import socket
from flask import Flask
import cgi


def parse(url):
	r = requests.get(url)
	root = BeautifulSoup(r.content, "html.parser")
	title = root.find("meta",  property="og:title")
	file_type = root.find("meta",  property="og:type")
	dagr = (46, 'file', 'pat', '2017-05-04 02:22:15.463918', None, None, 0)
	doc = (41, 'Page', 'pat', '2017-05-04 02:22:15.463918', None, 3, url, file_type, 46, url)
	add2db(url, dagr, doc)
	print("Working")
	return

def add2db(url, dagr, doc):
	file = 'db.sqlite3'
	conn = sqlite3.connect(file)
	c = conn.cursor()
	c.execute('INSERT INTO DAGR_dagr VALUES (?,?,?,?,?,?,?)', dagr)
	c.execute('INSERT INTO DAGR_document VALUES (?,?,?,?,?,?,?,?,?,?)', doc)
	conn.commit()
	print(c.fetchone())
	print ("Done")
	return


# while True:
# 	try:
# 		file = open("url.txt", "r")
# 		url = file.readline()
# 		if url != '':
# 			file.close()
# 			parse(url)
# 			os.remove("url.txt")
# 	except IOError:
# 		a = True

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "You're not supposed to be here."
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
def do_POST(self):
	form = cgi.FieldStorage()
	print (form.getvalue("status"))
        # Begin the response
	self.send_response(200)
	return

def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()