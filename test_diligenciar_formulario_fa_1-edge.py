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
    Test: Diligenciar Formulario FA_1
    Generated by: Dina Hurtado (nighwish22@gmail.com)
    Generated on 10/28/2021, 03:08:55
"""


@pytest.fixture()
def driver():
    driver = webdriver.Edge(token="15wM28xhucAOs7etwSr8IjyrLJhbrKI9iiG7X_EJ6DQ",
                            project_name="pruebas SW",
                            job_name="Diligenciar Formulario FA_1")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Validar obligatoriedad de los campos."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://demoqa.com/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Scroll window by ('0','333')
    driver.execute_script("window.scrollBy(0,333)")

    # 3. Click 'DIV'
    div = driver.find_element(By.XPATH,
                              "//div[2]/div/div/div[2]/div/div[2]")
    div.click()

    # 4. Scroll window by ('0','-333')
    driver.execute_script("window.scrollBy(0,-333)")

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

    # 8. Click 'name@example.com'
    name_example_com = driver.find_element(By.CSS_SELECTOR,
                                           "#userEmail")
    name_example_com.click()

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

    # 12. Click 'dateOfBirthInput'
    dateofbirthinput = driver.find_element(By.CSS_SELECTOR,
                                           "#dateOfBirthInput")
    dateofbirthinput.click()

    # 13. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    select.click()

    # 14. Select the '1985' option in 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    Select(select).select_by_value("1985")

    # 15. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    select.click()

    # 16. Click '22'
    _22 = driver.find_element(By.XPATH,
                              "//div[. = '22']")
    _22.click()

    # 17. Scroll window by ('0','301')
    driver.execute_script("window.scrollBy(0,301)")

    # 18. Scroll window by ('0','2')
    driver.execute_script("window.scrollBy(0,2)")

    # 19. Scroll window by ('0','24')
    driver.execute_script("window.scrollBy(0,24)")

    # 20. Scroll window by ('0','28')
    driver.execute_script("window.scrollBy(0,28)")

    # 21. Scroll window by ('0','48')
    driver.execute_script("window.scrollBy(0,48)")

    # 22. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//div[6]/div[2]/div/div/div[1]")
    div1.click()

    # 23. Type 'pruebas campos obligatorios' in 'subjectsInput'
    subjectsinput = driver.find_element(By.CSS_SELECTOR,
                                        "#subjectsInput")
    subjectsinput.send_keys("pruebas campos obligatorios")

    # 24. Click 'Reading'
    reading = driver.find_element(By.XPATH,
                                  "//label[. = 'Reading']")
    reading.click()

    # 25. Click 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.click()

    # 26. Type 'kjdsfkhdafh' in 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.send_keys("kjdsfkhdafh")

    # 27. Click 'DIV4'
    div4 = driver.find_element(By.XPATH,
                               "//div/div[2]/div/div[1]/div[2]/div")
    div4.click()

    # 28. Click 'Uttar Pradesh'
    uttar_pradesh = driver.find_element(By.CSS_SELECTOR,
                                        "#react-select-3-option-1")
    uttar_pradesh.click()

    # 29. Click 'DIV5'
    div5 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[1]/div[2]/div")
    div5.click()

    # 30. Click 'DIV3'
    div3 = driver.find_element(By.XPATH,
                               "//body/div[1]/div/div[1]")
    div3.click()

    # 31. Click 'Submit'
    submit = driver.find_element(By.CSS_SELECTOR,
                                 "#submit")
    submit.click()

    # 32. Scroll window by ('0','-361')
    driver.execute_script("window.scrollBy(0,-361)")

    # 33. Scroll window by ('0','-2')
    driver.execute_script("window.scrollBy(0,-2)")

    # 34. Scroll window by ('0','-4')
    driver.execute_script("window.scrollBy(0,-4)")

    # 35. Click 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.click()

    # 36. Type '3006555219' in 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.send_keys("3006555219")

    # 37. Click 'Last Name'
    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#lastName")
    last_name.click()

    # 38. Scroll window by ('0','237')
    driver.execute_script("window.scrollBy(0,237)")

    # 39. Scroll window by ('0','257')
    driver.execute_script("window.scrollBy(0,257)")

    # 40. Type 'hurtado' in 'Last Name'
    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#lastName")
    last_name.send_keys("hurtado")

    # 41. Click 'Submit'
    submit = driver.find_element(By.CSS_SELECTOR,
                                 "#submit")
    submit.click()

    '''
    # (STEP DISABLED)
    # 42. Click 'Ad.Plus Advertising'
    ad_plus_advertising = driver.find_element(By.XPATH,
    "//div/div/div[1]/a/img")
    ad_plus_advertising.click()
    '''

    '''
    # (STEP DISABLED)
    # 43. Click 'Close'
    close = driver.find_element(By.CSS_SELECTOR,
    "#closeLargeModal")
    close.click()
    '''
