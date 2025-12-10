import { Page } from '@playwright/test'

// Get the URL 
// Select (click) on a product

export class homePage{
    private page : Page

    constructor(page:Page){
        this.page = page
    }

    async gotopage(){
        await this.page.goto('https://demoblaze.com/')
    }

    async selectProduct(productName : string){
        await this.page.click(`text= ${productName}`)
    }
}