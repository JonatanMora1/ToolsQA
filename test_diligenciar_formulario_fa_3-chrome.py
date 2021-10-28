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
    Test: Diligenciar Formulario FA_3
    Generated by: Dina Hurtado (nighwish22@gmail.com)
    Generated on 10/28/2021, 03:05:34
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="15wM28xhucAOs7etwSr8IjyrLJhbrKI9iiG7X_EJ6DQ",
                              project_name="pruebas SW",
                              job_name="Diligenciar Formulario FA_3")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Validar longitud de campo mobile."""
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

    # 3. Scroll window by ('0','264')
    driver.execute_script("window.scrollBy(0,264)")

    # 4. Click 'DIV6'
    div6 = driver.find_element(By.XPATH,
                               "//div[2]/div/div[2]/div")
    div6.click()

    # 5. Scroll window by ('0','-264')
    driver.execute_script("window.scrollBy(0,-264)")

    # 6. Click 'item-0'
    item_0 = driver.find_element(By.XPATH,
                                 "//div[2]/div/ul/li")
    item_0.click()

    # 7. Click 'item-0'
    item_0 = driver.find_element(By.XPATH,
                                 "//div[2]/div/ul/li")
    item_0.click()

    # 8. Click 'First Name'
    first_name = driver.find_element(By.CSS_SELECTOR,
                                     "#firstName")
    first_name.click()

    # 9. Type 'Pruebas' in 'First Name'
    first_name = driver.find_element(By.CSS_SELECTOR,
                                     "#firstName")
    first_name.send_keys("Pruebas")

    # 10. Click 'Last Name'
    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#lastName")
    last_name.click()

    # 11. Type '1' in 'Last Name'
    last_name = driver.find_element(By.CSS_SELECTOR,
                                    "#lastName")
    last_name.send_keys("1")

    # 12. Click 'name@example.com'
    name_example_com = driver.find_element(By.CSS_SELECTOR,
                                           "#userEmail")
    name_example_com.click()

    # 13. Type 'dmhurtado80@ucatolica.edu.co' in 'name@example.com'
    name_example_com = driver.find_element(By.CSS_SELECTOR,
                                           "#userEmail")
    name_example_com.send_keys("dmhurtado80@ucatolica.edu.co")

    # 14. Click 'Other'
    other = driver.find_element(By.XPATH,
                                "//label[. = 'Other']")
    other.click()

    # 15. Click 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.click()

    # 16. Type '12345678' in 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.send_keys("12345678")

    # 17. Click 'dateOfBirthInput'
    dateofbirthinput = driver.find_element(By.CSS_SELECTOR,
                                           "#dateOfBirthInput")
    dateofbirthinput.click()

    # 18. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    select.click()

    # 19. Select the '1987' option in 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    Select(select).select_by_value("1987")

    # 20. Click 'SELECT'
    select = driver.find_element(By.XPATH,
                                 "//div[2]/select")
    select.click()

    # 21. Click '21'
    _21 = driver.find_element(By.XPATH,
                              "//div[. = '21']")
    _21.click()

    # 22. Scroll window by ('0','235')
    driver.execute_script("window.scrollBy(0,235)")

    # 23. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//div[6]/div[2]/div/div/div[1]")
    div1.click()

    # 24. Type 'pruebas longitud' in 'subjectsInput'
    subjectsinput = driver.find_element(By.CSS_SELECTOR,
                                        "#subjectsInput")
    subjectsinput.send_keys("pruebas longitud")

    # 25. Click 'Music'
    music = driver.find_element(By.XPATH,
                                "//label[. = 'Music']")
    music.click()

    # 26. Click 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.click()

    # 27. Scroll window by ('0','158')
    driver.execute_script("window.scrollBy(0,158)")

    # 28. Type 'hjhfhf////' in 'Current Address'
    current_address = driver.find_element(By.CSS_SELECTOR,
                                          "#currentAddress")
    current_address.send_keys("hjhfhf////")

    # 29. Click 'DIV9'
    div9 = driver.find_element(By.XPATH,
                               "//div[10]/div[2]/div/div[1]/div[1]")
    div9.click()

    # 30. Click 'Uttar Pradesh'
    uttar_pradesh = driver.find_element(By.CSS_SELECTOR,
                                        "#react-select-3-option-1")
    uttar_pradesh.click()

    # 31. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[3]/div/div[1]/div[1]")
    div2.click()

    # 32. Click 'Delhi'
    delhi = driver.find_element(By.CSS_SELECTOR,
                                "#react-select-4-option-0")
    delhi.click()

    # 33. Click 'Submit'
    submit = driver.find_element(By.CSS_SELECTOR,
                                 "#submit")
    submit.click()

    # 34. Scroll window by ('0','-226')
    driver.execute_script("window.scrollBy(0,-226)")

    # 35. Scroll window by ('0','-2')
    driver.execute_script("window.scrollBy(0,-2)")

    # 36. Click 'Mobile Number'
    mobile_number = driver.find_element(By.CSS_SELECTOR,
                                        "#userNumber")
    mobile_number.click()
