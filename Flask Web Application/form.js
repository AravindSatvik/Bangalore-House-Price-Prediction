formid=document.getElementById('formid')
formid.addEventListener('submit',func);
function func(event){
    var locationid=document.getElementById('location');
    if (locationid.value=='--Select Location--'){
        alert("Please Select a Location");
        event.preventDefault();
    }
}
