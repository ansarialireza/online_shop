// document.addEventListener('DOMContentLoaded', function () {
//     // گوش دادن به تغییرات در انتخاب‌ها
//     const corniceTypeCheckboxes = document.querySelectorAll('.cornice-type-checkbox');
//     corniceTypeCheckboxes.forEach(function (checkbox) {
//       checkbox.addEventListener('change', updateFinalPrice);
//     });
  
//     // تابع بروزرسانی قیمت نهایی
//     function updateFinalPrice() {
//       let totalPrice = 0;
  
//       corniceTypeCheckboxes.forEach(function (checkbox) {
//         if (checkbox.checked) {
//           const container = checkbox.closest('.cornice-type-container');
//           const quantity = container.querySelector('.cornice-quantity').value;
//           const priceWholesale = container.dataset.priceWholesale;
//           const priceRetail = container.dataset.priceRetail;
  
//           // اعمال قیمت بر اساس نوع کاربر
//           const price = (userIsAuthenticated && userIsWholesale) ? priceWholesale : priceRetail;
  
//           // محاسبه قیمت نهایی
//           totalPrice += quantity * price;
//         }
//       });
  
//       // نمایش قیمت نهایی
//       const finalPriceElement = document.getElementById('finalPrice');
//       finalPriceElement.innerHTML = 'قیمت نهایی: <span class="text-primary text-2xl md:text-sm font-bold">' + totalPrice.toLocaleString() + ' تومان</span>';
//     }
//   });
  