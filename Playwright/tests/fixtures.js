const { test: base, expect } = require("@playwright/test");

const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // You can add authentication logic here
    // Example: await page.goto('/login'); await page.fill(...); await page.click(...);
    await use(page);
  },
});

module.exports = { test, expect };
