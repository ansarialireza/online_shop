// script.js

document.addEventListener('DOMContentLoaded', function () {
    const fileInputs = document.querySelectorAll('.fileUpload');

    fileInputs.forEach(function (fileInput) {
        fileInput.addEventListener('change', function () {
            const containerId = fileInput.getAttribute('data-id');
            const imageContainer = document.getElementById('imageContainer-' + containerId);

            if (fileInput.files.length > 0) {
                const reader = new FileReader();

                reader.onload = function (e) {
                    imageContainer.innerHTML = `<img src="${e.target.result}" alt="تصویر پیش‌نمایش">`;
                    imageContainer.classList.remove('hidden');
                };

                reader.readAsDataURL(fileInput.files[0]);
            } else {
                imageContainer.innerHTML = '';
                imageContainer.classList.add('hidden');
            }
        });
    });
});
