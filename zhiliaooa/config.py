SECRET_KEY = "fbkahdfudbafjsjafajf"

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhiliaooa'
USERNAME = 'root'
PASSWORD = '050911'
DB_URI ='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


#邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2904940278@qq.com"
MAIL_PASSWORD = "azudrgijsktddded"
MAIL_DEFAULT_SENDER = "2904940278@qq.com"

