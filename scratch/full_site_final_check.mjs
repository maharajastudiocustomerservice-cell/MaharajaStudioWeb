import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';
const htmlFiles = fs.readdirSync(rootDir).filter(f => f.endsWith('.html'));

const viewports = [
    { name: 'Android Small', width: 360, height: 740 },
    { name: 'iPhone SE', width: 375, height: 667 },
    { name: 'iPhone 14', width: 390, height: 844 },
    { name: 'Pixel 7', width: 412, height: 915 },
    { name: 'Mobile Landscape', width: 844, height: 390 },
    { name: 'iPad Portrait', width: 768, height: 1024 },
    { name: 'iPad Air', width: 820, height: 1180 },
    { name: 'Desktop Standard', width: 1440, height: 900 }
];

async function finalAudit() {
    const browser = await chromium.launch({ headless: true });
    let totalScans = 0;
    const failures = [];

    for (const file of htmlFiles) {
        const fileUrl = 'file:///' + path.join(rootDir, file).replace(/\\/g, '/');

        for (const vp of viewports) {
            totalScans++;
            const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
            await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });
            await page.waitForTimeout(40);

            const hasOverflow = await page.evaluate(() => {
                const doc = document.documentElement;
                return doc.scrollWidth > doc.clientWidth + 1;
            });

            if (hasOverflow) {
                const diff = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
                failures.push(`[${file}] on ${vp.name} (${vp.width}x${vp.height}): +${diff}px overflow`);
            }

            await page.close();
        }
    }

    console.log(`Audited ${htmlFiles.length} HTML files across ${viewports.length} viewports (Total scans: ${totalScans})`);
    if (failures.length === 0) {
        console.log(`PERFECT: ALL ${totalScans} SCANS PASSED WITH ZERO HORIZONTAL OVERFLOW!`);
    } else {
        console.log(`Found ${failures.length} issues:`);
        failures.forEach(f => console.log('  -', f));
    }

    await browser.close();
}

finalAudit().catch(console.error);

