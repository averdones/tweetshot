from tweetshot.webdrivers.chrome import get_chrome_driver
from tweetshot.webdrivers.firefox import get_firefox_driver


OPTIONS_LIST = [
    '--headless'
]


def get_driver(type='chrome', executable_path=None):
    """Loads a selenium driver from one of the available ones.

    Supported drivers:
        - chromedriver
        - geckodriver

    Args:
        type (str, optional): Type of driver to use. Either 'chrome' or 'firefox', to use chromedriver or
                              geckodriver respectively.
        executable_path (str, optional): Path to the executable drive. If set to  'chromedriver', it will read it
                                         from the PATH.

    Returns:
        callable: Selenium driver.

    """
    if type == 'chrome':
        driver = get_chrome_driver(options_list=OPTIONS_LIST, executable_path=executable_path)
    elif type == 'firefox':
        driver = get_firefox_driver(options_list=OPTIONS_LIST, executable_path=executable_path)
    else:
        raise ("Type must be either 'chrome' or 'firefox'.")

    driver.set_window_size(1920, 1080)

    return driver
