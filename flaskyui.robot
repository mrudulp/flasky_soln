*** Settings ***
Documentation       Ui automation of Flasky using SeleniumLibrary.
Library             SeleniumLibrary
Library             flask_wrapper.FlaskWrapper

Suite Setup         Open Browser To Index Page
Suite Teardown      Close Browser

*** Variables ***
${LOGIN URL}        http://localhost:8080
${BROWSER}          Chrome

${USERNAME}         admin1
${PASSWORD}         admin1
${FIRSTNAME}        m
${LASTNAME}         p
${PHONE}            1234

*** Test Cases ***
Register through web portal
    [Documentation]     As a UI user I can Register through web portal
    
    Click Link                  Register
    Title Should Be             Register - Demo App
    Fill Registration Form
    Submit Form
    # Verification part
    Title Should Be             Log In - Demo App
    ${user_lists}=              GetUsersList    ${USERNAME}   ${PASSWORD}
    Should Contain              ${user_lists}   ${USERNAME}

Review my own user information from the main view
    [Documentation]     As a UI user I can Review my own user information from the main view

    Click Link                  Log In
    Fill Log In Form
    Submit Form
    # Verification Part
    Title Should Be             User Information - Demo App
    Element Text Should Be      username    ${USERNAME}
    Element Text Should Be      firstname   ${FIRSTNAME}
    Element Text Should Be      lastname    ${LASTNAME}
    Element Text Should Be      phone       ${PHONE}

*** Keywords ***
Open Browser To Index Page
    [Documentation]     Launches the application
    Open Browser                ${LOGIN URL}    ${BROWSER}
    Title Should Be             index page - Demo App
    Page Should Contain Link    Register
    Page Should Contain Link    Log In

Fill Registration Form
    [Documentation]     Fills Registration Form
    Input Text          username        ${USERNAME}
    Input Password      password        ${PASSWORD}
    Input Text          firstname       ${FIRSTNAME}
    Input Text          lastname        ${LASTNAME}
    Input Text          phone           ${PHONE}

Fill Log In Form
    [Documentation]     Fills Log In Form
    Input Text          username        ${USERNAME}
    Input Password      password        ${PASSWORD}
 
