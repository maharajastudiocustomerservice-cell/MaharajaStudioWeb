import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function checkObjectFinderLayout() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    await page.goto('file:///' + path.join(rootDir, 'object-finder-pro.html').replace(/\\/g, '/'));

    const data = await page.evaluate(() => {
        const sections = Array.from(document.querySelectorAll('section, header, footer')).map(s => {
            const h = s.querySelector('h1, h2, h3')?.textContent.trim() || s.className || s.tagName;
            const r = s.getBoundingClientRect();
            return {
                title: h,
                top: Math.round(r.top),
                height: Math.round(r.height),
                width: Math.round(r.width)
            };
        });

        const workbench = document.querySelector('.workbench-frame');
        const wbRect = workbench ? workbench.getBoundingClientRect() : null;

        const tabs = Array.from(document.querySelectorAll('.workbench-tab')).map(t => ({
            text: t.textContent.trim(),
            rect: t.getBoundingClientRect()
        }));

        const inspectorRows = Array.from(document.querySelectorAll('.inspector-row')).map(r => {
            const key = r.querySelector('.inspector-key')?.textContent.trim();
            const val = r.querySelector('.inspector-val')?.textContent.trim();
            const rect = r.getBoundingClientRect();
            return { key, val, height: Math.round(rect.height), width: Math.round(rect.width) };
        });

        const filterGrid = document.querySelector('.grid-2, .grid-3, .grid-4');
        const filterGridCards = filterGrid ? Array.from(filterGrid.children).map(c => {
            const r = c.getBoundingClientRect();
            return { tag: c.tagName, width: Math.round(r.width), height: Math.round(r.height) };
        }) : [];

        return {
            sections,
            wbRect,
            tabs,
            inspectorRows: inspectorRows.slice(0, 10),
            filterGridCards
        };
    });

    console.log('OBJECT FINDER PRO MOBILE LAYOUT:');
    console.log('Tabs:', data.tabs.map(t => `${t.text} (y: ${Math.round(t.rect.y)}, w: ${Math.round(t.rect.width)})`));
    console.log('Workbench rect:', data.wbRect);
    console.log('Inspector rows:');
    data.inspectorRows.forEach(r => console.log(`  - [${r.key}]: [${r.val}] (h: ${r.height})`));

    await browser.close();
}

checkObjectFinderLayout().catch(console.error);

