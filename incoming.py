from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
import urllib

class MailHandler(InboundMailHandler):
  def receive(self, message):
    content_type, encoded = message.bodies(content_type='text/plain').next()
    body = encoded.decode()
    sender = message.sender
    subject = message.subject
    urlfetch.fetch("http://yourotherapp.example.com/private/emails/handle_incoming", urllib.urlencode({'body':body, 'sender':sender, 'subject':subject}), urlfetch.POST) 
    
application = webapp.WSGIApplication([MailHandler.mapping()], debug=True)

def main():
  run_wsgi_app(application)
if __name__ == "__main__":
  main()