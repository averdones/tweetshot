from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from tweetshot.webdrivers.driver import get_driver


def get_firefox_driver(options_list=None, executable_path=None):
    """Loads the geckodriver.

    There are 3 possible ways of loading the driver:
        - Let webdriver_manager to load it automatically.
        - Load it from the PATH.
        - Point to the executable path of the driver.

    Args:
        options_list (list[Str], optional): Selenium driver options.
        executable_path (str, optional): Path to the executable drive. If set to  'geckodriver', it will read it
                                         from the PATH.

    Returns:
        callable: Selenium Chrome driver object.

    """
    try:
        from webdriver_manager.firefox import GeckoDriverManager as driver_manager
    except Exception as e:
        print(e)
        driver_manager = None

    return get_driver(webdriver.Firefox, driver_manager, options_list, executable_path, Options())
