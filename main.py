from selenium import webdriver


def main() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    print(driver.title)
    driver.close()


if __name__ == "__main__":
    main()
