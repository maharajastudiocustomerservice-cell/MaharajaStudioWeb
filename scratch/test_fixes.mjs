import { createRequire } from 'module';
import { pathToFileURL } from 'url';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const workspace = 'c:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function testFixes() {
    console.log('Testing fixes with Playwright Chromium...');
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

    // 1. Test msultimate-docs.html search dropdown visibility
    console.log('\n--- 1. Testing msultimate-docs.html search dropdown ---');
    const docUrl = pathToFileURL(path.join(workspace, 'msultimate-docs.html')).href;
    await page.goto(docUrl, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    const searchInput = page.locator('#doc-search');
    await searchInput.fill('hea');
    await page.waitForTimeout(400);

    const dropdown = page.locator('#ecosystem-search-results');
    const isVisible = await dropdown.isVisible();
    console.log(`Dropdown visible: ${isVisible}`);

    const dropdownBox = await dropdown.boundingBox();
    const heroBox = await page.locator('header.hero').boundingBox();
    console.log(`Dropdown bounds: y=${dropdownBox.y}, height=${dropdownBox.height}, bottom=${dropdownBox.y + dropdownBox.height}`);
    console.log(`Hero bounds: y=${heroBox.y}, height=${heroBox.height}, bottom=${heroBox.y + heroBox.height}`);

    const isExtendingPastHero = (dropdownBox.y + dropdownBox.height) > (heroBox.y + heroBox.height);
    console.log(`Is dropdown extending past hero bottom boundary? ${isExtendingPastHero}`);

    await page.screenshot({ path: path.join(workspace, 'scratch/test-search-dropdown.png') });
    console.log('Saved scratch/test-search-dropdown.png');

    // 2. Test index.html interactive hero switching
    console.log('\n--- 2. Testing index.html hero interactivity ---');
    const indexUrl = pathToFileURL(path.join(workspace, 'index.html')).href;
    await page.goto(indexUrl, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    const heroTitle = page.locator('#hero-title');
    const titleInitial = await heroTitle.innerText();
    console.log(`Initial hero title (MSUltimate): "${titleInitial}"`);

    // Click MSMotion tab
    console.log('Clicking [MSMotion] tab...');
    await page.click('button[data-tab-target="msmotion"]');
    await page.waitForTimeout(300);
    const titleMSMotion = await heroTitle.innerText();
    const descMSMotion = await page.locator('#hero-desc').innerText();
    const btnHrefMSMotion = await page.locator('#hero-btn-primary').getAttribute('href');
    const meta1MSMotion = await page.locator('#hero-meta-1').innerText();
    console.log(`After click MSMotion: title="${titleMSMotion}"`);
    console.log(`   desc="${descMSMotion}"`);
    console.log(`   btnHref="${btnHrefMSMotion}"`);
    console.log(`   meta1="${meta1MSMotion}"`);

    await page.screenshot({ path: path.join(workspace, 'scratch/test-index-msmotion.png') });
    console.log('Saved scratch/test-index-msmotion.png');

    // Click Scriptable Studio tab
    console.log('Clicking [Scriptable Studio] tab...');
    await page.click('button[data-tab-target="scriptable"]');
    await page.waitForTimeout(300);
    const titleScriptable = await heroTitle.innerText();
    console.log(`After click Scriptable: title="${titleScriptable}"`);

    // Click Tactical AI tab
    console.log('Clicking [Tactical AI] tab...');
    await page.click('button[data-tab-target="tactical"]');
    await page.waitForTimeout(300);
    const titleTactical = await heroTitle.innerText();
    console.log(`After click Tactical AI: title="${titleTactical}"`);

    // Click Object Finder tab
    console.log('Clicking [Object Finder] tab...');
    await page.click('button[data-tab-target="finder"]');
    await page.waitForTimeout(300);
    const titleFinder = await heroTitle.innerText();
    console.log(`After click Object Finder: title="${titleFinder}"`);

    // Click Quick Inspector tab
    console.log('Clicking [Quick Inspector] tab...');
    await page.click('button[data-tab-target="quick"]');
    await page.waitForTimeout(300);
    const titleQuick = await heroTitle.innerText();
    console.log(`After click Quick Inspector: title="${titleQuick}"`);

    // Click back to MSUltimate
    console.log('Clicking back to [MSUltimate] tab...');
    await page.click('button[data-tab-target="msultimate"]');
    await page.waitForTimeout(300);
    const titleBack = await heroTitle.innerText();
    console.log(`After click back MSUltimate: title="${titleBack}"`);

    // Check stats strip on index.html
    const statLabels = await page.locator('.stats-strip .stat-label').allInnerTexts();
    const statValues = await page.locator('.stats-strip .stat-value').allInnerTexts();
    console.log('\n--- Stats Strip on index.html ---');
    for (let i = 0; i < statLabels.length; i++) {
        console.log(`   ${statLabels[i]}: ${statValues[i]}`);
    }

    // Check featured cards on index.html
    const cardTags = await page.locator('#featured-assets .asset-meta-row').allInnerTexts();
    console.log('\n--- Featured Cards Badges on index.html ---');
    cardTags.forEach((t, i) => console.log(`   Card ${i+1}: ${t.replace(/\n/g, ' ')}`));

    // 3. Test ms-motion.html telemetry strip
    console.log('\n--- 3. Testing ms-motion.html telemetry strip ---');
    const motionUrl = pathToFileURL(path.join(workspace, 'ms-motion.html')).href;
    await page.goto(motionUrl, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    const motionStatLabels = await page.locator('.stats-strip .stat-label').allInnerTexts();
    const motionStatValues = await page.locator('.stats-strip .stat-value').allInnerTexts();
    for (let i = 0; i < motionStatLabels.length; i++) {
        console.log(`   ${motionStatLabels[i]}: ${motionStatValues[i]}`);
    }

    await page.screenshot({ path: path.join(workspace, 'scratch/test-ms-motion.png') });
    console.log('Saved scratch/test-ms-motion.png');

    console.log(`\nTotal Errors recorded: ${errors.length}`);
    if (errors.length > 0) {
        console.log('Errors:', errors);
    }

    await browser.close();
    console.log('\nAll test checks completed!');
}

testFixes().catch(err => {
    console.error('Fatal test error:', err);
    process.exit(1);
});

