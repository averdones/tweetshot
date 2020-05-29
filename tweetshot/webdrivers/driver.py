import os


def get_driver(webdriver, driver_manager, options_list, executable_path, options):
    """Loads a generic driver.

    There are 3 possible ways of loading the driver:
        - Let webdriver_manager to load it automatically.
        - Load it from the PATH.
        - Point to the executable path of the driver.

    Args:
        webdriver (callable): Selenium webdriver.
        driver_manager (callable): Driver manager.
        options_list (list[Str]): Selenium driver options.
        executable_path (str): Path to the executable drive. If set, it will read it from the PATH.
        options (callable): Options for Selenium driver

    Returns:
        callable: Selenium Chrome driver object.

    """
    if options_list is not None:
        for option in options_list:
            options.add_argument(option)

    if executable_path is None:
        print("Using automatic driver manager")
        return webdriver(executable_path=driver_manager(log_level=0).install(), options=options,
                         service_log_path=os.devnull)
    else:
        try:
            print("Using custom driver")
            return webdriver(executable_path=executable_path, options=options, service_log_path=os.devnull)
        except:
            print("ERROR. Falling back to automatic driver manager")
            return webdriver(executable_path=driver_manager(log_level=0).install(), options=options,
                             service_log_path=os.devnull)
