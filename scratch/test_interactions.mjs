import { createRequire } from 'module';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';
const screenshotsDir = path.join(rootDir, 'scratch', 'screenshots');

async function testMobileInteractions() {
    const browser = await chromium.launch({ headless: true });
    // Test iPhone 14
    const page = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });

    const testPages = ['index.html', 'object-finder-pro.html', 'msultimate.html', 'contact.html', 'support.html'];

    for (const p of testPages) {
        await page.goto('file:///' + path.join(rootDir, p).replace(/\\/g, '/'));
        await page.waitForTimeout(100);

        // Screenshot top at 390px
        await page.screenshot({ path: path.join(screenshotsDir, `after_${p.replace('.html', '')}_top.png`), clip: { x: 0, y: 0, width: 390, height: 844 } });

        // Scroll down 400px
        await page.evaluate(() => window.scrollTo(0, 400));
        await page.waitForTimeout(100);

        // Click mobile menu toggle while scrolled down!
        const toggleBtn = await page.$('[data-mobile-menu-toggle]');
        if (toggleBtn) {
            await toggleBtn.click();
            await page.waitForTimeout(250);

            // Screenshot the menu open while scrolled!
            await page.screenshot({ path: path.join(screenshotsDir, `after_${p.replace('.html', '')}_menu_scrolled.png`), clip: { x: 0, y: 0, width: 390, height: 844 } });

            // Close menu
            await toggleBtn.click();
            await page.waitForTimeout(150);
        }
    }

    console.log('Mobile interaction test screenshots generated successfully.');
    await browser.close();
}

testMobileInteractions().catch(console.error);

