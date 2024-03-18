from testpage import OperationsHelper


def test_step1(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_name("zoya")
    testpage.enter_email("example@test.com")
    testpage.enter_content("test content")
    testpage.submit_contact()
    assert testpage.get_alert_text() == "Form successfully submitted"
