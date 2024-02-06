import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    def test_authorization(self, browser, wait, load_config):

        login = load_config['login_stepik']
        password = load_config['password_stepik']