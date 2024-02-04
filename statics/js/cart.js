// addToCart.js

document.addEventListener("DOMContentLoaded", function() {
    const addToCartBtns = document.querySelectorAll("[data-product-id]");

    addToCartBtns.forEach(function(btn) {
        btn.addEventListener("click", function() {
            const productId = btn.dataset.productId;

            // Get the form data
            const formData = new FormData();
            formData.append("quantity", 1);

            // Fetch API to submit the form data asynchronously
            fetch(`/cart/add-to-cart/${productId}/`, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}", // Include the CSRF token
                },
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response, you can update the UI or show a message
                console.log(data);
                alert("محصول به سبد خرید افزوده شد!");
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });
});
