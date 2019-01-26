let button = document.getElementById('button');
button.onclick = function(){
    window.open('edit_profile');
}

let my_trips_driver=document.getElementById('driver');
my_trips_driver.onclick = function(){
    my_trips_driver.parentNode.removeChild(my_trips_driver);
    return false;
}