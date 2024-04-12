from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BOX_LINKS = (By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")


@then("Verify there are {expected_number_of_boxes} Benefit boxes")
def verify_target_circle_boxes(context, expected_number_of_boxes):  # Expected here is 10
    actual_number_of_boxes = int(expected_number_of_boxes)
    total_number_of_boxes = context.driver.find_elements(*BOX_LINKS)
    sleep(5)
    assert len(total_number_of_boxes) == actual_number_of_boxes, \
        f"Expected {actual_number_of_boxes} but got {len(total_number_of_boxes)}"
