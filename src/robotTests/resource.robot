*** Settings ***
Library  ../mainLibrary.py

*** Keywords ***
Input New Command
    Input  new

Input Hae Command
    Input  hae

<<<<<<< HEAD
Input Book Command
    #Input  book
    #Input  Matti Meikäläinen
    #Input  Testikirja
    #Input  2020
    #Input  Testikustantaja
    ${result}=  Input Book
    RETURN    ${result}
=======
Input Print Command
    Input  print
>>>>>>> 4bd5e8bf0ca302063b0ef9dff363ee5ad96b2927
