import { createRequire } from 'module';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function checkAfterMetrics() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });

    console.log('=== VERIFYING INDEX.HTML METRICS ===');
    await page.goto('file:///' + path.join(rootDir, 'index.html').replace(/\\/g, '/'));
    const indexMetrics = await page.evaluate(() => {
        const tabsContainer = document.querySelector('.workbench-tabs');
        const heroActions = document.querySelector('.hero-actions');
        const buttons = heroActions ? Array.from(heroActions.querySelectorAll('.btn')).map(b => ({
            text: b.textContent.trim(),
            w: Math.round(b.getBoundingClientRect().width),
            h: Math.round(b.getBoundingClientRect().height)
        })) : [];
        return {
            tabsHeight: tabsContainer ? Math.round(tabsContainer.getBoundingClientRect().height) : null,
            buttons
        };
    });
    console.log('Index tabs height:', indexMetrics.tabsHeight);
    console.log('Index buttons:', indexMetrics.buttons);

    console.log('\n=== VERIFYING OBJECT-FINDER-PRO.HTML METRICS ===');
    await page.goto('file:///' + path.join(rootDir, 'object-finder-pro.html').replace(/\\/g, '/'));
    const ofpMetrics = await page.evaluate(() => {
        const tabsContainer = document.querySelector('.workbench-tabs');
        const heroActions = document.querySelector('.hero-actions');
        const buttons = heroActions ? Array.from(heroActions.querySelectorAll('.btn')).map(b => ({
            text: b.textContent.trim(),
            w: Math.round(b.getBoundingClientRect().width),
            h: Math.round(b.getBoundingClientRect().height)
        })) : [];
        const inspectorRows = Array.from(document.querySelectorAll('.inspector-row')).slice(0, 5).map(r => ({
            text: r.textContent.trim().slice(0, 35),
            h: Math.round(r.getBoundingClientRect().height),
            w: Math.round(r.getBoundingClientRect().width)
        }));
        return {
            tabsHeight: tabsContainer ? Math.round(tabsContainer.getBoundingClientRect().height) : null,
            buttons,
            inspectorRows
        };
    });
    console.log('OFP tabs height:', ofpMetrics.tabsHeight);
    console.log('OFP buttons:', ofpMetrics.buttons);
    console.log('OFP inspector rows:', ofpMetrics.inspectorRows);

    console.log('\n=== VERIFYING MSULTIMATE.HTML METRICS ===');
    await page.goto('file:///' + path.join(rootDir, 'msultimate.html').replace(/\\/g, '/'));
    const msuMetrics = await page.evaluate(() => {
        const tabsContainer = document.querySelector('.workbench-tabs');
        return {
            tabsHeight: tabsContainer ? Math.round(tabsContainer.getBoundingClientRect().height) : null,
            tabCount: document.querySelectorAll('.workbench-tab').length
        };
    });
    console.log(`MSUltimate: ${msuMetrics.tabCount} tabs in container height: ${msuMetrics.tabsHeight}px`);

    await browser.close();
}

checkAfterMetrics().catch(console.error);

