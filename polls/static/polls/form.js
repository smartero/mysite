// register.html
let form = document.getElementById('registration');
form.onsubmit = function(){

    if(!form.username.value)
    {
        alert('Provide username');
        return false;
    }

    else if (!form.email.value)
    {
        alert('Provide e-mail');
        return false;
    }

    else if (!form.password.value)
    {
        alert('Provide password');
        return false;
    }

    else if(form.password.value.length < 6)
    {
        alert('Password must be at least 6 characters');
        return false;
    }
    
    else if (!form.confirmation.value)
    {
        alert('Password not confirmed');
        return false;
    }

    else if (form.password.value != form.confirmation.value)
    {
        alert('Confirmation doesn\'t match')
    }

    return true;
}