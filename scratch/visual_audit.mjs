import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';
const screenshotsDir = path.join(rootDir, 'scratch', 'screenshots');

async function testMobileExperience() {
    const browser = await chromium.launch({ headless: true });
    // Test iPhone 14 (390 x 844) and Android small (360 x 740)
    const context = await browser.newContext({
        viewport: { width: 390, height: 844 },
        deviceScaleFactor: 2
    });
    const page = await context.newPage();

    const testPages = [
        'index.html',
        'object-finder-pro.html',
        'msultimate.html',
        'ms-motion.html',
        'scriptable-studio-pro.html',
        'tactical-cover-retreat-ai-system.html',
        'documentation.html',
        'msultimate-docs.html'
    ];

    for (const pageName of testPages) {
        const filePath = path.join(rootDir, pageName);
        const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');

        await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });
        await page.waitForTimeout(300);

        // Screenshot full hero and top section
        await page.screenshot({
            path: path.join(screenshotsDir, `detail_${pageName.replace('.html', '')}_top.png`),
            clip: { x: 0, y: 0, width: 390, height: 844 }
        });

        // Test mobile menu click
        const menuBtn = await page.$('[data-mobile-menu-toggle]');
        if (menuBtn) {
            await menuBtn.click();
            await page.waitForTimeout(200);
            await page.screenshot({
                path: path.join(screenshotsDir, `detail_${pageName.replace('.html', '')}_menu_open.png`),
                clip: { x: 0, y: 0, width: 390, height: 600 }
            });
            // Click again to close
            await menuBtn.click();
            await page.waitForTimeout(100);
        }

        // Check if there are scrollable elements or overflow
        const layoutMetrics = await page.evaluate(() => {
            const results = {};
            const heroTitle = document.querySelector('.hero h1');
            if (heroTitle) {
                const style = window.getComputedStyle(heroTitle);
                results.heroTitleFontSize = style.fontSize;
                results.heroTitleLineHeight = style.lineHeight;
            }
            const workbench = document.querySelector('.workbench-frame');
            if (workbench) {
                const rect = workbench.getBoundingClientRect();
                results.workbenchWidth = rect.width;
            }
            const tabs = document.querySelectorAll('.workbench-tab');
            results.tabCount = tabs.length;

            const siteNav = document.querySelector('.site-nav');
            if (siteNav) {
                results.navHeight = siteNav.getBoundingClientRect().height;
            }

            const mobileDrawer = document.querySelector('.mobile-drawer');
            if (mobileDrawer) {
                const s = window.getComputedStyle(mobileDrawer);
                results.drawerPosition = s.position;
                results.drawerZIndex = s.zIndex;
            }

            return results;
        });

        console.log(`Page: ${pageName}`, layoutMetrics);
    }

    await browser.close();
}

testMobileExperience().catch(console.error);

