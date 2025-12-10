import {test, expect} from '@playwright/test'
import {SignIN} from  "../pages/signIn_Logout_page"
import {logIn, signingIn} from "../utils_data/test_data"
import { homePage } from '../pages/homePage';


test.describe("Verify the login and logout functionality of the blaze site", async () => {
    test.beforeEach("loading the URL", async ({page}) => {
        const url = new homePage(page)
        await url.gotopage()
        //await page.pause()

    })
    test("Verify Sign in", async ({page}) => {
        for(const sign of signingIn){
            await page.getByRole('link', { name: 'Sign up' }).click();
            const signInPage = new SignIN(page)
            await signInPage.signin(sign.userEmail, sign.userPassword)
            //await expect(page.locator('#nameofuser')).toContainText(sign.expectedResult);
            page.once('dialog', dialog => {
                console.log(`Dialog message: ${dialog.message()}`);
                dialog.dismiss().catch(() => { });
            });

        }
        
    })
  
    test("Verify logout", async ({page}) => {
        await page.getByRole('link', { name: 'Log in' }).click();
        for(const log of logIn){
            const loggin = new SignIN(page)
            const result = await loggin.login(log.userEmail, log.userPassword);
            //expect(result).toBe(log.expectedResult);
            page.once('dialog', dialog => {
                console.log(`Dialog message: ${dialog.message()}`);
                dialog.dismiss().catch(() => { });
            })

        }
    
    })
})