*** Settings ***
Resource  resource.robot
Test Setup  Clear Database

*** Test Cases ***
Recommendation Can Be Deleted
    Insert A New Recommendation  Fifty Shades of Grey  video
    Navigate To Edit Mode From Menu
    Input  1
    Select Deletition In Edit Menu
    Confirm Input
    Exit From Menu
    Run Application
    Output Should Contain  1: Fifty Shades of Grey (video)
    Output Should Contain  Confirm deletition. 1: Delete, 0: Cancel

Deleted Recommendation Is Not Shown Anymore
    Insert A New Recommendation  Fifty Shades of Grey  video
    Navigate To Edit Mode From Menu
    Input  1
    Select Deletition In Edit Menu
    Confirm Input
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Run Application
    Output Should Contain  1: Fifty Shades of Grey (video)
    Output Should Contain  Confirm deletition. 1: Delete, 0: Cancel
    Output Should Contain  You have no recommendations saved.
    Output Should Not Contain  Fifty Shades of Grey (video)

Recommendation Can Be Edited And Old Information Is Not Shown
    Insert A New Recommendation  Pyöreäpöytä  podcast
    Navigate To Edit Mode From Menu
    Input  1
    Select Edit This Recommendation In Edit Menu
    Input Recommendation Information  The Cuckoo's Egg  1
    Confirm Input
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Run Application
    Output Should Contain  1: Pyöreäpöytä (podcast)
    Output Should Contain  The Cuckoo's Egg (book)
    Output Should Not Contain  Pyöreäpöytä (podcast)