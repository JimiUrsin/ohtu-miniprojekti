*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add A Recommendation To The Database
    Input  1
    Input  Book Name
    Input  1
    Input  1
    Input  0
    Run Application
    Output Should Contain  Is "Book Name", a book, correct? 1: Yes, 2: No, reinput information, 0: Quit
    Output Should Contain  "Book Name" was added!
