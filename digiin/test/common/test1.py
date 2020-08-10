from digiin.test.common.start_app import Android_driver

from digiin.test.pages.choice_schoolpage import Choice_SchoolPage
from digiin.test.pages.loginPage import LoginPage


Choice_SchoolPage().choice_school()

LoginPage().login(2020052804)