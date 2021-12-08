*** Settings ***
Resource  resource.robot
Test Setup  Clear Database

*** Test Cases ***
Add A Recommendation To The Database
    Navigate To Add A Recommendation From Menu
    Input Recommendation Information  Book Name  1
    Confirm Input
    Exit From Menu
    Run Application
    Output Should Contain  "Book Name" was added!

Browsing Recommendations Where Some Have Been Created
    Insert A New Recommendation  Animorphs The Invasion  book
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Run Application
    Output Should Contain   Animorphs The Invasion (book)

Browsing Recommendations Where The Are None Created
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Run Application
    Output Should Contain  You have no recommendations saved.

Created Recommendation Is Displayed In Browse Mode
    Navigate To Add A Recommendation From Menu
    Input Recommendation Information  Fifty Shades of Grey  1
    Confirm Input
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Run Application
    Output Should Contain  Fifty Shades of Grey (book)