** Settings **
Resource  resource.robot
Library  RequestsLibrary
Library  Collections
Library  OperatingSystem

*** Variables ***
${DROPBOX_APP_KEY}  %{DROPBOX_APP_KEY=None}
${DROPBOX_APP_SECRET}  %{DROPBOX_APP_SECRET=None}
${DROPBOX_REFRESH_TOKEN}  %{DROPBOX_REFRESH_TOKEN=None}

${DROPBOX_FILE_PATH}  /robot.json
${LOCAL_DOWNLOAD_PATH}  ${OUTPUT_DIR}${/}downloaded_robot.json

*** Test Cases ***
Käyttäjänä voin synkronoida data eri koneiden välillä CLI-sovelluksessa
    [Documentation]  Tämä on hyväksymiskriteeri Sprint:in 3 Stroylle "Käyttäjänä voin synkronoida data eri koneiden välillä CLI-sovelluksessa"

   ${access_token}=    Get Fresh Access Token

    Download Dropbox File    ${access_token}    ${DROPBOX_FILE_PATH}    ${LOCAL_DOWNLOAD_PATH}

    File Should Exist    ${LOCAL_DOWNLOAD_PATH}

*** Keywords ***
Get Fresh Access Token
    ${data}=    Create Dictionary
    ...    grant_type=refresh_token
    ...    refresh_token=${DROPBOX_REFRESH_TOKEN}
    ...    client_id=${DROPBOX_APP_KEY}
    ...    client_secret=${DROPBOX_APP_SECRET}

    # Dropbox API to refresh token
    ${response}=    POST    https://api.dropbox.com/oauth2/token    data=${data}
    Should Be Equal As Strings    ${response.status_code}    200

    # Ottaa uuden tokenin
    ${token}=    Set Variable    ${response.json()}[access_token]
    RETURN    ${token}

Download Dropbox File
    [Arguments]    ${token}    ${remote_path}    ${local_path}

    # Headers, jotka Dropbox API tarvii
    ${headers}=    Create Dictionary
    ...    Authorization=Bearer ${token}
    ...    Dropbox-API-Arg={"path": "${remote_path}"}

    # Latauksen loppupiste on POST kutsu
    ${response}=    POST    https://content.dropboxapi.com/2/files/download    headers=${headers}
    ...    headers=${headers}
    ...    expected_status=any

    # 4. Jos epäonnistuu, Logataan errorkoodi Dropboxista
    Run Keyword If    ${response.status_code} != 200    Fail    Dropbox Error: ${response.json()}
    # Tallennetaan ladattu data paikallisesti
    Create Binary File    ${local_path}    ${response.content}

    # Tarkistetaan, että data on oikeaa.
    ${content}=      Get File    ${LOCAL_DOWNLOAD_PATH}
    Should Contain    ${content}    {
    Should Contain    ${content}    "entryType": "Inproceedings",
    Should Contain    ${content}    "author": "test",
    Should Contain    ${content}    "title": "test",
    Should Contain    ${content}    "year": "test",
    Should Contain    ${content}    "booktitle": "test",
    Should Contain    ${content}    }
