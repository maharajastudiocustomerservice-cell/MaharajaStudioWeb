import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function audit() {
    console.log('--- Starting Comprehensive Site & Docs Audit ---');
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

    const htmlFiles = fs.readdirSync(rootDir).filter(f => f.endsWith('.html'));

    const issues = [];

    for (const file of htmlFiles) {
        const filePath = path.join(rootDir, file);
        const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');

        page.on('console', msg => {
            const t = msg.text();
            if (msg.type() === 'error' && !t.includes('ERR_NAME_NOT_RESOLVED') && !t.includes('fonts.googleapis.com')) {
                issues.push(`[${file}] Console error: ${t}`);
            }
        });

        await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });
        await page.waitForTimeout(100);

        // Check internal same-page hash links
        const badHashLinks = await page.evaluate(() => {
            const links = Array.from(document.querySelectorAll('a[href^="#"]'));
            const bad = [];
            for (const a of links) {
                const hash = a.getAttribute('href');
                if (hash === '#' || hash === '') continue;
                try {
                    const targetId = decodeURIComponent(hash.slice(1));
                    const target = document.getElementById(targetId) || 
                                   document.querySelector(`[name="${CSS.escape(targetId)}"]`) ||
                                   document.getElementById(CSS.escape(targetId));
                    if (!target) {
                        bad.push(hash);
                    }
                } catch (e) {
                    bad.push(hash);
                }
            }
            return Array.from(new Set(bad));
        });

        if (badHashLinks.length > 0) {
            issues.push(`[${file}] Broken same-page anchors: ${badHashLinks.join(', ')}`);
        }

        // Check for looping category links in directory tables
        const loopingLinks = await page.evaluate(() => {
            const tables = Array.from(document.querySelectorAll('.studio-table, table'));
            const bad = [];
            for (const t of tables) {
                const rows = Array.from(t.querySelectorAll('tbody tr'));
                for (const row of rows) {
                    const firstLink = row.querySelector('td:first-child a');
                    if (firstLink) {
                        const href = firstLink.getAttribute('href') || '';
                        if (href.startsWith('#cat-')) {
                            bad.push(`${firstLink.textContent.trim()} -> ${href}`);
                        }
                    }
                }
            }
            return bad;
        });

        if (loopingLinks.length > 0) {
            issues.push(`[${file}] Category looping links in table: ${loopingLinks.join(', ')}`);
        }
    }

    console.log(`Audited ${htmlFiles.length} pages.`);
    if (issues.length === 0) {
        console.log('SUCCESS: Zero broken hash anchors and zero category looping links across all 28 HTML pages!');
    } else {
        console.log('ISSUES FOUND:');
        issues.forEach(i => console.log('  -', i));
    }

    await browser.close();
}

audit().catch(console.error);
