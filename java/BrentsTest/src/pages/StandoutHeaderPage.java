import org.openqa.selenium.By;

public class StandoutiHeaderPage {

    // ----- start ----- define selectors for Page Elements
    By dismissCookieMessageClose = By.className("dismiss-cookie"); // Close X for Cookie Disclaimer
    By menuLogout = By.id("logout"); // Logout sub-menu item
    By menuPreferences = By.id("preferences"); // Root Menu Icon for preferences
    // ----- end ----- define selectors

    public StandoutHeaderPage(SafariDriver driver) {
        this.driver = driver;
    }

    public dismissCookieDisclaimer() {
        driver.findElement(dismissCookieMessageClose).click();
    }

    public clickSubMenuLogout() {
        driver.findElement(menuLogout).click();
    }

    public clickLoginButton() {
        driver.findElement(menuPreferences).click();
    }

}

