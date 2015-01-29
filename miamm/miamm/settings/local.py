from .base import root

DEBUG = True

DATABASES = {
      'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': 'devdb',
      'USER': '',
      'PASSWORD': '',
      'HOST': '',
      'PORT': '',
                                                            }
}

TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = root('..')
TEST_DISCOVER_ROOT = root('..')
TEST_DISCOVER_PATTERN = 'test_*'