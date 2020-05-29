from PIL import Image

from tweetshot import take_screenshot, take_screenshot_as_pil, take_screenshot_as_bytes, take_screenshot_as_base64


def test_take_screenshot_chrome(tmp_path):
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = tmp_path / "shot"
    im = take_screenshot(url, type_driver='chrome', output_filename=im)

    assert isinstance(Image.open(im), Image.Image)


def test_take_screenshot_firefox(tmp_path):
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = tmp_path / "shot"
    im = take_screenshot(url, type_driver='firefox', output_filename=im)

    assert isinstance(Image.open(im), Image.Image)


def test_take_screenshot_as_pil_chrome():
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = take_screenshot_as_pil(url, type_driver='chrome')

    assert isinstance(im, Image.Image)


def test_take_screenshot_as_pil_firefox():
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = take_screenshot_as_pil(url, type_driver='firefox')

    assert isinstance(im, Image.Image)


def test_take_screenshot_as_bytes_chrome():
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = take_screenshot_as_bytes(url, type_driver='chrome')

    assert isinstance(im, bytes)

def test_take_screenshot_as_bytes_firefox():
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = take_screenshot_as_bytes(url, type_driver='firefox')

    assert isinstance(im, bytes)


def test_take_screenshot_as_base64_chrome():
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = take_screenshot_as_base64(url, type_driver='chrome')

    assert isinstance(im, bytes)


def test_take_screenshot_as_base64_firefox():
    url = 'https://twitter.com/hideo_kojima_en/status/1002107372091817984'
    im = take_screenshot_as_base64(url, type_driver='firefox')

    assert isinstance(im, bytes)
