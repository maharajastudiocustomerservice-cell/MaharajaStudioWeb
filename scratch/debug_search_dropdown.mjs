import { createRequire } from 'module';
import { pathToFileURL } from 'url';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

async function test() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

    page.on('console', msg => console.log('PAGE LOG:', msg.type(), msg.text()));
    page.on('pageerror', err => console.log('PAGE ERROR:', err.message));

    await page.goto('file:///C:/Users/Soutick/MyCreation/MaharajaStudioWeb/msultimate-docs.html');
    await page.waitForTimeout(500);

    const input = await page.$('#doc-search');
    console.log('Input found:', !!input);
    if (input) {
        await page.fill('#doc-search', 'hea');
        await page.waitForTimeout(500);
    }

    const dropdown = await page.$('#ecosystem-search-results');
    console.log('Dropdown found:', !!dropdown);
    if (dropdown) {
        const isHidden = await dropdown.evaluate(el => el.classList.contains('is-hidden'));
        const box = await dropdown.boundingBox();
        const html = await dropdown.innerHTML();
        console.log('Dropdown isHidden:', isHidden);
        console.log('Dropdown bounding box:', box);
        console.log('Dropdown items count:', (await dropdown.$$('.eco-search-item')).length);
    }

    await page.screenshot({ path: 'scratch/test-search-dropdown.png' });
    await browser.close();
    console.log('Screenshot saved to scratch/test-search-dropdown.png');
}

test().catch(console.error);
