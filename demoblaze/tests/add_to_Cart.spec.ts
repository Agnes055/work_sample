import { test, expect } from '@playwright/test';
import { CartPage } from '../pages/cartPage';
import { homePage } from '../pages/homePage';
import { OrderPlacement } from '../pages/placeOrderPage';
import { placeorder } from '../utils_data/test_data';
import { addProduct } from '../pages/productpage';

// Tests 
// •	Add items to cart
// •	Verify product Price calculation
// •	Checkout page navigation

// test.use({
//   viewport: { width: 360, height: 740 },
// });

test('Add item to cart and validate', async ({ page }) => {
    const home = new homePage(page);
    await home.gotopage();   // Correct stable navigation
    await home.selectProduct('Samsung galaxy s6');
    // Add product ot cart
    const product = new addProduct(page);
    await product.addProductpage();
    await product.backHome();

    await home.selectProduct('Iphone 6 32gb');
    await product.addProductpage();
    await product.backHome();
    const cart = new CartPage(page);
    await cart.goToCart();
    //await page.pause()
    // Verify products in cart
    await cart.verifyItemsInCart([
      { name: 'Samsung galaxy s6', price: 360 },
      { name: 'Iphone 6 32gb', price: 790 }
    ])
    await cart.verifyTotal(1150);
    await cart.verifyCheckoutButton();
    //await page.pause()
    // Proceed to checkout
    for (const order of placeorder) {
      const checkouts = new OrderPlacement(page)
      await checkouts.check(order.name, order.city, order.country, order.card, order.month, order.year);

      await expect(page.locator(".confirm")).toBeVisible();
    }

});