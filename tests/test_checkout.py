from models.bstackdemo import LoginPage, CartPage, CheckoutPage
from playwright.sync_api import sync_playwright
import pytest, time, datetime

# @pytest.fixture(scope="function", autouse=True)
# def take_screenshot(appium_driver):
#     yield
#     time.sleep(1)
#     appium_driver.get_screenshot_as_file(
#         f'test_reports/{datetime.today().strftime("%Y-%m-%d")}.png')

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
login = LoginPage(page)
cart = CartPage(page)
checkout = CheckoutPage(page)

def test_singleSignIn():
    login.navigate()
    username = "demouser"
    password = "testingisfun99"
    login.clickSignIn()
    login.signIn(username, password)
    login.checkLoggedIn(username)

@pytest.mark.parametrize("locator",
                            [pytest.param("[id=\"\\32 \"]", id=""),
                            pytest.param("[id=\"\\38 \"]", id=""),
                            pytest.param("[id=\"\\31 4\"]", id=""),
                            pytest.param("[id=\"\\32 0\"]", id=""),
                            pytest.param("[id=\"\\32 5\"]", id=""),
                            pytest.param("[id=\"\\31 \"]", id="")]
                        )
def test_addToCart(locator):
    cart.addToCart(locator)

def test_clickCheckOut():
    cart.clickCheckout()

def test_formFillup():
    checkout.fillUpForm()

def test_orderPlacedConfirmation():
    checkout.confirmOrder()

def test_continueShopping():
    checkout.continueShopping()

def test_logOut():
    login.signOut()