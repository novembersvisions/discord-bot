// get airplane images

var Scraper = require('images-scraper');

const google = new Scraper({
  puppeteer: {
    headless: true,
    detail: false,
  },
  tbs: {
    isz: "l",
  }
});

(async () => {
  const results = await google.scrape('airplane', 200);
  console.log('results', results);
})();