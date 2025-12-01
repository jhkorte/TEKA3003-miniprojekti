*** Settings ***
Library  ../mainLibrary.py

*** Keywords ***
Input New Command
    Input  new

Input Hae Command
    Input  hae

Input Print Command
    Input  print

Input Book Command
    #Input  book
    #Input  Matti Meikäläinen
    #Input  Testikirja
    #Input  2020
    #Input  Testikustantaja
    ${result}=  Input Book
    RETURN    ${result}
