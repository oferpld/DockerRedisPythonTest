from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Class that is responsible for selenium testing of 'Docker Redis Python' web site
class DockerRedisPythonTest:

    def printSiteText(self, siteUrl):
        print('Browsing to {0}...'.format(siteUrl))

        try:
            driverCH = webdriver.Chrome(executable_path="C:/Python/PycharmProjects/Silenium/chromedriver.exe")
            driverCH.implicitly_wait(10)

            driverCH.get(siteUrl)
            bodyElement = driverCH.find_elements_by_xpath('/html/body')
            driverCH.implicitly_wait(10)

            print('Site text is "{0}"'.format(bodyElement[0].text))
        except NoSuchElementException:
            print('Cannot find element within {0} !!'.format(siteUrl))
        except:
            print('Failed to print site text in - {0} !!'.format(siteUrl))
        finally:
            driverCH.close()

def main():
    DockerRedisPythonTest().printSiteText('http://localhost:5000/')

if __name__ == '__main__':
    main()