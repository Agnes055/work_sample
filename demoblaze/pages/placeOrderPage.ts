import { Page } from "@playwright/test";

export class OrderPlacement{
    private page : Page

    constructor(page:Page){
        this.page = page
    }
    async check(
        names:string,
        country:string,
        city:string,
        credit:string,
        month:string,
        year:string,
       ) : Promise<void>{
        await this.page.getByRole('button', { name: 'Place Order' }).click();
        await this.page.getByRole('textbox', { name: 'Total: 1150 Name:' }).fill(names)
        await this.page.getByRole('textbox', { name: 'Country:' }).fill(country);
        await this.page.getByRole('textbox', { name: 'City:' }).fill(city);
        await this.page.getByRole('textbox', { name: 'Credit card:' }).fill(credit);
        await this.page.getByRole('textbox', { name: 'Month:' }).fill(month);
        await this.page.getByRole('textbox', { name: 'Year:' }).fill(year);
        await this.page.click('button[onclick="purchaseOrder()"]');
        await this.page.waitForSelector('.sweet-alert');
        // this.page.once('dialog', dialog => {
        //     console.log(`Dialog message: ${dialog.message()}`);
        //     dialog.dismiss().catch(() => { });
        // });
    }
}