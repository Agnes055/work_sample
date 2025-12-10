import { Page } from '@playwright/test'

//add product to cart
//check (accept) the product popup
// go back home


export class addProduct{
    private page: Page

    constructor(page:Page){
        this.page = page
    }

    async addProductpage(){
        await this.page.click('text=Add to cart')
        await this.page.once('dialog', dialog => {
        console.log(`Dialog message: ${dialog.message()}`);
        dialog.dismiss().catch(() => {});
        });
        //await this.page.waitForEvent('dialog')
        //await this.page.once('dialog', dialog => dialog.accept())
    }
    async backHome(){
        await this.page.click('text=home')
    }
}
