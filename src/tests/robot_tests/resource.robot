*** Settings ***
Library  ../../RobotLibrary.py

*** Keywords ***
Navigate To Add A Recommendation From Menu
    Input  1

Navigate To Browse Recommendations From Menu
    Input  2

Navigate To Edit Mode From Menu
    Input  3

Exit From Menu
    Input  0

Confirm Input
    Input  1

Select Deletition In Edit Menu
    Input  2

Select Edit This Recommendation In Edit Menu
    Input  1

Input Book Information
    [Arguments]  ${title}  ${author}  ${recom_type}  ${isbn}  ${comment}  ${description}
    Input  ${title}
    Input  ${author}
    Input  ${recom_type}
	Input  ${isbn}
	Input  ${comment}
	Input  ${description}
	
Input Video Or Blog Information
    [Arguments]  ${title}  ${author}  ${recom_type}  ${url}  ${comment}  ${description}
    Input  ${title}
    Input  ${author}
    Input  ${recom_type}
	Input  ${url}
	Input  ${comment}
	Input  ${description}
	
Input Podcast Information
    [Arguments]  ${title}  ${author}  ${recom_type}  ${url}  ${comment}
    Input  ${title}
    Input  ${author}
    Input  ${recom_type}
	Input  ${url}
	Input  ${comment}
