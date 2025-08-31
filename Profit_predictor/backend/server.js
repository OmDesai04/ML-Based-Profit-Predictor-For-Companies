const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");

const app = express();
app.use(cors());
app.use(express.json());

app.post("/predict", (req, res) => {
  const { rndSpend, admin, marketing } = req.body;

  const r = Number(rndSpend);
  const a = Number(admin);
  const m = Number(marketing);
  if (!Number.isFinite(r) || !Number.isFinite(a) || !Number.isFinite(m)) {
    return res.status(400).json({ error: "Invalid inputs" });
  }

  const path = require("path");
  const fs = require("fs");

  const venvPython = path.resolve(__dirname, "..", "..", ".venv", "Scripts", "python.exe");
  const preferred = process.env.PYTHON_PATH && fs.existsSync(process.env.PYTHON_PATH)
    ? process.env.PYTHON_PATH
    : (fs.existsSync(venvPython) ? venvPython : null);

  const runPython = (cmd) =>
    spawn(cmd, ["app.py", r, a, m], { cwd: __dirname });

  let py = preferred ? runPython(preferred) : runPython("python");
  let result = "";
  let hadError = false;

  const attachHandlers = () => {
    py.stdout.on("data", (data) => {
      result += data.toString();
    });

    py.stderr.on("data", (data) => {
      hadError = true;
      console.error(`stderr: ${data}`);
    });

    py.on("error", (err) => {
      // Fallback to 'py' on Windows if the first attempt fails
      if (process.platform === "win32" && err) {
        py = runPython("py");
        result = "";
        hadError = false;
        attachHandlers();
      } else {
        res.status(500).json({ error: "Python not available" });
      }
    });

    py.on("close", () => {
      const num = parseFloat(result.trim());
      if (hadError || !Number.isFinite(num)) {
        return res.status(500).json({ error: "Prediction failed" });
      }
      res.json({ prediction: num });
    });
  };

  attachHandlers();
});

const PORT = Number(process.env.PORT) || 5000;
function startServer(port) {
  const server = app.listen(port, () => console.log(`Server running on port ${port}`));
  server.on("error", (err) => {
    if (err && err.code === "EADDRINUSE") {
      const fallback = port + 1;
      console.warn(`Port ${port} in use, retrying on ${fallback}...`);
      startServer(fallback);
    } else {
      throw err;
    }
  });
}

startServer(PORT);