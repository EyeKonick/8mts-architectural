const sharp = require('sharp'); const fs = require('fs'); const path = require('path');
const dir = process.argv[2]; const files = fs.readdirSync(dir).filter(f => /^u-.*\.jpg$/.test(f)).sort();
(async () => {
  const W = 480, H = 320, cols = 4, rows = Math.ceil(files.length / cols);
  const comps = [];
  for (let i = 0; i < files.length; i++) {
    const buf = await sharp(path.join(dir, files[i])).resize(W, H, { fit: 'cover' }).toBuffer();
    const label = Buffer.from(`<svg width="60" height="44"><rect width="60" height="44" fill="red"/><text x="10" y="32" font-size="30" fill="white" font-family="Arial">${i}</text></svg>`);
    comps.push({ input: buf, left: (i % cols) * W, top: Math.floor(i / cols) * H }, { input: label, left: (i % cols) * W, top: Math.floor(i / cols) * H });
    console.log(i, files[i]);
  }
  await sharp({ create: { width: W * cols, height: H * rows, channels: 3, background: '#fff' } }).composite(comps).jpeg().toFile(path.join(dir, 'sheet.jpg'));
})();
