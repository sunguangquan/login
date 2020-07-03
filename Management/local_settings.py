# 设置本地数据库配置，需要执行"pip install mysqlclient"安装依赖。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'san611027',
        'NAME': 'happy_size'
    }
}
# 设置语言为中文
LANGUAGE_CODE = 'zh-hans'
# 设置时区为上海时区
TIME_ZONE = 'Asia/Shanghai'
# 设置不使用国际时区。
USE_TZ = False
