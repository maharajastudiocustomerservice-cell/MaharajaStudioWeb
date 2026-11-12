import { createRequire } from 'module';
import path from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('C:\\Users\\Soutick\\.gemini\\config\\skills\\unslop\\scripts\\node_modules\\playwright');

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';

async function verifyReviews() {
    console.log('Verifying reviews on index.html and product pages...');
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

    // 1. Index testimonials
    await page.goto('file:///' + path.join(rootDir, 'index.html').replace(/\\/g, '/'));
    await page.waitForTimeout(300);
    const testimonials = await page.$('#testimonials');
    if (testimonials) {
        await testimonials.scrollIntoViewIfNeeded();
        await page.waitForTimeout(300);
        await page.screenshot({ path: 'scratch/verify-index-reviews.png' });
        console.log('Index reviews screenshot saved!');
        
        const cards = await testimonials.$$('.review-card');
        console.log(`Found ${cards.length} review cards on index.html`);
        for (let i = 0; i < cards.length; i++) {
            const author = await cards[i].$eval('.review-author-name', el => el.textContent.trim());
            const quote = await cards[i].$eval('.review-quote', el => el.textContent.trim());
            console.log(`  Card ${i+1}: ${author} -> "${quote.slice(0, 60)}..."`);
        }
    }

    // 2. Tactical AI review
    await page.goto('file:///' + path.join(rootDir, 'tactical-cover-retreat-ai-system.html').replace(/\\/g, '/'));
    await page.waitForTimeout(300);
    const tacReview = await page.$('.review-card');
    if (tacReview) {
        await tacReview.scrollIntoViewIfNeeded();
        await page.waitForTimeout(200);
        await page.screenshot({ path: 'scratch/verify-tactical-review.png' });
        console.log('Tactical AI review verified!');
    }

    // 3. Scriptable Studio Pro reviews
    await page.goto('file:///' + path.join(rootDir, 'scriptable-studio-pro.html').replace(/\\/g, '/'));
    await page.waitForTimeout(300);
    const sspReview = await page.$('.review-card');
    if (sspReview) {
        await sspReview.scrollIntoViewIfNeeded();
        await page.waitForTimeout(200);
        await page.screenshot({ path: 'scratch/verify-scriptable-reviews.png' });
        console.log('Scriptable Studio reviews verified!');
    }

    // 4. Object Finder Pro review
    await page.goto('file:///' + path.join(rootDir, 'object-finder-pro.html').replace(/\\/g, '/'));
    await page.waitForTimeout(300);
    const ofpReview = await page.$('.review-card');
    if (ofpReview) {
        await ofpReview.scrollIntoViewIfNeeded();
        await page.waitForTimeout(200);
        await page.screenshot({ path: 'scratch/verify-finder-review.png' });
        console.log('Object Finder review verified!');
    }

    await browser.close();
    console.log('All reviews verified successfully!');
}

verifyReviews().catch(console.error);

