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

Input Recommendation Information
    [Arguments]  ${title}  ${recom_type}
    Input  ${title}
    Input  ${recom_type}