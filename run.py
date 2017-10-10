from selenium import webdriver

def phantom_exemples():
    '''
        Exemples using PhantomJS 
        Didn't display the site
    '''
    print('\n Phanthom JS \n')

    phantom_browser =  webdriver.PhantomJS() 
    phantom_browser.get('http://2017.pythonbrasil.org.br')
    
    # Get page title
    print(phantom_browser.title)

    # Find link in a page
    content = phantom_browser.find_element_by_css_selector('#day5 > div:nth-child(5) > a:nth-child(15)')
    print(content.get_attribute('href'))


    # Find link in a page
    lectures = phantom_browser.find_elements_by_css_selector('#day5 > .lecture')
    speakers_of_the_day_5 = []
    talks_of_the_day_5 = []
    for lecture in lectures:

        try:
            talks_of_the_day_5 += [ t.text for t in lecture.find_elements_by_css_selector('a .talk') ]
        except Exception as e:
            print(e)

        try:
            speakers_of_the_day_5 += [ s.text for s in lecture.find_elements_by_css_selector('.speaker') ] 
        except Exception as e:
            print(e)

    print('Talks: {}'.format(talks_of_the_day_5))
    print('Speakers: {}'.format(speakers_of_the_day_5))

def firefox_exemples():
    '''
        Exemples using geckodriver
        Open Firefox browser 
    '''
    print('\n Firefox \n')

    firefox_browser = webdriver.Firefox()
    firefox_browser.get('http://2017.pythonbrasil.org.br')

    # Click in a button
    firefox_browser.find_element_by_css_selector('#day5 > div:nth-child(5) > a:nth-child(15)').click()

    firefox_browser.quit()    

if __name__ == '__main__':
    phantom_exemples()
    # firefox_exemples()
    



    


