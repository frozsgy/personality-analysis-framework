const express = require('express');
const app = express();
const port = process.env.PORT || 8081;
const path = require('path');
const fs = require('fs')
const server = "https://personality-api.ozanalpay.com/";
const defaultImage = "personality-dimensions-chart.png";
const url = require('url');

const defaultTags = (request, response, image = defaultImage) => {
  const filePath = path.resolve(__dirname, './build', 'index.html');

  fs.readFile(filePath, 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    
    data = data.replace(/\$OG_TITLE/g, 'Tweetleriniz ile Kişilik Analizi');
    data = data.replace(/\$OG_DESCRIPTION/g, "Bilimsel olarak kanıtlanmış yöntemimiz ile tweetlerinizi analiz edip Twitter'da nasıl bir kişilik temsil ettiğinizi hesaplıyoruz. Makine Öğrenmesi kullanarak yöntemimizi sürekli iyileştiriyoruz.");
    data = data.replace(/\$OG_IMAGE/g, image);
    response.send(data);
  });
}

app.get('/', function(request, response) {
  defaultTags(request, response); 
});


app.get('/callback', function(request, response) {
  defaultTags(request, response); 
});

app.get('/result', function(request, response) {
  const queryObject = url.parse(request.url,true).query;
  const imageUrl = server + "image?hash=" + queryObject.hash;
  defaultTags(request, response, imageUrl); 
});

app.get('/share/*', function(request, response) {
  const hash = request.url.split('/')[2];
  const imageUrl = server + "image?hash=" + hash;
  defaultTags(request, response, imageUrl); 
});

app.use(express.static(path.resolve(__dirname, './build')));

app.get('*', function(request, response) {
  const filePath = path.resolve(__dirname, './build', 'index.html');
  response.sendFile(filePath);
});

app.listen(port, () => console.log(`Listening on port ${port}`));