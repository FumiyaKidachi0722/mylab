import express, { Request, Response } from 'express';
const router = express.Router();

router.get('/', async (req: Request, res: Response) => {
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
        </style>
      </head>
      <body>
        <!-- ヘッダーのインクルード -->
        ${require('../partials/header')}
        
        <h1>About</h1>
        <p>This is the about page.</p>
        
        <!-- フッターのインクルード -->
        ${require('../partials/footer')}
      </body>
    </html>
  `);
});

module.exports = router;
