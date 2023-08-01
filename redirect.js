const http = require('http');

http.createServer((req, res) => {
  const redirectUrl = `https://www.highlyfecollective.com${req.url}`;

  res.writeHead(301, {
    'Location': redirectUrl,
  });
  res.end();
}).listen(process.env.PORT || 3000);
