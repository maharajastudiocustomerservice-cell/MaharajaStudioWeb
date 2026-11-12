import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';
const screenshotsDir = path.join(rootDir, 'scratch', 'screenshots');
if (!fs.existsSync(screenshotsDir)) {
    fs.mkdirSync(screenshotsDir, { recursive: true });
}

const viewports = [
    { name: 'android-small', width: 360, height: 740 },
    { name: 'iphone-se', width: 375, height: 667 },
    { name: 'iphone-14', width: 390, height: 844 },
    { name: 'pixel-7', width: 412, height: 915 },
    { name: 'ipad-portrait', width: 768, height: 1024 },
    { name: 'tablet-landscape', width: 1024, height: 768 }
];

const keyPages = [
    'index.html',
    'msultimate.html',
    'ms-motion.html',
    'scriptable-studio-pro.html',
    'object-finder-pro.html',
    'tactical-cover-retreat-ai-system.html',
    'ultimate-quick-inspector.html',
    'documentation.html',
    'msultimate-docs.html',
    'contact.html',
    'legal.html'
];

async function runAudit() {
    console.log('--- Launching Mobile Audit ---');
    const browser = await chromium.launch({ headless: true });
    const overflowReport = [];

    for (const pageName of keyPages) {
        const filePath = path.join(rootDir, pageName);
        if (!fs.existsSync(filePath)) continue;
        const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');

        for (const vp of viewports) {
            const context = await browser.newContext({
                viewport: { width: vp.width, height: vp.height },
                deviceScaleFactor: 2
            });
            const page = await context.newPage();

            await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });
            await page.waitForTimeout(200);

            // Check for horizontal overflow
            const overflowData = await page.evaluate((vpWidth) => {
                const scrollWidth = document.documentElement.scrollWidth;
                const clientWidth = document.documentElement.clientWidth;
                const hasHScroll = scrollWidth > clientWidth;

                const offendingElements = [];
                if (hasHScroll) {
                    const allEls = document.querySelectorAll('*');
                    for (const el of allEls) {
                        const r = el.getBoundingClientRect();
                        if (r.right > vpWidth + 1) { // 1px tolerance for subpixel
                            // Check if element has an id or class
                            const tag = el.tagName.toLowerCase();
                            const cls = el.className ? `.${Array.from(el.classList).join('.')}` : '';
                            const id = el.id ? `#${el.id}` : '';
                            offendingElements.push({
                                selector: `${tag}${id}${cls}`,
                                right: Math.round(r.right),
                                width: Math.round(r.width),
                                overflowX: Math.round(r.right - vpWidth)
                            });
                        }
                    }
                }
                return {
                    scrollWidth,
                    clientWidth,
                    hasHScroll,
                    offendingElements: offendingElements.slice(0, 10) // top 10
                };
            }, vp.width);

            if (overflowData.hasHScroll) {
                overflowReport.push({
                    page: pageName,
                    viewport: `${vp.name} (${vp.width}x${vp.height})`,
                    scrollWidth: overflowData.scrollWidth,
                    clientWidth: overflowData.clientWidth,
                    offenders: overflowData.offendingElements
                });
            }

            // Save screenshots for iPhone 14
            if (vp.name === 'iphone-14') {
                const ssPath = path.join(screenshotsDir, `${pageName.replace('.html', '')}_mobile.png`);
                await page.screenshot({ path: ssPath, fullPage: false });
            }

            await context.close();
        }
    }

    console.log(`\nAudit completed across ${keyPages.length} pages and ${viewports.length} viewports.`);
    if (overflowReport.length === 0) {
        console.log('No horizontal overflow detected on key pages!');
    } else {
        console.log(`Found ${overflowReport.length} viewport/page combinations with horizontal overflow:`);
        for (const item of overflowReport) {
            console.log(`\nPage: ${item.page} at ${item.viewport}`);
            console.log(`  scrollWidth: ${item.scrollWidth}, clientWidth: ${item.clientWidth}`);
            console.log(`  Top offending elements:`);
            for (const off of item.offenders) {
                console.log(`    - ${off.selector} (width: ${off.width}px, right: ${off.right}px, overflow: +${off.overflowX}px)`);
            }
        }
    }

    await browser.close();
}

runAudit().catch(console.error);

