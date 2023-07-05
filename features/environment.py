from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_webdriver_chrome(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    context.driver = webdriver.Chrome(options=options)
    yield context.driver


def before_scenario(context, scenario):
    tags = ["bug", "outdated"]
    for tag in tags:
        if tag in scenario.effective_tags:
            scenario.skip()
    else:
        use_fixture(selenium_webdriver_chrome, context)
