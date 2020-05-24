import  time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_quest_should_see_login_link_pass(driver):
     driver.get(link)

     time.sleep(30)
     
     button = len(driver.find_elements_by_css_selector(".btn.btn-add-to-basket"))
     assert button >0, "button not found!"









