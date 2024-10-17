const firstEl = document.getElementById("first")

const secondEl = document.getElementById("second")
const thirdEl = document.getElementById("third")
const fourthEl = document.getElementById("fourth")
const email_firstEl = document.getElementById("email_first")
const contact_firstEl = document.getElementById("contact_first")
const pass_firstEl = document.getElementById("pass-first")
const pass_secondEl = document.getElementById("pass-second")
const pass_thirdEl = document.getElementById("pass-third")
const pass_fourthEl = document.getElementById("pass-fourth")
const pass_fifthEl = document.getElementById("pass-fifth")
const pass_value = document.getElementById("id_password")
const cpass = document.getElementById("cpass-first")

function validateUName(e) {
    console.log(e.trim());
    let name = ""
    name = name+e;
    name = name.trim();
    

    if(name.length<7 || name.length>11){
        firstEl.style.color = "red"
        firstEl.style.textDecoration="none"

    }else{
        firstEl.style.color = "green"
        firstEl.style.textDecoration="line-through"
    }


    var format = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/ ;


    if(e.match(format) ){
        secondEl.style.color = "red"
        secondEl.style.textDecoration="none"
        fourthEl.style.color = "red"
        fourthEl.style.textDecoration="none"
      }else{
        secondEl.style.color = "green"
        secondEl.style.textDecoration="line-through"
        fourthEl.style.color = "green"
        fourthEl.style.textDecoration="line-through"
      }

      function checkWhitespace(str) {
        return /\s/.test(str);
    }

    if(checkWhitespace(name)){
        thirdEl.style.color = "red";
        thirdEl.style.textDecoration="none"
    }
    else{
        thirdEl.style.color = "green";
        thirdEl.style.textDecoration="line-through"
    }
    



}

function validateEmail(e){
    let email = ""
    email = email+e;
    email = email.trim();


    var format = /[!#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/ ;
    var char = /@/

    if(e.match(format)){
        email_firstEl.style.color = "red";
        email_firstEl.style.textDecoration="none"

    }
    else{
        email_firstEl.style.color = "green";
        email_firstEl.style.textDecoration="line-through"
    }

    if(e.match(char)){
        
        email_firstEl.style.color = "green";
        email_firstEl.style.textDecoration="line-through"

    }
    else{
        email_firstEl.style.color = "red";
        email_firstEl.style.textDecoration="none"
    }

}

function validateContact(e){
    let contact = ""
    contact = contact+e;

    if(contact.length==10){
        
        contact_firstEl.style.color = "green"
        contact_firstEl.style.textDecoration="line-through"

    }else{
        contact_firstEl.style.color = "red"
        contact_firstEl.style.textDecoration="none"
        
    }
}

function validatePassword(e){
    let password = ""
    password = password+e;
    console.log(e)

    if(password.length<8 || password.length>12){
        pass_firstEl.style.color = "red"
        pass_firstEl.style.textDecoration="none"

    }else{
        pass_firstEl.style.color = "green"
        pass_firstEl.style.textDecoration="line-through"
    }

    let uppcase = 0;
    let number = 0;
    let special = 0;

    var format = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/ ;
    var num = /[0-9]/
    var ucase = /[A-Z]/

    if(e.match(ucase) ){
        pass_thirdEl.style.color = "green";
        pass_thirdEl.style.textDecoration="line-through";
        uppcase++;
      }else{
        pass_thirdEl.style.color = "red";
        pass_thirdEl.style.textDecoration="none";
      }

      if(e.match(num) ){
        pass_fourthEl.style.color = "green";
        pass_fourthEl.style.textDecoration="line-through";
        number++;
      }else{
        pass_fourthEl.style.color = "red";
        pass_fourthEl.style.textDecoration="none";
      }
      if(e.match(format) ){
        pass_fifthEl.style.color = "green";
        pass_fifthEl.style.textDecoration="line-through";
        special++;
      }else{
        pass_fifthEl.style.color = "red";
        pass_fifthEl.style.textDecoration="none";
      }

      if(uppcase && number && special){
        pass_secondEl.style.color = "green";
        pass_secondEl.style.textDecoration="line-through";
      }else{
        pass_secondEl.style.color = "red";
        pass_secondEl.style.textDecoration="none";
      }




}

function validateC_Password(e){
    let password = pass_value.value;

    let cpassword = ""
    cpassword = cpassword+e;

    if(cpassword==password){
        cpass.style.color="green";
        cpass.style.textDecoration="line-through";

    }else{
        cpass.style.color="red";
        cpass.style.textDecoration="none";
    }

}