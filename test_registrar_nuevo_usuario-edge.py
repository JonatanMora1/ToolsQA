from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: pruebas SW
    Package: TestProject.Generated.Tests.PruebasSw
    Test: Registrar nuevo usuario
    Generated by: Dina Hurtado (nighwish22@gmail.com)
    Generated on 10/28/2021, 03:07:13
"""


@pytest.fixture()
def driver():
    driver = webdriver.Edge(token="15wM28xhucAOs7etwSr8IjyrLJhbrKI9iiG7X_EJ6DQ",
                            project_name="pruebas SW",
                            job_name="Registrar nuevo usuario")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Validar el registro de un nuevo usuario en la aplicación “Book Store”."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://demoqa.com/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Ad.Plus Advertising1'
    ad_plus_advertising1 = driver.find_element(By.XPATH,
                                               "//body/div[1]//img")
    ad_plus_advertising1.click()

    # 3. Scroll window by ('0','680')
    driver.execute_script("window.scrollBy(0,680)")

    # 4. Click 'DIV11'
    div11 = driver.find_element(By.XPATH,
                                "//div[6]")
    div11.click()

    # 5. Scroll window by ('0','-680')
    driver.execute_script("window.scrollBy(0,-680)")

    # 6. Scroll window by ('0','494')
    driver.execute_script("window.scrollBy(0,494)")

    # 7. Scroll window by ('0','40')
    driver.execute_script("window.scrollBy(0,40)")

    # 8. Scroll window by ('0','-492')
    driver.execute_script("window.scrollBy(0,-492)")

    # 9. Click 'Login'
    login = driver.find_element(By.CSS_SELECTOR,
                                "#login")
    login.click()

    # 10. Scroll window by ('0','-42')
    driver.execute_script("window.scrollBy(0,-42)")

    # 11. Click 'New User'
    new_user = driver.find_element(By.CSS_SELECTOR,
                                   "#newUser")
    new_user.click()

    # 12. Click 'First Name1'
    first_name1 = driver.find_element(By.CSS_SELECTOR,
                                      "#firstname")
    first_name1.click()

    # 13. Type 'pruebas' in 'First Name1'
    first_name1 = driver.find_element(By.CSS_SELECTOR,
                                      "#firstname")
    first_name1.send_keys("pruebas")

    # 14. Click 'Last Name1'
    last_name1 = driver.find_element(By.CSS_SELECTOR,
                                     "#lastname")
    last_name1.click()

    # 15. Type 'uno' in 'Last Name1'
    last_name1 = driver.find_element(By.CSS_SELECTOR,
                                     "#lastname")
    last_name1.send_keys("uno")

    # 16. Click 'UserName'
    username = driver.find_element(By.CSS_SELECTOR,
                                   "#userName")
    username.click()

    # 17. Type 'pruebas1' in 'UserName'
    username = driver.find_element(By.CSS_SELECTOR,
                                   "#userName")
    username.send_keys("pruebas1")

    # 18. Click 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.click()

    # 19. Scroll window by ('0','172')
    driver.execute_script("window.scrollBy(0,172)")

    # 20. Type 'Dimi2209*' in 'Password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.send_keys("Dimi2209*")

    # 21. Click 'DIV12'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@name = 'a-pu7p0l59gt4t']|/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[6]/div/div/div/iframe"))
    div12 = driver.find_element(By.XPATH,
                                "//span/div[1]")
    div12.click()

    # 22. Click 'Register'
    register = driver.find_element(By.CSS_SELECTOR,
                                   "#register")
    register.click()