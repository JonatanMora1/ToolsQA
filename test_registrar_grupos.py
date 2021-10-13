from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.Generated.Tests.MyFirstProject
    Test: Registrar Grupos
    Generated by: JONATAN ALEXANDER MORA LADINO (jamora649@ucatolica.edu.co)
    Generated on 10/13/2021, 15:33:02
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="AJINYVeRnsa_fctNQarCvNuzlv3Ck0fNyGkTXrfx0-g",
                              project_name="My first Project",
                              job_name="Registrar Grupos")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """El sistema deberá mostrar formulario para registro de usuario  en grupos, permitiendo diligenciamiento y cargue."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://demoqa.com/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 3. Click 'path'
    path = driver.find_element(By.XPATH,
                               "//div[4]//*[name()='path']")
    path.click()

    # 4. Scroll window by ('0','-100')
    driver.execute_script("window.scrollBy(0,-100)")

    # 5. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 6. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 7. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 8. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 9. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 10. Scroll window by ('0','100')
    driver.execute_script("window.scrollBy(0,100)")

    # 11. Click 'Select Menu'
    select_menu = driver.find_element(By.XPATH,
                                      "//span[. = 'Select Menu']")
    select_menu.click()

    # 12. Scroll window by ('0','-600')
    driver.execute_script("window.scrollBy(0,-600)")

    # 13. Click 'DIV2'
    div2 = driver.find_element(By.XPATH,
                               "//div[2]/div[1]/div[2]/div/div/div[1]/div[1]")
    div2.click()

    # 14. Click 'Group 1, option 2'
    group_1_option_2 = driver.find_element(By.CSS_SELECTOR,
                                           "#react-select-2-option-0-1")
    group_1_option_2.click()

    # 15. Click 'DIV3'
    div3 = driver.find_element(By.XPATH,
                               "//div[4]/div/div/div[1]/div[1]")
    div3.click()

    # 16. Click 'Mr.'
    mr_ = driver.find_element(By.CSS_SELECTOR,
                              "#react-select-3-option-0-1")
    mr_.click()

    # 17. Click 'oldSelectMenu'
    oldselectmenu = driver.find_element(By.CSS_SELECTOR,
                                        "#oldSelectMenu")
    oldselectmenu.click()

    # 18. Select the '4' option in 'oldSelectMenu'
    oldselectmenu = driver.find_element(By.CSS_SELECTOR,
                                        "#oldSelectMenu")
    Select(oldselectmenu).select_by_value("4")

    # 19. Click 'oldSelectMenu'
    oldselectmenu = driver.find_element(By.CSS_SELECTOR,
                                        "#oldSelectMenu")
    oldselectmenu.click()

    # 20. Scroll window by ('0','200')
    driver.execute_script("window.scrollBy(0,200)")

    # 21. Click 'DIV4'
    div4 = driver.find_element(By.XPATH,
                               "//div[7]/div/div/div[1]/div[1]")
    div4.click()

    # 22. Click 'Blue1'
    blue1 = driver.find_element(By.CSS_SELECTOR,
                                "#react-select-4-option-1")
    blue1.click()

    # 23. Click 'Red'
    red = driver.find_element(By.CSS_SELECTOR,
                              "#react-select-4-option-3")
    red.click()

    # 24. Select the 'opel' option in 'cars'
    cars = driver.find_element(By.CSS_SELECTOR,
                               "#cars")
    Select(cars).select_by_value("opel")

    # 25. Click 'Opel'
    opel = driver.find_element(By.XPATH,
                               "//option[. = 'Opel']")
    opel.click()

    # 26. Scroll window by ('0','300')
    driver.execute_script("window.scrollBy(0,300)")