# Functional Test Cases – Demoblaze

| TC ID | Test Case Description | Precondition | Steps | Expected Result |
|------|------------------------|--------------|--------|-----------------|
| TC01 | Verify login modal opens | Homepage loaded | Click “Log in” | Login modal should appear |
| TC02 | Login with valid data | User account exists | Enter username & password → Login | Username displayed on top |
| TC03 | Login with invalid data | None | Enter wrong creds → Login | Error message displayed |
| TC04 | View category products | Homepage loaded | Click Phones category | Phones list displayed |
| TC05 | Product details view | Category page loaded | Click a product | Product detail page opens |
| TC06 | Add product to cart | On product detail page | Click “Add to cart” | Alert appears “Product added” |
| TC07 | Remove product from cart | Product added | Navigate to cart → Delete | Item removed |
| TC08 | Place order | Cart has item | Click “Place order” → Fill fields → Purchase | Confirmation modal appears |
| TC09 | Place order empty fields | Cart has item | Click “Place order” → Submit empty | Error or validation behavior |
| TC10 | Logout | Logged in | Click “Log out” | User successfully logged out |
