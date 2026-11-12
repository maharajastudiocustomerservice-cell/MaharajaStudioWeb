import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function inspectPages() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 375, height: 667 } }); // iPhone SE

    const files = [
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

    for (const f of files) {
        await page.goto('file:///' + path.join(rootDir, f).replace(/\\/g, '/'), { waitUntil: 'domcontentloaded' });
        await page.waitForTimeout(200);

        const analysis = await page.evaluate((fileName) => {
            const problems = [];
            const docW = document.documentElement.clientWidth;

            // 1. Check all elements extending beyond docW
            document.querySelectorAll('*').forEach(el => {
                const r = el.getBoundingClientRect();
                if (r.right > docW + 1) {
                    problems.push(`Overflow: <${el.tagName.toLowerCase()} class="${el.className}"> right:${Math.round(r.right)}px`);
                }
            });

            // 2. Check workbench-tabs wrapping
            const wbTabs = document.querySelector('.workbench-tabs');
            if (wbTabs) {
                const tabEls = Array.from(wbTabs.querySelectorAll('.workbench-tab'));
                const yVals = new Set(tabEls.map(t => Math.round(t.getBoundingClientRect().top)));
                if (yVals.size > 1) {
                    problems.push(`Workbench tabs wrapped into ${yVals.size} rows (tabs: ${tabEls.length})`);
                }
            }

            // 3. Check hero-actions wrapping
            const heroActions = document.querySelector('.hero-actions');
            if (heroActions) {
                const btns = Array.from(heroActions.querySelectorAll('.btn'));
                const yVals = new Set(btns.map(b => Math.round(b.getBoundingClientRect().top)));
                if (yVals.size > 1 && btns.length > 1) {
                    problems.push(`Hero action buttons stacked unevenly (${btns.length} buttons across ${yVals.size} rows)`);
                }
            }

            // 4. Check stats-strip layout
            const stats = document.querySelector('.stats-strip, .stats-strip-6');
            if (stats) {
                const cells = Array.from(stats.querySelectorAll('.stat-cell'));
                const cWidths = cells.map(c => Math.round(c.getBoundingClientRect().width));
                // check if single column or multi column
            }

            // 5. Check cards padding and width
            document.querySelectorAll('.feature-card, .asset-card, .review-card').forEach(card => {
                const r = card.getBoundingClientRect();
                const style = window.getComputedStyle(card);
                const pLeft = parseFloat(style.paddingLeft);
                const pRight = parseFloat(style.paddingRight);
                if (pLeft + pRight > 50 && r.width < 360) {
                    problems.push(`Card ${card.className} excessive horizontal padding (${Math.round(pLeft + pRight)}px on ${Math.round(r.width)}px card)`);
                }
            });

            // 6. Check tables without horizontal scrolling
            document.querySelectorAll('table').forEach(tbl => {
                const p = tbl.parentElement;
                const pStyle = window.getComputedStyle(p);
                const pOverflow = pStyle.overflowX;
                if (tbl.scrollWidth > p.clientWidth && !['auto', 'scroll'].includes(pOverflow)) {
                    problems.push(`Table ${tbl.className || 'table'} overflows parent (${tbl.scrollWidth}px > ${p.clientWidth}px) without overflow-x: auto`);
                }
            });

            // 7. Check mobile drawer usability
            const drawer = document.querySelector('.mobile-drawer');
            if (drawer) {
                const dStyle = window.getComputedStyle(drawer);
                if (dStyle.position !== 'fixed' && dStyle.position !== 'sticky') {
                    problems.push(`Mobile drawer is static (${dStyle.position}) - scrolls away and does not stick under header when scrolled`);
                }
            }

            // 8. Check code blocks
            document.querySelectorAll('pre').forEach(pre => {
                const preStyle = window.getComputedStyle(pre);
                if (preStyle.overflowX !== 'auto' && preStyle.overflowX !== 'scroll') {
                    problems.push(`Pre block lacks overflow-x: auto`);
                }
            });

            return problems;
        }, f);

        console.log(`\n=== [${f}] (375x667) ===`);
        if (analysis.length === 0) {
            console.log('  No issues flagged.');
        } else {
            analysis.forEach(p => console.log('  !', p));
        }
    }

    await browser.close();
}

inspectPages().catch(console.error);

