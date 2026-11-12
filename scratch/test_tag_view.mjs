import { createRequire } from 'module';
import { pathToFileURL } from 'url';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const workspace = 'c:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function testTags() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

    const coreUrl = pathToFileURL(path.join(workspace, 'msultimate-core-docs.html')).href + '#cat-callbacks';
    await page.goto(coreUrl, { waitUntil: 'load' });
    await page.waitForTimeout(600);

    await page.screenshot({ path: path.join(workspace, 'scratch/test-callbacks-tags.png') });
    console.log('Saved scratch/test-callbacks-tags.png');
    await browser.close();
}

testTags();

