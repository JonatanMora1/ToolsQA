from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: pruebas SW
    Package: TestProject.Generated.Tests.PruebasSw
    Test: Diligenciar Formulario
    Generated by: Dina Hurtado (nighwish22@gmail.com)
    Generated on 10/28/2021, 01:58:11
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="15wM28xhucAOs7etwSr8IjyrLJhbrKI9iiG7X_EJ6DQ",
                              project_name="pruebas SW",
                              job_name="Diligenciar Formulario")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """El sistema deberá mostrar el formulario de registro de un estudiante, permitir su diligenciamiento y registro en el mismo."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://demoqa.com/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Scroll window by ('0','349')
    driver.execute_script("window.scrollBy(0,349)")

    # 3. Click 'DIV'
    div = driver.find_element(By.XPATH,
                              "//div[2]/div/div/div[2]/div/div[2]")
    div.click()

    # 4. Scroll window by ('0','-349')
    driver.execute_script("window.scrollBy(0,-349)")

    # 5. Click 'item-0'
    item_0 = driver.find_element(By.XPATH,
                                 "//div[2]/div/ul/li")
    item_0.click()

    # 6. Click 'First Name'
    first_name = driver.find_element(By.CSS_SELECTOR,
                                     "#firstName")
    first_name.click()

    # 7. Type 'Dina' in 'First Name'
    first_name = driver.find_element(By.CSS_SELECTOR,
                                     "#firstName")
    first_name.send_keys("Dina")

    # 8. Type 'pruebas 1' in 'Last Name'
    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#lastName")
    last_name.send_keys("pruebas 1")

    # 9. Click 'name@example.com'
    name_example_com = driver.find_element(By.CSS_SELECTOR,
                                           "#userEmail")
    name_example_com.click()

    # 10. Type 'dinamilena99@hotmail.com' in 'name@example.com'
    name_example_com = driver.find_element(By.CSS_SELECTOR,
                                           "#userEmail")
    name_example_com.send_keys("dinamilena99@hotmail.com")

    # 11. Click 'Female'
    female = driver.find_element(By.XPATH,
                                 "//label[. = 'Female']")
    female.click()

    # 12. Click 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.click()

    # 13. Type '3006555219' in 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.send_keys("3006555219")

    # 14. Click 'dateOfBirthInput'
    dateofbirthinput = driver.find_element(By.CSS_SELECTOR,
                                           "#dateOfBirthInput")
    dateofbirthinput.click()

    # 15. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    select.click()

    # 16. Select the '1985' option in 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    Select(select).select_by_value("1985")

    # 17. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    select.click()

    # 18. Click '22'
    _22 = driver.find_element(By.XPATH,
                              "//div[. = '22']")
    _22.click()

    # 19. Scroll window by ('0','221')
    driver.execute_script("window.scrollBy(0,221)")

    # 20. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//div[6]/div[2]/div/div/div[1]")
    div1.click()

    # 21. Type 'pruebas caso 1' in 'subjectsInput'
    subjectsinput = driver.find_element(By.CSS_SELECTOR,
                                        "#subjectsInput")
    subjectsinput.send_keys("pruebas caso 1")

    # 22. Click 'Music'
    music = driver.find_element(By.XPATH,
                                "//label[. = 'Music']")
    music.click()

    # 23. Click 'uploadPicture'
    uploadpicture = driver.find_element(By.CSS_SELECTOR,
                                        "#uploadPicture")
    uploadpicture.click()

    # 24. Type 'C:\fakepath\Logo_ucatolica.jpg' in 'uploadPicture'
    uploadpicture = driver.find_element(By.CSS_SELECTOR,
                                        "#uploadPicture")
    uploadpicture.send_keys("C:\\fakepath\\Logo_ucatolica.jpg")

    # 25. Click 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.click()

    # 26. Scroll window by ('0','253')
    driver.execute_script("window.scrollBy(0,253)")

    # 27. Type 'calle 13 sur' in 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.send_keys("calle 13 sur")

    # 28. Click 'svg'
    svg = driver.find_element(By.XPATH,
                              "//div[2]/div/div[1]/div[2]/div/*[name()='svg']")
    svg.click()

    # 29. Click 'NCR'
    ncr = driver.find_element(By.CSS_SELECTOR,
                              "#react-select-3-option-0")
    ncr.click()

    # 30. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[1]/div[1]")
    div2.click()

    # 31. Click 'Delhi'
    delhi = driver.find_element(By.CSS_SELECTOR,
                                "#react-select-4-option-0")
    delhi.click()

    # 32. Click 'Submit'
    submit = driver.find_element(By.CSS_SELECTOR,
                                 "#submit")
    submit.click()

    # 33. Click 'Ad.Plus Advertising'
    ad_plus_advertising = driver.find_element(By.XPATH,
                                              "//div/div/div[1]/a/img")
    ad_plus_advertising.click()

    # 34. Click 'Close'
    close = driver.find_element(By.CSS_SELECTOR,
                                "#closeLargeModal")
    close.click()
