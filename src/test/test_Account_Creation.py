import pytest

from src.pageFactory.pageRepository.create_Account_Page import AccountCreate

@pytest.mark.smoke
@pytest.mark.sanitty
def test_account_creation(driver_c):
    account = AccountCreate(driver_c)

    account.account_type_selection()
    account.entering_name()
    account.entering_dob_and_gender()