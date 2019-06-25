import org.openqa.selenium.By;

public class StandoutOptionsModalPage {

    // ----- start ----- define selectors for Page Elements
    By userId = By.id("email"); // User ID text input field
    By password = By.id("password"); // Password text input field
    By loginButton = By.id("loginButton"); // Large Login button (top frame)
    By myTeamsMenuPullDown = By.className("text_inner"); // Big pulldown for My Teams
    By myTeamsList = By.cssSelector("div .teamname-text"); // Filter for my teams
    By teamOptionsSubNav = By.id("team-options-subnav")); // Team Options menu
    By editTeamSubMenu = By.cssSelector("li[data-gaaction=\"rename team\"]"); //Edit Team submenu
    // ----- end ----- define selectors


    public StandoutOptionsModalPage(SafariDriver driver) {
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

    public clickMyTeamsPullDown() {
        driver.findElement(myTeamsMenuPullDown).click();
    }

    public clickOptionsMenu() {
        driver.findElement(teamOptionsSubNav).click();
    }

    public clickEditTeamSubMenuItem() {
        driver.findElement(editTeamSubMenu).click();
    }
}

