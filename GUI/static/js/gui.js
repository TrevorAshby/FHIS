//const input = document.getElementById("input");
//const output = document.querySelector("output");
let imagesArray = [];



function displayImages() {
    var output = document.getElementById("output")
    let images = ""
    imagesArray.forEach((image, index) => {
        images += `<div class="image">
        <img src="${URL.createObjectURL(image)}" alt="image">
        <span onclick="deleteImage(${index})">&times;</span>
        </div>`
    });
    output.innerHTML = images
}

function deleteImage(index) {
    imagesArray.splice(index, 1)
    displayImages()
  }



function importFile() {
    
    // var input = document.getElementById('input');

    // input.addEventListener("change", () => {
    //     const file = input.files
    //     imagesArray.push(file[0]);
    //     displayImages();
    // });

    input.onchange = e => {
        var file = e.target.files[0];

        imagesArray.push(file);
        displayImages();
        //console.log(file);
    }
}