import express, { Request, Response } from 'express';
import { spawn } from 'child_process';

const app = express();
const port = process.env.PORT || 3000;

// ルートハンドラーのインポート
const indexRouter = require('./routes/index');
const aboutRouter = require('./routes/about');
const contactRouter = require('./routes/contact');

// 静的ファイルの提供
app.use(express.static('public'));

// ルートハンドラーの設定
app.use('/', indexRouter);
app.use('/about', aboutRouter);
app.use('/contact', contactRouter);
app.post('/run', express.json(), async (req: Request, res: Response) => {
  try {
    const { appName } = req.body;
    const pythonApps = [
      { name: 'Bingo', command: 'src/bingo/main.py' },
      { name: 'Shooting Game', command: 'src/shootingGame/main.py' }
    ];
    const selectedApp = pythonApps.find((app) => app.name === appName);

    if (!selectedApp) {
      res.status(404).send('App not found');
      return;
    }

    const pythonProcess = spawn('python', [selectedApp.command]);
    let output = '';

    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`Error executing ${appName}:`, data.toString());
    });

    pythonProcess.on('close', (code) => {
      console.log(`Process exited with code ${code}`);
      res.json({ appName, output });
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
