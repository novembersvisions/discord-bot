const polka = require('polka');
const send = require('@polka/send-type');
const compress = require('compression')();
const cors = require('cors');

const baseURL = "http://hivemindbot.surge.sh/img/" 
polka()
    .use(cors())
    .use(compress)
    .get('/get', (req, res) => {
        let airplanes = 22
        const randairplanes = Math.floor(Math.random() * (airplanes - 1) + 1);
        let data = {
            "image": `${baseURL}${randairplanes}.jpg`,
        }
        console.log(data);
        send(res, 200, data);
    })
    .listen(333, err => {
        if (err) throw err;
        console.log(`> Running on http://localhost:333`);
    });

  /* const url = "http://hivemindbot.surge.sh/get";
   let plane;
   let result;
   async function fetchImg() {
        const response = await fetch(url)
        result = await response.json()
        plane = result.image;
     }
   fetchImg() */