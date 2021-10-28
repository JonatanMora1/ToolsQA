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
    Test: Diligenciar Formulario FA_2
    Generated by: Dina Hurtado (nighwish22@gmail.com)
    Generated on 10/28/2021, 03:08:08
"""


@pytest.fixture()
def driver():
    driver = webdriver.Edge(token="15wM28xhucAOs7etwSr8IjyrLJhbrKI9iiG7X_EJ6DQ",
                            project_name="pruebas SW",
                            job_name="Diligenciar Formulario FA_2")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Validar tipo de datos."""
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

    # 3. Click 'DIV8'
    div8 = driver.find_element(By.XPATH,
                               "//div[2]/div/div[2]/div/div[1]")
    div8.click()

    # 4. Click 'Practice Form'
    practice_form = driver.find_element(By.XPATH,
                                        "//span[. = 'Practice Form']")
    practice_form.click()

    # 5. Click 'First Name'
    first_name = driver.find_element(By.CSS_SELECTOR,
                                     "#firstName")
    first_name.click()

    # 6. Type 'pruebas' in 'First Name'
    first_name = driver.find_element(By.CSS_SELECTOR,
                                     "#firstName")
    first_name.send_keys("pruebas")

    # 7. Click 'Last Name'
    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#lastName")
    last_name.click()

    # 8. Type '1' in 'Last Name'
    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#lastName")
    last_name.send_keys("1")

    # 9. Click 'name@example.com'
    name_example_com = driver.find_element(By.CSS_SELECTOR,
                                           "#userEmail")
    name_example_com.click()

    # 10. Type 'dmhurtado80@ucatolica.edu.co' in 'name@example.com'
    name_example_com = driver.find_element(By.CSS_SELECTOR,
                                           "#userEmail")
    name_example_com.send_keys("dmhurtado80@ucatolica.edu.co")

    # 11. Click 'Female'
    female = driver.find_element(By.XPATH,
                                 "//label[. = 'Female']")
    female.click()

    # 12. Click 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.click()

    # 13. Type '300abc5219' in 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.send_keys("300abc5219")

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

    # 18. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[1]/select")
    select1.click()

    # 19. Select the '8' option in 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[1]/select")
    Select(select1).select_by_value("8")

    # 20. Click 'SELECT1'
    select1 = driver.find_element(By.XPATH,
                                  "//div[1]/select")
    select1.click()

    # 21. Click '22'
    _22 = driver.find_element(By.XPATH,
                              "//div[. = '22']")
    _22.click()

    # 22. Scroll window by ('0','327')
    driver.execute_script("window.scrollBy(0,327)")

    # 23. Click 'Reading'
    reading = driver.find_element(By.XPATH,
                                  "//label[. = 'Reading']")
    reading.click()

    # 24. Click 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.click()

    # 25. Type 'khsfahs%&&' in 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.send_keys("khsfahs%&&")

    # 26. Click 'state'
    state = driver.find_element(By.CSS_SELECTOR,
                                "#state")
    state.click()

    # 27. Scroll window by ('0','65')
    driver.execute_script("window.scrollBy(0,65)")

    # 28. Click 'NCR'
    ncr = driver.find_element(By.CSS_SELECTOR,
                              "#react-select-3-option-0")
    ncr.click()

    # 29. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[1]/div[1]")
    div2.click()

    # 30. Click 'Delhi'
    delhi = driver.find_element(By.CSS_SELECTOR,
                                "#react-select-4-option-0")
    delhi.click()

    # 31. Click 'Submit'
    submit = driver.find_element(By.CSS_SELECTOR,
                                 "#submit")
    submit.click()

    # 32. Scroll window by ('0','-176')
    driver.execute_script("window.scrollBy(0,-176)")

    # 33. Scroll window by ('0','-21')
    driver.execute_script("window.scrollBy(0,-21)")

    # 34. Scroll window by ('0','-2')
    driver.execute_script("window.scrollBy(0,-2)")
