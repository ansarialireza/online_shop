// script.js
document.addEventListener('DOMContentLoaded', function () {
    openModal();
});

function openModal() {
    document.getElementById('myModal').style.display = 'block';
    document.getElementById('modalOverlay').style.display = 'block';

    setTimeout(function () {
        closeModal();
    }, 3000);
}

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
    document.getElementById('modalOverlay').style.display = 'none';
}
