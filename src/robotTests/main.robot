** Settings **
Resource  resource.robot

*** Test Cases ***
ViiteRepository New Command Test
    Input New Command
    ${result}=  Input Book  key1 Matti Meikäläinen  Testikirja  2020  Testikustantaja
    Log To Console  ${result}

    Should Contain    ${result}    Luotu: @book{key1,
    Should Contain    ${result}    author = {Matti Meikäläinen},
    Should Contain    ${result}    title = {Testikirja},
    Should Contain    ${result}    year = {2020},
    Should Contain    ${result}    publisher = {Testikustantaja},
