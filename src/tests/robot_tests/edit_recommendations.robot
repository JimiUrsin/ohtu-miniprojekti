*** Settings ***
Resource  resource.robot
Test Setup  Clear Database

*** Test Cases ***
Recommendation Can Be Deleted
    Insert A New Recommendation  Fifty Shades of Grey  Author  book
    Navigate To Edit Mode From Menu
    Input  1
    Select Deletition In Edit Menu
    Confirm Input
    Exit From Menu
    Run Application
    Output Should Contain  1: Fifty Shades of Grey (book), Author: Author
    Output Should Contain  Confirm deletition. 1: Delete, 0: Cancel

Deleted Recommendation Is Not Shown Anymore
    Insert A New Recommendation  Fifty Shades of Grey  Author  book
    Navigate To Edit Mode From Menu
    Input  1
    Select Deletition In Edit Menu
    Confirm Input
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Exit From Menu
    Run Application
    Output Should Contain  1: Fifty Shades of Grey (book), Author: Author
    Output Should Contain  Confirm deletition. 1: Delete, 0: Cancel
    Output Should Contain  You have no recommendations saved.
    Output Should Not Contain  Fifty Shades of Grey (book), Author: Author

Recommendation Can Be Edited And Old Information Is Not Shown
    Insert A New Recommendation  Pyöreäpöytä  Author  book
    Navigate To Edit Mode From Menu
    Input  1
    Select Edit This Recommendation In Edit Menu
    Input Podcast Information  Podcast Name  Author  4  ""  ""
    Confirm Input
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Exit From Menu
    Run Application
    Output Should Contain  1: Pyöreäpöytä (book), Author: Author
    Output Should Contain  Podcast Name (podcast), Author: Author, URL: "", Comment: ""
    Output Should Not Contain  Pyöreäpöytä (book), Author: Author
