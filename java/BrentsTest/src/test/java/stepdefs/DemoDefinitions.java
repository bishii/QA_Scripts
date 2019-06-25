package stepdefs;

import cucumber.api.PendingException;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.safari.SafariDriver;

import java.util.Iterator;
import java.util.List;
import java.util.concurrent.TimeUnit;


public class DemoDefinitions {

    @Given("I have a configured Cucumber-JVM project")
    public void i_have_a_configured_Cucumber_JVM_project() {
        //FirefoxDriver driver=new FirefoxDriver();
        SafariDriver driver=new SafariDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("https://stagingstandout.tmbc.com");

        /*
        try
        {
            Thread.sleep(3000);
        }
        catch(InterruptedException ex)
        {
            Thread.currentThread().interrupt();
        }
        */

        WebElement a = driver.findElement(By.className("dismiss-cookie"));
        a.click();

        driver.findElement(By.id("email")).sendKeys("ishii.persona6@test.com");

        //could use by class here...
        driver.findElement(By.id("password")).sendKeys("$Coconut!");

        //could use other identifiers here...
        driver.findElement(By.id("loginButton")).click();

        try
        {
            Thread.sleep(5000);
        }
        catch(InterruptedException ex)
        {
            Thread.currentThread().interrupt();
        }
        WebElement x = driver.findElement(By.id("preferences"));
        System.out.println("**** WEBELEMENT IS:" + x.getTagName());
        try
        {
            Thread.sleep(3000);
        }
        catch(InterruptedException ex)
        {
            Thread.currentThread().interrupt();
        }
        x.click();

        try
        {
            Thread.sleep(5000);
        }
        catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        WebElement y = driver.findElement(By.id("logout"));
        System.out.println("**** WEBELEMENT2 IS:" + y.getTagName());
        y.click();

        /*

        driver.findElement(By.id("team-options-subnav")).click();
        try
        {
            Thread.sleep(3000);
        }
        catch(InterruptedException ex)
        {
            Thread.currentThread().interrupt();
        }

        driver.findElement(By.cssSelector("li[data-gaaction=\"create\"]")).click();
        try
        {
            Thread.sleep(3000);
        }
        catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        // be sure to check if visible; Also, this is reused to make into a page object.
        driver.findElement(By.id("teamname")).sendKeys("Test Team 3");

        driver.findElement(By.id("create")).click();
        try
        {
            Thread.sleep(3000);
        }
        catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        driver.findElement(By.name("email")).sendKeys("lee1.persona4@test.com");
        try
        {
            Thread.sleep(3000);
        }
        catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        driver.findElement(By.className("add-to-queue-link")).click();
        driver.findElement(By.className("send-invite-btn")).click();

        try
        {
            Thread.sleep(8000);
        }
        catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        driver.get("https://stagingstandout.tmbc.com");

        driver.findElement(By.id("preferences")).click();
        try
        {
            Thread.sleep(3000);
        }
        catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        driver.findElement(By.id("logout")).click();
        */

        throw new cucumber.api.PendingException();
    }

    @When("I run it within my IDE")
    public void i_run_it_within_my_IDE() {
        //FirefoxDriver driver=new FirefoxDriver();
        SafariDriver driver=new SafariDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("https://stagingstandout.tmbc.com");
        driver.findElement(By.id("email")).sendKeys("ishii.persona6@test.com");

        //could use by class here...
        driver.findElement(By.id("password")).sendKeys("$Coconut!");

        //could use other identifiers here...
        driver.findElement(By.id("loginButton")).click();


        try {
            Thread.sleep(5000);
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }


        WebElement z = driver.findElement(By.className("text_inner"));
        WebElement a = driver.findElement(By.className("dismiss-cookie"));
        System.out.println("*** big pulldown is:" + z.getText());
        a.click();


        try {
            Thread.sleep(1000);
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }

        z.click();

        /*
        try {
            Thread.sleep(1000);
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        */
        //WebElement b=driver.findElement(By.xpath("/div[contains(text(),'Test Team 3')]"));
        Iterator<WebElement> b=driver.findElements(By.cssSelector("div .teamname-text")).iterator();

        boolean found = false;
        while(!found) {
            WebElement c = b.next();
            System.out.println("->" + c.getText() + "<-");
            if (c.getText().equals("Test Team 3")) {
               c.click();
               found = true;
            }
        }
        System.out.println("***Submenu is: " + b);


        try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
        }
            driver.findElement(By.id("team-options-subnav")).click();
        try {
                Thread.sleep(3000);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }


            driver.findElement(By.cssSelector("li[data-gaaction=\"rename team\"]")).click();
            try {
                Thread.sleep(3000);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }

            driver.findElement(By.className("delete-team")).click();

            try {
                Thread.sleep(3000);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }

            driver.findElement(By.id("disband")).click();
            // Write code here that turns the phrase above into concrete actions
            throw new cucumber.api.PendingException();
        }

    @Then("I will be able to run connected step definitions")
    public void i_will_be_able_to_run_connected_step_definitions() {
        // Write code here that turns the phrase above into concrete actions
        throw new cucumber.api.PendingException();
    }
}
