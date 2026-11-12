import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function checkHeroLayout() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    await page.goto('file:///' + path.join(rootDir, 'index.html').replace(/\\/g, '/'));

    const data = await page.evaluate(() => {
        const tabs = Array.from(document.querySelectorAll('.workbench-tab')).map(t => ({
            text: t.textContent.trim(),
            rect: t.getBoundingClientRect()
        }));
        const tabsContainer = document.querySelector('.workbench-tabs');
        const containerRect = tabsContainer ? tabsContainer.getBoundingClientRect() : null;

        const heroActions = document.querySelector('.hero-actions');
        const actionButtons = heroActions ? Array.from(heroActions.querySelectorAll('a, button')).map(b => ({
            text: b.textContent.trim(),
            rect: b.getBoundingClientRect()
        })) : [];

        const statsStrip = document.querySelector('.stats-strip, .stats-strip-6');
        const statCells = statsStrip ? Array.from(statsStrip.querySelectorAll('.stat-cell')).map(c => ({
            label: c.querySelector('.stat-label')?.textContent.trim(),
            val: c.querySelector('.stat-value')?.textContent.trim(),
            rect: c.getBoundingClientRect()
        })) : [];

        return {
            containerRect,
            tabs,
            actionButtons,
            statCells
        };
    });

    console.log('INDEX.HTML MOBILE DATA:');
    console.log('Tabs container height:', data.containerRect?.height);
    console.log('Tabs:', data.tabs.map(t => `${t.text} (y: ${Math.round(t.rect.y)}, h: ${Math.round(t.rect.height)})`));
    console.log('Action buttons:', data.actionButtons.map(b => `${b.text} (x: ${Math.round(b.rect.x)}, y: ${Math.round(b.rect.y)}, w: ${Math.round(b.rect.width)}, h: ${Math.round(b.rect.height)})`));
    console.log('Stat cells count:', data.statCells.length);

    await browser.close();
}

checkHeroLayout().catch(console.error);

