import fs from 'fs';
import path from 'path';

const rootDir = 'C:/Users/Soutick/MyCreation/MaharajaStudioWeb';
const files = fs.readdirSync(rootDir).filter(f => f.endsWith('.html'));

let badCount = 0;

for (const file of files) {
    const html = fs.readFileSync(path.join(rootDir, file), 'utf-8');
    const regex = /<img[^>]+src=["']([^"']+)["']/g;
    let m;
    while ((m = regex.exec(html)) !== null) {
        const src = m[1];
        if (src.startsWith('http') || src.startsWith('data:')) continue;
        const cleanSrc = src.split('?')[0].split('#')[0];
        const fullPath = path.resolve(rootDir, cleanSrc);
        if (!fs.existsSync(fullPath)) {
            console.error(`[${file}] Missing image: ${src} -> ${fullPath}`);
            badCount++;
        }
    }
}

if (badCount === 0) {
    console.log(`All images across all ${files.length} HTML files exist on disk!`);
} else {
    console.log(`Found ${badCount} missing images.`);
}

