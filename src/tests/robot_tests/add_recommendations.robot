*** Settings ***
Resource  resource.robot
Test Setup  Setup Database

*** Test Cases ***
Add A Book Recommendation With A Description, Isbn And Comment To The Database 
    Navigate To Add A Recommendation From Menu
    Input Book Information  Book Name  Author  1  ISBN  Comment  Description
    Confirm Input
    Exit From Menu
    Run Application
    Output Should Contain  "Book Name" was added!
    
Add A Video Recommendation With A Description, Url And Comment To The Database
    Navigate To Add A Recommendation From Menu
    Input Video Or Blog Information  Video Name  Author  2  URL  Comment  Description
    Confirm Input
    Exit From Menu
    Run Application
    Output Should Contain  "Video Name" was added!
    
Add A Blog Recommendation With A Description, Url And Comment To The Database
    Navigate To Add A Recommendation From Menu
    Input Video Or Blog Information  Blog Name  Author  3  URL  Comment  Description
    Confirm Input
    Exit From Menu
    Run Application
    Output Should Contain  "Blog Name" was added!
    
Add A Podcast Recommendation With Url And Comment To The Database
    Navigate To Add A Recommendation From Menu
    Input Podcast Information  Podcast Name  Author  4  URL  Comment
    Confirm Input
    Exit From Menu
    Run Application
    Output Should Contain  "Podcast Name" was added!

Browsing Recommendations Where Some Have Been Created
    Insert A New Recommendation  Animorphs The Invasion  Author  book
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Exit From Menu
    Run Application
    Output Should Contain   Animorphs The Invasion (book), Author: Author

Browsing Recommendations Where There Are None Created
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Exit From Menu
    Run Application
    Output Should Contain  You have no recommendations saved.

Created Recommendation Is Displayed In Browse Mode
    Navigate To Add A Recommendation From Menu
    Input Book Information  Book Name  Author  1  ISBN1000  Good  This is a book.
    Confirm Input
    Navigate To Browse Recommendations From Menu
    Exit From Menu
    Exit From Menu
    Run Application
    Output Should Contain  Book Name (book), Author: Author, ISBN: ISBN1000, Decription: This is a book., Comment: Good
