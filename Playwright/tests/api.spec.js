const { test, expect } = require('@playwright/test');

test.describe('API Tests', () => {
  test('should fetch data successfully', async ({ request }) => {
    const response = await request.get('https://api.github.com/repos/microsoft/playwright');
    expect(response.status()).toBe(200);
    const json = await response.json();
    expect(json).toHaveProperty('name', 'playwright');
  });

  test('should handle POST request', async ({ request }) => {
    const response = await request.post('https://httpbin.org/post', {
      data: { name: 'test', value: 123 },
    });
    expect(response.status()).toBe(200);
    const json = await response.json();
    expect(json).toHaveProperty('data');
  });
});
