from flask_mail import Message

class Mailer():
    def __init__(self,server,port,username,password):
        self.server = server
        self.username = username
        self.port = port
        self.password = password
  
        DEBUG=True,
        MAIL_SERVER='%s' % self.server,
        MAIL_PORT= '%d' % self.port,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='%s' % self.username,
        MAIL_PASSWORD= '%s' % self.password
        
