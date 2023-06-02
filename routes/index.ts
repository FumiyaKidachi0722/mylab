import express, { Request, Response } from 'express';
const router = express.Router();

router.get('/', async (req: Request, res: Response) => {
  try {
    const pythonApps = [
      { name: 'Bingo', command: 'src/bingo/main.py' },
      { name: 'Shooting Game', command: 'src/shootingGame/main.py' }
    ];

    const appListItems = pythonApps
      .map((app) => `<li onclick="runApp('${app.name}')">${app.name}</li>`)
      .join('');

    res.send(`
      <html>
        <head>
          <style>
            body {
              font-family: Arial, sans-serif;
            }
            h1 {
              text-align: center;
            }
            ul {
              list-style-type: none;
              padding: 0;
              margin: 0;
            }
            li {
              padding: 10px;
              background-color: #f2f2f2;
              margin-bottom: 10px;
              cursor: pointer;
            }
          </style>
          <script>
            async function runApp(appName) {
              if (['Bingo', 'Shooting Game'].includes(appName)) {
                const response = await fetch('/run', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ appName })
                });
                const data = await response.json();
                console.log(data);
              }
            }
          </script>
        </head>
        <body>
          <!-- ヘッダーのインクルード -->
          ${require('../partials/header')}
          
          <h1>Python Apps</h1>
          <ul>
            ${appListItems}
          </ul>
          
          <!-- フッターのインクルード -->
          ${require('../partials/footer')}
        </body>
      </html>
    `);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});

module.exports = router;
