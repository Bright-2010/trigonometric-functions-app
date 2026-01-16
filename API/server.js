const express = require("express");
const app = express();

app.get("/trigapi", (req, res) => {
  const { type, deg } = req.query;

  const degree = Number(deg);

  // 基本校验
  if (!type || isNaN(degree)) {
    return res.status(400).json({
      error: "参数错误，需要 type 和 deg"
    });
  }

  // 角度 → 弧度
  const rad = degree * Math.PI / 180;

  let result;

  switch (type.toLowerCase()) {
    case "sin":
      result = Math.sin(rad);
      break;
    case "cos":
      result = Math.cos(rad);
      break;
    case "tan":
      result = Math.tan(rad);
      break;
    default:
      return res.status(400).json({
        error: "type 只能是 sin / cos / tan"
      });
  }

  res.json({
    type,
    degree,
    radian: rad,
    result: Number(result.toFixed(12)) // 控制浮点误差
  });
});

app.listen(3000, () => {
  console.log("Trig API running at http://localhost:3000");
});
