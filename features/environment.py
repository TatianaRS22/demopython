from selenium.webdriver import Chrome

def before_scenario(context, scenario):
    context.driver = Chrome('resources/chromedriver')
    
def after_scenario(context, scenario):    
    context.driver.quit()

