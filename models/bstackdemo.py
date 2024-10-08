from playwright.sync_api import Playwright, expect, sync_playwright
import time, re
counter = 0

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://bstackdemo.com/", wait_until="load")
        
    def clickSignIn(self):
        expect(self.page).to_have_url("https://bstackdemo.com/")
        assert self.page.get_by_role("link", name="Sign In").is_visible()
        self.page.get_by_role("link", name="Sign In").click()
    
    
    def signIn(self, username, password):
        expect(self.page).to_have_url("https://bstackdemo.com/signin")
        assert self.page.get_by_text("Select Username").is_visible()
        assert self.page.get_by_text("Select Password").is_visible()
        assert self.page.get_by_role("button", name="Log In").is_visible()
        
        self.page.get_by_text("Select Username").click()
        self.page.get_by_text(username, exact=True).click()

        self.page.get_by_text("Select Password").click()
        self.page.get_by_text(password, exact=True).click()
        
        self.page.get_by_role("button", name="Log In").click()

    def checkLoggedIn(self, username):
        expect(self.page).to_have_url("https://bstackdemo.com/?signin=true")
        print("Successfully signed in")
        assert self.page.get_by_text(username).is_visible()

    def signOut(self):
        self.page.get_by_role("link", name="Logout").click()
        print("Successfully signed out")

    def checkLocked(self):
        assert self.page.get_by_role("heading", name="Your account has been locked.").is_visible

class CartPage:
    def __init__(self, page):
        self.page = page

    def addToCart(self, locator):
        global counter
        assert self.page.get_by_role("link", name="Logout").is_visible()
        self.page.locator(locator).get_by_text("Add to cart").click()
        self.page.get_by_text("X", exact=True).click()
        counter+=1
        print("Item added to cart")

    def clickCheckout(self):
        global counter
        expect(self.page).to_have_url("https://bstackdemo.com/?signin=true")
        assert self.page.get_by_role("link", name="Logout").is_visible()

        self.page.locator("span").filter(has_text=re.compile(r"^{}$".format(counter))).first.click()
        self.page.get_by_text("Checkout").click()

class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fillUpForm(self):
        expect(self.page).to_have_url("https://bstackdemo.com/checkout")
        print("Checkout page reached")

        assert self.page.locator("[data-test=\"shipping-address-heading\"]").is_visible()
        self.page.get_by_label("First Name").click()
        self.page.get_by_label("First Name").fill("John")

        self.page.get_by_label("Last Name").click()
        self.page.get_by_label("Last Name").fill("Doe")

        self.page.get_by_label("Address").click()
        self.page.get_by_label("Address").fill("Uday Tower, Gulshan-1")

        self.page.get_by_label("State/Province").click()
        self.page.get_by_label("State/Province").fill("Dhaka")

        self.page.get_by_label("Postal Code").click()
        self.page.get_by_label("Postal Code").fill("1218")

        self.page.get_by_role("button", name="Submit").click()
        print("form filled up")
        
        
    def confirmOrder(self):
        expect(self.page).to_have_url("https://bstackdemo.com/confirmation")

        self.page.get_by_text("Download order receipt").click()
        print("Order receipt downloaded")

    def continueShopping(self):
        expect(self.page).to_have_url("https://bstackdemo.com/confirmation")

        assert self.page.get_by_role("button", name="Continue Shopping »").is_visible()
        self.page.get_by_role("button", name="Continue Shopping »").click()

        assert self.page.get_by_role("link", name="Logout").is_visible()
