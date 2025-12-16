*** Settings ***
Library  RequestsLibrary
Library  String

*** Variables ***
${DOI_API_URL}  https://doi.org
${TEST_DOI}  10.1038/nature12345

*** Test Cases ***
Käyttäjänä voin hakea datan DOI-tunnisteen perusteella
    Create Session  doi_session  ${DOI_API_URL}  verify=${True}

    ${headers}=  Create Dictionary  Accept=application/x-bibtex

    ${response}=  GET On Session  doi_session  /${TEST_DOI}  headers=${headers}  expected_status=200
    Log  The Doi object is: \n ${response.text}

    Should Match Regexp  ${response.text}  ^\\s*@.*\{  msg=Response is not a valid BibTeX entry

    Should Contain    ${response.text}    ${TEST_DOI}
