#! /usr/bin/python
import os
from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File
from twisted.web.vhost import NameVirtualHost
from twisted.web.server import Site



def generateHomePage():
	template = open("index.html","r")
	return template.read()

class Root(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        return Resource.getChild(self, name, request)
    
    def render_GET(self, request):
        print "Got a GET Request"
	return generateHomePage()
    
    def render_POST(self, request):
        val = request.__dict__['args']
        return str(results)

class Node(Resource):
    isLeaf = True
    def getChild(self, name, request):
        if name == '':
            return self
        return Resource.getChild(self, name, request)

    def render_GET(self, request):
        return "Hello, world! I am located at %r." % (request.prepath,)


class Images(Resource):
	isLeaf = True
	def getChild(self,name,request):
		if name == '':
			return self
		return Resource.getChild(self,name,request)
	def render_GET(self,request):
		print os.getcwd()
		return open(request.uri[1:],"r")

root = Root()
root.putChild('test',Node())
root.putChild('images',File("./images"))
root.putChild('css',File("./css"))
root.putChild('fonts',File("./fonts"))
root.putChild('video',File("./video.html"))
root.putChild('video_files',File("./video_files"))       #Temporary hack to get this working
root.putChild('MY_VIDEO.mp4',File('MY_VIDEO.mp4'))	 #temporary hack
site = server.Site(root)
reactor.listenTCP(8080, site)
reactor.run()
