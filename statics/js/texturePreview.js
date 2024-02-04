// document.addEventListener('DOMContentLoaded', function () {
//     const chooseTextureDivs = document.querySelectorAll('.chooseTexture');
//     const texturePreview = document.getElementById('texturePreview');
//     const textureInput = document.getElementById('textureInput');
  
//     chooseTextureDivs.forEach(chooseTextureDiv => {
//       chooseTextureDiv.addEventListener('click', function () {
//         const textureImage = this.querySelector('img');
//         const textureCode = textureImage.dataset.id; // تغییر در اینجا
  
//         // Update the texturePreview
//         texturePreview.src = textureImage.src;
//         texturePreview.alt = textureCode;
  
//         // Update any hidden input field with the selected texture code
//         textureInput.value = textureCode;
//       });
//     });
//   });
  

  document.addEventListener('DOMContentLoaded', function () {
    const chooseTextureDivs = document.querySelectorAll('.chooseTexture');
    const texturePreview = document.getElementById('texturePreview');
    const textureInput = document.getElementById('textureInput');

    chooseTextureDivs.forEach(chooseTextureDiv => {
        chooseTextureDiv.addEventListener('click', function () {
            const textureImage = this.querySelector('img');
            const textureCode = textureImage.dataset.id;

            // Update the texturePreview
            texturePreview.src = textureImage.src;
            texturePreview.alt = textureCode;

            // Update the hidden input field with the selected texture code
            textureInput.value = textureCode;
        });
    });
});


