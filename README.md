# StarWiki / 天文馆 XR 剧情 Demo

仓库：https://github.com/MiLab-Bit/starwiki

可玩剧情原型：双线体验——《航向火星·救援队归来》×《回到普林斯顿》第 1 集。  
引擎：[Ren'Py](https://www.renpy.org/) 8.x · 分辨率 1280×720（16:9）

出品：上海端点星幻境科技有限公司  
制作：AIGC艺术家 · 吟游诗人Lab

## 仓库说明

本仓库为**完整工程源码**（脚本、图像、音频、字体），可在 Ren'Py SDK 中直接打开与修改。

```
TianwenguanXRDemo/
├── project.json          # Ren'Py 工程元数据
├── game/
│   ├── script.rpy        # 入口与枢纽
│   ├── mars_rescue.rpy   # 火星救援线
│   ├── princeton_ep1.rpy # 普林斯顿第 1 集
│   ├── screens.rpy       # UI / HUD / 片尾滚词
│   ├── options.rpy       # 工程配置与版本号
│   ├── audio_defs.rpy    # 音频定义
│   ├── images_defs.rpy   # 图像与 Q 头像逻辑
│   ├── simhei.ttf        # 界面字体
│   ├── audio/            # BGM / 环境音 / 主题曲
│   └── images/           # 场景与 busts
└── README.md
```

## 本地运行

1. 安装 [Ren'Py 8.5+](https://www.renpy.org/latest.html)
2. 将本仓库放入 Ren'Py 的 `projects` 目录，或在启动器中选择「偏好 → Projects Directory」指向本仓库父目录
3. 启动器中选中 **TianwenguanXRDemo** → Launch Project

也可命令行（将 SDK 路径换成你的本机路径）：

```bat
renpy.exe TianwenguanXRDemo
```

## 博物馆体验版

面向馆方演示的 **Windows PC 可执行包**请使用另行提供的「博物馆体验版」压缩包（含 `TianwenguanXRDemo.exe`，无需安装 Ren'Py）。

## 版本

见 `game/options.rpy` 中 `config.version`。

## 许可与用途

仅用于方案展示、评审演示与双方合作对齐。未经书面授权请勿商用转售。
