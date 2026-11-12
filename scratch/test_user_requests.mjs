import { createRequire } from 'module';
import { pathToFileURL } from 'url';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const workspace = 'c:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function verifyAll() {
    console.log('Running Playwright verification on all new requirements...');
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

    const errors = [];
    page.on('console', msg => {
        const txt = msg.text();
        if (msg.type() === 'error' && !txt.includes('ERR_NAME_NOT_RESOLVED') && !txt.includes('fonts.googleapis.com')) {
            errors.push(`[Console Error] ${txt}`);
        }
    });
    page.on('pageerror', err => {
        errors.push(`[Page Error] ${err.message}`);
    });

    // 1. Check index.html with interactive cards
    console.log('\n--- 1. Testing index.html with dynamic selected asset cards ---');
    const indexUrl = pathToFileURL(path.join(workspace, 'index.html')).href;
    await page.goto(indexUrl, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    // Check Initial Stats (MSUltimate)
    let statLabels = await page.locator('#hero-asset-stats .stat-label').allInnerTexts();
    let statValues = await page.locator('#hero-asset-stats .stat-value').allInnerTexts();
    console.log('Initial stats (MSUltimate):');
    statLabels.forEach((l, i) => console.log(`   ${l}: ${statValues[i]}`));
    await page.screenshot({ path: path.join(workspace, 'scratch/verify-index-msultimate.png') });

    // Click MSMotion tab
    console.log('\nClicking [MSMotion] tab...');
    await page.click('button[data-tab-target="msmotion"]');
    await page.waitForTimeout(300);

    statLabels = await page.locator('#hero-asset-stats .stat-label').allInnerTexts();
    statValues = await page.locator('#hero-asset-stats .stat-value').allInnerTexts();
    console.log('After clicking MSMotion:');
    statLabels.forEach((l, i) => console.log(`   ${l}: ${statValues[i]}`));

    // Check MSMotion workbench image
    const msmotionImgSrc = await page.locator('div[data-tab-pane="msmotion"] img').getAttribute('src');
    console.log(`MSMotion workbench image src: ${msmotionImgSrc}`);

    // Check flagship card image
    const flagshipImgSrc = await page.locator('.flagship-card:has-text("MSMotion") img').first().getAttribute('src');
    console.log(`MSMotion flagship image src: ${flagshipImgSrc}`);

    await page.screenshot({ path: path.join(workspace, 'scratch/verify-index-msmotion.png') });

    // Click Tactical AI tab
    console.log('\nClicking [Tactical AI] tab...');
    await page.click('button[data-tab-target="tactical"]');
    await page.waitForTimeout(300);

    statLabels = await page.locator('#hero-asset-stats .stat-label').allInnerTexts();
    statValues = await page.locator('#hero-asset-stats .stat-value').allInnerTexts();
    console.log('After clicking Tactical AI:');
    statLabels.forEach((l, i) => console.log(`   ${l}: ${statValues[i]}`));
    await page.screenshot({ path: path.join(workspace, 'scratch/verify-index-tactical.png') });

    // Click Scriptable Studio tab
    console.log('\nClicking [Scriptable Studio] tab...');
    await page.click('button[data-tab-target="scriptable"]');
    await page.waitForTimeout(300);
    statLabels = await page.locator('#hero-asset-stats .stat-label').allInnerTexts();
    statValues = await page.locator('#hero-asset-stats .stat-value').allInnerTexts();
    console.log('After clicking Scriptable:');
    statLabels.forEach((l, i) => console.log(`   ${l}: ${statValues[i]}`));

    // Click Object Finder tab
    console.log('\nClicking [Object Finder] tab...');
    await page.click('button[data-tab-target="finder"]');
    await page.waitForTimeout(300);
    statLabels = await page.locator('#hero-asset-stats .stat-label').allInnerTexts();
    statValues = await page.locator('#hero-asset-stats .stat-value').allInnerTexts();
    console.log('After clicking Object Finder:');
    statLabels.forEach((l, i) => console.log(`   ${l}: ${statValues[i]}`));

    // Click Quick Inspector tab
    console.log('\nClicking [Quick Inspector] tab...');
    await page.click('button[data-tab-target="quick"]');
    await page.waitForTimeout(300);
    statLabels = await page.locator('#hero-asset-stats .stat-label').allInnerTexts();
    statValues = await page.locator('#hero-asset-stats .stat-value').allInnerTexts();
    console.log('After clicking Quick Inspector:');
    statLabels.forEach((l, i) => console.log(`   ${l}: ${statValues[i]}`));

    // 2. Check msultimate-core-docs.html#cat-callbacks tag layout
    console.log('\n--- 2. Testing msultimate-core-docs.html attribute target badges ---');
    const coreUrl = pathToFileURL(path.join(workspace, 'msultimate-core-docs.html')).href + '#cat-callbacks';
    await page.goto(coreUrl, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    const onFieldBlurRow = page.locator('tr:has-text("[OnFieldBlur]")');
    const tags = await onFieldBlurRow.locator('.tag').allInnerTexts();
    console.log(`OnFieldBlur tags: ${JSON.stringify(tags)}`);

    const blurTagBox = await onFieldBlurRow.locator('.tag-group').boundingBox();
    console.log(`OnFieldBlur tag-group box: width=${blurTagBox.width}, height=${blurTagBox.height}`);

    await page.screenshot({ path: path.join(workspace, 'scratch/verify-core-tags.png') });

    console.log(`\nTotal Errors recorded: ${errors.length}`);
    if (errors.length > 0) {
        console.log('Errors:', errors);
    }

    await browser.close();
    console.log('\nVerification suite finished successfully!');
}

verifyAll().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});

