function dropdownText(i){
    var text = document.getElementsByClassName("text");
    for (let index = 0; index < text.length; index++) {
        if(text[index].style.display != "none"){
            text[index].style.display = "none";
        }
        
    }
    if(text[i-1].style.display = "none"){
        text[i-1].style.display = "block";
    }    
}