import org.openqa.selenium.By;

public class StandoutLoginPage {

    // ----- start ----- define selectors for Page Elements
    By userId = By.id("email"); // User ID text input field
    By password = By.id("password"); // Password text input field
    By loginButton = By.id("loginButton"); // Large Login button (top frame)
    // ----- end ----- define selectors

    public StandoutLoginPage(SafariDriver driver) {
        this.driver = driver;
    }

    public enterUserName(String strTheUserName) {
        driver.findElement(userId).sendKeys(strTheUserName);
    }

    public enterPassword(String strThePassword) {
        driver.findElement(password).sendKeys(strThePassword);
    }

    public clickLoginButton() {
        driver.findElement(loginButton).click();
    }

}
