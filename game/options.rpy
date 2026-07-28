## 天文馆 XR 剧情 Demo · 工程配置
## Ren'Py 8.x

define config.name = _("天文馆 XR 剧情 Demo")
define gui.show_name = True
define config.version = "1.0.13"
define gui.about = _("上海端点星幻境科技有限公司 · 天文馆 XR 剧情可玩样片\n制作：AIGC艺术家 吟游诗人Lab\n仅用于方案展示与评审演示")

define build.name = "TianwenguanXRDemo"

## 固定 16:9，避免黑边/错位
define config.screen_width = 1280
define config.screen_height = 720
define config.physical_width = 1280
define config.physical_height = 720

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.save_directory = "TianwenguanXRDemo-2026"
define config.window_icon = None

## 窗口标题
define config.window_title = u"天文馆 XR 剧情 Demo · 火星救援 × 回到普林斯顿"

## 默认文字速度（0=瞬间，建议 40 打字机效果）
default preferences.text_cps = 40
default preferences.afm_time = 15

## 打包分类（build 时用）
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/_pre_cutout_backup/**', None)
    build.classify('**/_cutout_v2/**', None)
    build.classify('**/_gen_audio.py', None)

