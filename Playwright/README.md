# Playwright Testing Framework

A modern, comprehensive testing framework built with Playwright and JavaScript for cross-browser web application testing, with integrated Allure Reports.

## Features

✅ **Cross-Browser Testing**: Support for Chromium, Firefox, and WebKit
✅ **Mobile Testing**: Device emulation for mobile viewports
✅ **JavaScript Support**: Pure JavaScript configuration
✅ **API Testing**: Built-in API request testing
✅ **Screenshot & Video**: Automatic screenshot and video capture on failures
✅ **Dual Reports**: HTML test reports + Allure detailed reports
✅ **Debug Mode**: Interactive debugging with `--debug` flag
✅ **UI Mode**: Visual test runner with UI mode
✅ **Allure Integration**: Advanced test reporting with Allure Reports

## Project Structure

```
.
├── tests/
│   ├── example.spec.js       # Example UI tests
│   ├── api.spec.js           # API testing examples
│   └── fixtures.js           # Custom test fixtures
├── playwright.config.js      # Playwright configuration
├── allure.config.js          # Allure reporter configuration
├── package.json              # Project dependencies
└── README.md                 # This file
```

## Prerequisites

- Node.js 16+ 
- npm or yarn

## Installation

```bash
# Install dependencies
npm install

# This will also install Playwright browsers automatically
```

## Running Tests

### Run all tests
```bash
npm test
```

### Run tests in headed mode (visible browser)
```bash
npm run test:headed
```

### Run tests in debug mode
```bash
npm run test:debug
```

### Run tests with UI Mode
```bash
npm run test:ui
```

### Run tests for specific browser
```bash
npm run test:chrome      # Chromium only
npm run test:firefox     # Firefox only
npm run test:webkit      # WebKit only
```

### Generate test code
```bash
npm run codegen
```

### View test report
```bash
npm run report
```

### Generate Allure report
```bash
npm run allure:report
```

### Open Allure report
```bash
npm run allure:open
```

## Test Organization

### Example Test File Structure

```javascript
const { test, expect } = require('@playwright/test');

test.describe('Feature Name', () => {
  test.beforeEach(async ({ page }) => {
    // Setup before each test
    await page.goto('https://example.com');
  });

  test('should perform action', async ({ page }) => {
    // Test implementation
    await expect(page).toHaveTitle('Expected Title');
  });
});
```

## Configuration Details

### Browser Environments
- Desktop Chrome
- Desktop Firefox
- Desktop Safari
- Mobile Chrome (Pixel 5)
- Mobile Safari (iPhone 12)

### Test Options
- Parallel execution enabled
- Screenshots on failure
- Video recording on failure
- Trace collection on retry
- Auto-retry enabled for CI

## Debugging

### Debug Mode
```bash
npm run test:debug
```
This opens the Playwright Inspector with step-by-step execution.

### UI Mode (Recommended)
```bash
npm run test:ui
```
Visual test runner with replay functionality.

### Trace Viewer
Traces are automatically collected and can be viewed with:
```bash
npx playwright show-trace <trace-file>
```

## Writing Tests

### Basic Test Example
```javascript
const { test, expect } = require('@playwright/test');

test('login successfully', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.fill('input[name="username"]', 'user');
  await page.fill('input[name="password"]', 'pass');
  await page.click('button:has-text("Login")');
  await expect(page).toHaveURL('https://example.com/dashboard');
});
```

### Using Fixtures
Create reusable test setup with custom fixtures in `tests/fixtures.js`:
```javascript
const { test: base, expect } = require('@playwright/test');

const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // Setup authenticated state
    await use(page);
  },
});

module.exports = { test, expect };
```

### Allure Annotations
Add Allure test details to enhance reports:
```javascript
const { test, expect } = require('@playwright/test');

test('login functionality', async ({ page }) => {
  test.info().annotations.push({
    type: 'feature',
    description: 'Authentication',
  });
  
  test.info().annotations.push({
    type: 'severity',
    description: 'critical',
  });
  
  // Test code here
});
```

## Allure Reports

Allure Reports provide detailed, interactive test reports with history, trends, and analytics.

### Generate Report
After running tests, generate the Allure report:
```bash
npm run allure:report
```

### View Report
Open the Allure report in your browser:
```bash
npm run allure:open
```

### Report Features
- **Test Details**: Step-by-step test execution with attachments
- **History**: Track test results over time
- **Trends**: Visualize test stability
- **Timeline**: See test execution timeline
- **Retries**: View original and retry attempts
- **Attachments**: Screenshots, videos, and logs

### Test Results Location
- **Raw Results**: `allure-results/` (automatically generated)
- **HTML Report**: `allure-report/` (generated by `npm run allure:report`)

## CI/CD Integration

Tests are configured for CI environments with:
- 2 retries on failure
- Sequential execution (1 worker)
- Failure screenshots and videos
- HTML and Allure reports

To use in GitHub Actions:
```yaml
- name: Run Playwright tests
  run: npm test

- name: Generate Allure report
  if: always()
  run: npm run allure:report

- name: Upload Allure results
  if: always()
  uses: actions/upload-artifact@v3
  with:
    name: allure-report
    path: allure-report
```

## Useful Resources

- [Playwright Documentation](https://playwright.dev)
- [Playwright API Reference](https://playwright.dev/docs/api/class-playwright)
- [Best Practices](https://playwright.dev/docs/best-practices)
- [Debugging Guide](https://playwright.dev/docs/debug)

## Troubleshooting

### Browser not found
```bash
npx playwright install
```

### Timeout issues
Adjust in `playwright.config.ts`:
```typescript
use: {
  navigationTimeout: 30000,
  actionTimeout: 10000,
}
```

### Port conflicts
Update `baseURL` in `playwright.config.ts` if your application runs on a different port.

## License

MIT
