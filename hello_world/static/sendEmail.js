function sendEmail() {
    var name=document.getElementById("name").value
    var subject=document.getElementById("subject").value
    var message=document.getElementById("message").value
    mailtoLink = "mailto:thenmelody@gmail.com?subject=" + subject + "&body=" + message
    //alert(name + email + message)
    window.location.href = mailtoLink

    };
function verification(){
    location.reload()
}