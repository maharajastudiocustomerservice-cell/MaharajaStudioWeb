import { createRequire } from 'module';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

const viewports = [
    { name: 'Android Small', width: 360, height: 740 },
    { name: 'iPhone SE', width: 375, height: 667 },
    { name: 'iPhone 14', width: 390, height: 844 },
    { name: 'Pixel 7', width: 412, height: 915 },
    { name: 'Mobile Landscape', width: 844, height: 390 },
    { name: 'iPad Portrait', width: 768, height: 1024 },
    { name: 'iPad Air', width: 820, height: 1180 },
    { name: 'iPad Landscape', width: 1024, height: 768 },
    { name: 'Desktop Standard', width: 1440, height: 900 }
];

const pages = [
    'index.html',
    'object-finder-pro.html',
    'msultimate.html',
    'ms-motion.html',
    'scriptable-studio-pro.html',
    'tactical-cover-retreat-ai-system.html',
    'ultimate-quick-inspector.html',
    'documentation.html',
    'msultimate-docs.html',
    'contact.html',
    'support.html',
    'legal.html'
];

async function runCheck() {
    const browser = await chromium.launch({ headless: true });
    let totalChecks = 0;
    let failedChecks = 0;

    for (const pageName of pages) {
        const fileUrl = 'file:///' + path.join(rootDir, pageName).replace(/\\/g, '/');

        for (const vp of viewports) {
            totalChecks++;
            const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
            await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });
            await page.waitForTimeout(60);

            const result = await page.evaluate((vpWidth) => {
                const scrollW = document.documentElement.scrollWidth;
                const clientW = document.documentElement.clientWidth;
                return {
                    overflow: scrollW > clientW,
                    diff: scrollW - clientW
                };
            }, vp.width);

            if (result.overflow) {
                failedChecks++;
                console.log(`FAIL: ${pageName} on ${vp.name} (${vp.width}x${vp.height}): +${result.diff}px overflow`);
            }

            await page.close();
        }
    }

    console.log(`\nChecked ${totalChecks} combinations (${pages.length} pages across ${viewports.length} viewports).`);
    if (failedChecks === 0) {
        console.log('ALL 108 VIEWPORT/PAGE TESTS PASSED WITH ZERO HORIZONTAL OVERFLOW!');
    } else {
        console.log(`${failedChecks} failed checks.`);
    }

    await browser.close();
}

runCheck().catch(console.error);

