import { Page, expect } from '@playwright/test';


export class CartPage {
  constructor(private page: Page) {}

  async goToCart() {
    await this.page.click('#cartur');
  }
  async verifyItemsInCart(expectedItems: { name: string; price: number }[]) {
    await this.page.waitForSelector('#tbodyid > tr');  // Ensure cart table has loaded
    const rows = this.page.locator('#tbodyid > tr');
    const count = await rows.count();

    for (const expectedItem of expectedItems) {
      let found = false;

      for (let i = 0; i < count; i++) {
        const row = rows.nth(i);
        const text = (await row.textContent())?.trim();
        console.log(`Row ${i}:`, text);  // Optional debug

        if (text?.toLowerCase().includes(expectedItem.name.toLowerCase()) &&
          text.includes(expectedItem.price.toString())) {
          found = true;
          break;
        }
      }

      expect(found).toBeTruthy();  // Fails if item not found in any row
    }
  }

  async verifyTotal(expectedTotal: number) {
    const total = await this.page.locator('#totalp').textContent();
    expect(Number(total)).toBe(expectedTotal);
  }

  async verifyCheckoutButton() {
    await expect(this.page.locator('//*[@id="page-wrapper"]/div/div[2]/button')).toBeVisible();
  }
}
