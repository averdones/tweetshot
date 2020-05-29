from pathlib import Path
from PIL import Image
from io import BytesIO
import base64
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tweetshot.webdrivers.set_webdriver import get_driver


class Tweetshot:
    """Class to take a screenshot of a tweet.

    Attributes:
        url (str): tweet URL.
        type_driver (str): Type of driver to use. Either 'chrome' or 'firefox'.
        executable_path (str, optional): Path to the executable drive.
        timeout (int, optional): Number of seconds before timing out when searching for the tweet element.

    """

    def __init__(self, url, type_driver='chrome', executable_path=None, timeout=30):
        """Initializes instance of class Tweetshot."""
        self.url = url
        self.type_driver = type_driver
        self.executable_path = executable_path
        self.timeout = timeout

        self.driver = None

    def get_tweetshot(self):
        """Gets a tweet screenshot.

        Returns:
            PIL image: tweet screenshot.

        """
        self.set_up()
        self.go_to_url()
        tweet_element = self.get_tweet_element()
        tweet_location = self.get_tweet_location(tweet_element)
        self.wait_tweet_image_element()
        full_screenshot = self.take_full_screenshot()
        self.tear_down()

        return self.crop_tweet_screenshot(full_screenshot, tweet_location)

    def get_tweetshot_as_pil(self):
        """Returns the tweet screenshot as a PIL Image.

        Returns:
            PIL image: tweet screenshot.

        """
        return self.get_tweetshot()

    def get_tweetshot_as_bytes(self):
        """Returns the tweet screenshot as a bytes Image.

        Returns:
            bytes: tweet screenshot.

        """
        buffered = BytesIO()
        self.get_tweetshot().save(buffered, format="PNG")

        return buffered.getvalue()

    def get_tweetshot_as_base64(self):
        """Returns the tweet screenshot as a base64 image.

        Returns:
            base64: tweet screenshot.

        """
        return base64.b64encode(self.get_tweetshot_as_bytes())

    def set_up(self):
        """Sets up the Selenium driver connection."""
        self.driver = get_driver(type=self.type_driver, executable_path=self.executable_path)

    def tear_down(self):
        """Tears down the Selenium driver connection."""
        self.driver.quit()

    def go_to_url(self):
        """Sends the selenium driver to a specific url."""
        self.driver.get(self.url)

    def take_full_screenshot(self):
        """Takes a screenshot of the full visible screen.

        Returns:
            PIL image: full screen screenshot.

        """
        png = self.driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))

        return im

    def get_tweet_element(self):
        """Gets the HTML element of the tweet.

        Returns:
            Tweet element.

        """
        xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div/div/section/div/div/div/div[1]/div/' \
                'div/div/div/article'

        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def get_tweet_image_element(self):
        """Gets the HTML element of the image in the tweet, if present.

        Returns:
            Tweet element.

        """
        # TODO: deal better with waiting for the tweet to fully load
        xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div/div/section/div/div/div/div[1]/div/' \
                'div/div/div/article/div/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/a[2]/div/div/div'

        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def wait_tweet_image_element(self):
        """Waits for the image in the tweet to load, if there is one.

        Returns:

        """
        # noinspection PyBroadException
        try:
            self.get_tweet_image_element()
        except Exception:
            pass

    @staticmethod
    def get_tweet_location(tweet_element):
        """Gets a 4-tuple defining the left, upper, right, and lower pixel coordinate of the tweet element.

        Args:
            tweet_element (WebElement instance): HTML tweet element.

        Returns:
            tuple: 4-tuple with coordinates.

        """
        location = tweet_element.location
        size = tweet_element.size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        return left, top, right, bottom

    @staticmethod
    def crop_tweet_screenshot(full_screenshot, tweet_location):
        """Crops the full screen screenshot to get only the tweet.

        Args:
            full_screenshot (PIL Image): full screen screenshot.
            tweet_location (tuple);  4-tuple with coordinates.

        Returns:
            PIL image: tweet screenshot.

        """
        return full_screenshot.crop(tweet_location)

    def save_tweet_screenshot(self, output_filename=None):
        """Saves the tweet screenshot to disk.

        Args:
            output_filename (Path or str, optional): Absolute or relative path where to save the screenshot.

        Returns:
            Path: Path to the saved file.

        """
        if output_filename is None:
            output_filename = 'screenshot'

        tweetshot = self.get_tweetshot_as_pil()
        output_filename = Path(output_filename).with_suffix('.png')
        tweetshot.save(output_filename)

        return output_filename


def take_screenshot(url, type_driver='chrome', executable_path=None, timeout=10, output_filename='screenshot'):
    """Takes a screenshot of a tweet and saves it to disk.

    Args:
        url (str): tweet URL.
        type_driver (str): Type of driver to use. Either 'chrome' or 'firefox'.
        executable_path (str, optional): Path to the executable drive.
        timeout (int, optional): Number of seconds before timing out when searching for the tweet element.
        output_filename (Path or str, optional): Absolute or relative path where to save the screenshot.

    Returns:
        Path: Path to the saved file.

    """
    return Tweetshot(url, type_driver, executable_path, timeout).save_tweet_screenshot(output_filename)


def take_screenshot_as_pil(url, type_driver='chrome', executable_path=None, timeout=10):
    """Returns a PIL Image with a tweet screenshot.

    Args:
        url (str): tweet URL.
        type_driver (str): Type of driver to use. Either 'chrome' or 'firefox'.
        executable_path (str, optional): Path to the executable drive.
        timeout (int, optional): Number of seconds before timing out when searching for the tweet element.

    Returns:
        PIL Image: Image in PIL Image format.

    """
    return Tweetshot(url, type_driver, executable_path, timeout).get_tweetshot_as_pil()


def take_screenshot_as_bytes(url, type_driver='chrome', executable_path=None, timeout=10):
    """Returns a bytes image with a tweet screenshot.

    Args:
        url (str): tweet URL.
        type_driver (str): Type of driver to use. Either 'chrome' or 'firefox'.
        executable_path (str, optional): Path to the executable drive.
        timeout (int, optional): Number of seconds before timing out when searching for the tweet element.

    Returns:
        bytes: Image in bytes format.

    """
    return Tweetshot(url, type_driver, executable_path, timeout).get_tweetshot_as_bytes()


def take_screenshot_as_base64(url, type_driver='chrome', executable_path=None, timeout=10):
    """Returns a base64 image with a tweet screenshot.

    Args:
        url (str): tweet URL.
        type_driver (str): Type of driver to use. Either 'chrome' or 'firefox'.
        executable_path (str, optional): Path to the executable drive.
        timeout (int, optional): Number of seconds before timing out when searching for the tweet element.

    Returns:
        base64: Image in base64 format.

    """
    return Tweetshot(url, type_driver, executable_path, timeout).get_tweetshot_as_base64()
