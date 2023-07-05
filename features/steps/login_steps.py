from behave import *
from expects import *
from tools.credentials import Credentials
from tools.page_factory import PageFactory


@Given('Access to a browser.')
def step_impl(context,):
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


@When('The user access "{env}".')
def step_impl(context, env):
    context.env = env
    credentials = Credentials()
    context.env_settings = credentials.get_credentials(context.env)
    context.driver.get(context.env_settings['URL'])


@step('logs in as "{user_type}".')
def step_impl(context, user_type):
    context.page = PageFactory(context.driver).create_page('Login')
    expect(context.page.login_visible()).to(be_true)
    context.page.login(context.env_settings[user_type], context.env_settings['PWD'])
