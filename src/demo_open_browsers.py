from selenium import webdriver
from selenium.webdriver.common.by import By

def demo_in_browser(browser_name: str):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get("https://example.org/")

    h1_text = driver.find_element(By.TAG_NAME, "h1").text
    print(f"[{browser_name}] H1 text:", h1_text)

    driver.quit()

if __name__ == "__main__":
    for b in ("chrome", "firefox"):
        try:
            demo_in_browser(b)
        except Exception as e:
            print(f"Failed in {b}: {e}")
