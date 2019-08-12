import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuesmon_contrib_mailchimp_subscription_tests.settings")
sys.path.insert(0, "../../tuesmon-back/")

from tests.fixtures import *

import pytest
import django

def pytest_configure(config):
    django.setup()
