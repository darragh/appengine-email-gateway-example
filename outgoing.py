from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail

class OutgoingEmailHandler(webapp.RequestHandler):
  def post(self):
	message = mail.EmailMessage(sender="someone@example.com")
	message.subject = self.request.get('subject')
	message.to = self.request.get('to')
	message.body = self.request.get('body')
	message.send()    
  
application = webapp.WSGIApplication([('/emails', OutgoingEmailHandler)], debug=True)

def main():
  run_wsgi_app(application)
if __name__ == "__main__":
  main()