function gioClicked(){
    document.body.style.backgroundColor = "red";

    const color1 = "red"
    const color2 = "green"

    const image = document.getElementsByClassName("my-img")[0]

    img.style.display = "none"
    if (document.body.backgroundColor==color1){
        document.body.backgroundColor = color2;
    } else {
        document.body.style.backgroundColor = color1;
    }
}