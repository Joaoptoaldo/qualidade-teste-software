import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class SauceDemoTest {

    private WebDriver driver;

    @BeforeEach
    void iniciar() throws InterruptedException {
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        Thread.sleep(1000);
    }

    /**
    @Test
    void abrirPagina() throws InterruptedException {
        driver.get("https://www.saucedemo.com/"); // acessa pagina
        Thread.sleep(5000);
    }
     */

    @Test
    @DisplayName("RF01 - Login válido deve apresentar o catálogo")
    void loginValidoDeveApresentarCatalago() throws InterruptedException {
        driver.get("https://www.saucedemo.com/");
        Thread.sleep(2000);

        // localiza o campo de usuário pelo ID
        WebElement usuario = driver.findElement(By.id("user-name"));

        // preenche o campo de usuário com o valor "standard_user"
        usuario.sendKeys("standard_user");
        Thread.sleep(2000);

        WebElement senha = driver.findElement(By.id("password"));

        senha.sendKeys("secret_sauce");
        Thread.sleep(2000);

        // localiza o botão de login pelo ID e clica nele
        WebElement login = driver.findElement(By.id("login-button"));
        login.click();
        Thread.sleep(2000);

        // verifica se a URL atual contém "inventory.html", indicando que o login foi bem-sucedido
        assertTrue(
                driver.getCurrentUrl().contains("inventory.html")
        );
    }

    @AfterEach
    void finalizar() {
        if (driver != null) {
            driver.quit(); // encerra a sessão e fecha o navegador
        }
    }
}