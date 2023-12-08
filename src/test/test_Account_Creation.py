import pytest

from src.pageFactory.pageRepository.create_Account_Page import AccountCreate

@pytest.mark.smoke
@pytest.mark.sanitty
def test_account_creation(driver):
    account = AccountCreate(driver)

    account.account_type_selection()
    account.entering_name()
    account.entering_dob_and_gender()