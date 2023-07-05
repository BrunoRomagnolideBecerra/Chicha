from tools.helpers import Helpers
from inspect import isclass
from pkgutil import iter_modules
from importlib import import_module

# iterate through the modules in the pages package
package_dir = 'pages'
for (_, module_name, _) in iter_modules([package_dir]):

    # import the module and iterate through its attributes
    module = import_module(f"pages.{module_name}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if isclass(attribute):
            # Add the class to this package's variables
            globals()[attribute_name] = attribute


class PageFactory:

    def __init__(self, driver):
        self.driver = driver

    def create_page(self, page_name):
        clazz_name = Helpers().convert_string_to_camel_case(page_name)
        return globals()[clazz_name](self.driver)
