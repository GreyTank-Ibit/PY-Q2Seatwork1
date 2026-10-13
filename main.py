from pyscript import document,display

def checkName(e):

    firstname = ["Gian", "Roque", "Isaias", "Cameron"]
    lastname = ["Ibit", "Saludes", "Berdin", "Bufford"]

    num1=document.getElementById("num1").value
    lastName=document.getElementById("lastName").value
    name=f"{num1} {lastName}"

    confirm_num = any(num1 == first and lastName == last for first, last in zip(firstname, lastname))

    message= (f'I\'m sorry {name}, you aren\'t a member of Math Club!.', f'Yahoo! {name}, you are a member of Math Club!')

    document.getElementById("output1").innerHTML = message[confirm_num]