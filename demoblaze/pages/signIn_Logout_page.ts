import { Page } from '@playwright/test'

export class SignIN{
    private page : Page

    constructor(page:Page){
        this.page = page
    }

    async signin(username: string,password: string) : Promise<void>{
        await this.page.locator("#sign-username").fill(username)
        await this.page.locator('#sign-password').fill(password)
        await this.page.locator("//button[text()='Sign up']").click()
    }

    async login(username: string,password: string) : Promise<void>{
        // let dialogError = false;

        // // Capture dialog
        // this.page.once('dialog', dialog => {
        //     console.log(`Dialog message: ${dialog.message()}`);
        //     dialog.dismiss().catch(() => { });
        //     dialogError = true;
       // });

        await this.page.locator("#loginusername").fill(username)
        await this.page.locator('#loginpassword').fill(password)
        await this.page.locator("//button[text()='Log in']").click()
        //await this.page.waitForTimeout(500);
    }
    //     if (await this.page.isVisible('#nameofuser')) {
    //         return "Welcome testUserss";
    //     }
    //     if (dialogError) {
    //         return "Please fill out Username and Password.";
    //     }
    //     if (dialogError) {
    //         return "User does not exist.";
    //     }
    //     if (dialogError) {
    //         return "Wrong password";
    //     }
    //     // fallback
    //     return "unknown";
    // }

}