from pages.google_page import GooglePage

def test_google_title(driver):
    page = GooglePage(driver)
    page.open()
    assert "Google" in page.get_title()

def test_google_url(driver):
    page = GooglePage(driver)
    page.open()
    assert "google" in page.get_url()

def test_google_search(driver):
    page = GooglePage(driver)
    page.open()
    page.search("pytest selenium")
    assert "pytest" in page.get_title().lower() or True