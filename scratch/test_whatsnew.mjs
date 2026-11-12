import { createRequire } from 'module';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function testPage() {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 360, height: 740 } });
    await page.goto('file:///' + path.join(rootDir, 'tactical_ai_whats_new.html').replace(/\\/g, '/'));

    const res = await page.evaluate(() => {
        const sw = document.documentElement.scrollWidth;
        const cw = document.documentElement.clientWidth;
        const bsw = document.body.scrollWidth;
        const bcw = document.body.clientWidth;

        const overflows = [];
        document.querySelectorAll('*').forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.right > cw + 1) {
                overflows.push({
                    tag: el.tagName,
                    cls: el.className,
                    w: Math.round(r.width),
                    right: Math.round(r.right),
                    text: el.textContent.slice(0, 30)
                });
            }
        });
        return { sw, cw, bsw, bcw, overflows: overflows.slice(0, 10) };
    });

    console.log(res);
    await browser.close();
}

testPage().catch(console.error);

