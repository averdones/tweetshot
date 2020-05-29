import argparse

from tweetshot.take_screenshot import take_screenshot


def parse_arguments():
    parser = argparse.ArgumentParser(description="Takes a screenshot of a tweet")
    parser.add_argument('url', type=str, help="Url of the tweet to screenshot")
    parser.add_argument('-d', '--driver_type', type=str, default='chrome', help="Type of driver to use. Either 'chrome'"
                                                                                "or 'firefox'")
    parser.add_argument('-c', '--custom_driver', type=str, default=None, help="Path to a custom driver to use. This "
                                                                              "must match the --driver_type argument,"
                                                                              "which by default is 'chrome'")
    parser.add_argument("-t", "--timeout", type=str, default=10, help="Number of seconds before timing out while"
                                                                      " taking the screenshot")
    parser.add_argument("--driver-from-path", dest="driver_from_path", action="store_true", help="If present, this "
                        "option will use load the Selenium driver from the PATH, if present. The type of driver used"
                        "is selected with the option --driver_type")
    parser.add_argument("-f", "--filename", type=str, help="Output file of the screenshot taken. If thi is just a name"
                        "the file will be saved in the same directory where the program is located. Otherwise, an"
                        "absolute path can be introduced to save the file in a different directory")

    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.driver_from_path:
        if args.driver_type == 'chrome':
            args.custom_driver = 'chromedriver'
        elif args.driver_type == 'firefox':
            args.custom_driver = 'geckodriver'

    take_screenshot(args.url, args.driver_type, args.custom_driver, args.timeout, args.filename)
