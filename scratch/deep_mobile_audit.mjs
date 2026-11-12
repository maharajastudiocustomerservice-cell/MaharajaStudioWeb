import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';
const htmlFiles = fs.readdirSync(rootDir).filter(f => f.endsWith('.html'));

const viewports = [
    { name: '360x740 (Small Android)', width: 360, height: 740 },
    { name: '375x667 (iPhone SE)', width: 375, height: 667 },
    { name: '390x844 (iPhone 14)', width: 390, height: 844 },
    { name: '412x915 (Pixel 7)', width: 412, height: 915 },
    { name: '768x1024 (iPad Portrait)', width: 768, height: 1024 },
    { name: '820x1180 (iPad Air)', width: 820, height: 1180 }
];

async function deepAudit() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();

    const results = [];

    for (const file of htmlFiles) {
        const filePath = path.join(rootDir, file);
        const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');

        for (const vp of viewports) {
            await page.setViewportSize({ width: vp.width, height: vp.height });
            await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });
            await page.waitForTimeout(100);

            const pageIssues = await page.evaluate((vpWidth) => {
                const issues = [];
                const docEl = document.documentElement;

                // 1. Horizontal scroll check
                if (docEl.scrollWidth > docEl.clientWidth + 1) {
                    const diff = docEl.scrollWidth - docEl.clientWidth;
                    // Find elements causing overflow
                    const overflowers = [];
                    const allEls = document.querySelectorAll('body *');
                    for (const el of allEls) {
                        const r = el.getBoundingClientRect();
                        if (r.right > vpWidth + 1.5) {
                            const tag = el.tagName.toLowerCase();
                            const cls = el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.') : '';
                            const id = el.id ? '#' + el.id : '';
                            overflowers.push(`${tag}${id}${cls} (w:${Math.round(r.width)}, right:${Math.round(r.right)})`);
                        }
                    }
                    issues.push(`Page horizontal overflow: +${diff}px. Causes: ${overflowers.slice(0, 5).join('; ')}`);
                }

                // 2. Unwrapped pre / code blocks causing container expansion
                const preElements = document.querySelectorAll('pre, pre code');
                for (const pre of preElements) {
                    const r = pre.getBoundingClientRect();
                    if (r.width > vpWidth) {
                        issues.push(`Pre block wider than screen (${Math.round(r.width)}px > ${vpWidth}px)`);
                        break;
                    }
                }

                // 3. Tables wider than container without scroll
                const tables = document.querySelectorAll('table');
                for (const t of tables) {
                    const parent = t.parentElement;
                    const tRect = t.getBoundingClientRect();
                    const pRect = parent.getBoundingClientRect();
                    const pOverflow = window.getComputedStyle(parent).overflowX;
                    if (tRect.width > pRect.width + 2 && !['auto', 'scroll'].includes(pOverflow)) {
                        issues.push(`Table overflowing parent without scroll wrapper (table ${Math.round(tRect.width)}px > parent ${Math.round(pRect.width)}px)`);
                    }
                }

                // 4. Mobile menu button check on pages with site-nav
                const siteNav = document.querySelector('.site-nav');
                if (siteNav && vpWidth <= 840) {
                    const menuBtn = document.querySelector('[data-mobile-menu-toggle]');
                    if (!menuBtn) {
                        issues.push('site-nav present but missing mobile menu toggle button');
                    } else {
                        const btnStyle = window.getComputedStyle(menuBtn);
                        if (btnStyle.display === 'none') {
                            issues.push('mobile-menu-btn is display:none on mobile');
                        }
                    }
                }

                return issues;
            }, vp.width);

            if (pageIssues.length > 0) {
                results.push({
                    file,
                    viewport: vp.name,
                    issues: pageIssues
                });
            }
        }
    }

    console.log(`\nAudit completed across ${htmlFiles.length} pages.`);
    if (results.length === 0) {
        console.log('No layout issues detected across viewports!');
    } else {
        console.log(`Found ${results.length} page/viewport issues:`);
        for (const r of results) {
            console.log(`\n[${r.file}] @ ${r.viewport}:`);
            r.issues.forEach(i => console.log('  *', i));
        }
    }

    await browser.close();
}

deepAudit().catch(console.error);

