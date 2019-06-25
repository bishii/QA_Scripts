import org.openqa.selenium.By;

public class StandoutMainModalPage {

    // ----- start ----- define selectors for Page Elements
    By teamNameInputBox = By.id("teamname"); // Text Input box for the Team Name
    By createButton = By.id("create"); // Button to create the team
    By inviteEmailInputBox = By.name("email"); // Combo Search box for email addresses to include
    By createTeamLink = By.className("add-to-queue-link"); // Link to create team
    By sendInviteButton = By.className("send-invite-btn"); // Button to send invitations
    By deleteTeamLink = By.className("delete-team");
    By confirmDeleteTeamButton = By.id("disband");
    // ----- end ----- define selectors

    public StandoutMainModalPage(SafariDriver driver) {
        this.driver = driver;
    }

    public EnterTeamNameToCreate(String strTeamName) {
        driver.findElement(teamNameInputBox).sendKeys(strTeamName);
    }

    public EnterEmailForInvite(String strEmail) {
        driver.findElement(iinviteEmailInputBox).sendKeys(strEmail);
    }

    public clickCreateLink() {
        driver.findElement(createTeamLink).click();
    }

    public clickSendInviteButton() {
        driver.findElement(sendInviteButton).click();
    }

    public clickDeleteTeamLink() {

        driver.findElement(deleteTeamLink).click();
    }

    public clickSendInviteButton() {
        driver.findElement(sendInviteButton).click();
    }
}

