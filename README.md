# StarWiki · Web 版（编译产物）

本分支 `web` 存放 **Ren'Py Web / WASM 编译产物**，用于通过 GitHub Pages 直接浏览器试玩。

> ⚠️ 这是构建输出，**不要在此分支改源码**。源码在 `main` 分支，设计文档在 `docs/design` 分支。

## 在线试玩

由本分支经 GitHub Pages 发布：

👉 https://milab-bit.github.io/starwiki/

（首次上线需在仓库 **Settings → Pages** 将源分支设为 `web`、目录选 root。）

## 本分支内容

| 文件 | 作用 |
|------|------|
| `index.html` | 入口页面 |
| `renpy.wasm` / `renpy.js` / `renpy.data` | Ren'Py Web 运行时 |
| `game.zip` | 游戏资源包 |
| `service-worker.js` | PWA 离线缓存 |
| `manifest.json` / `pwa_catalog.json` | PWA 清单 |
| `renpy-pre.js` | 运行时前置脚本 |
| `web-presplash.jpg` / `icons/` | 启动图与图标 |

## 如何从源码重新构建

源码见 `main` 分支，使用 Ren'Py 的 Web 构建（如 `renpy.sh web_build .` 或 Ren'Py Launcher → Build → Web），
将生成的 `web/` 目录内容同步回本分支即可。

---

出品：上海端点星幻境科技有限公司 ｜ 制作：AIGC艺术家 · 吟游诗人Lab
仅供展示与交流。未经授权请勿商用转售。
